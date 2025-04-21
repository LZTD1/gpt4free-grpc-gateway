import asyncio
from logging import Logger
from typing import Dict, List

import g4f
from g4f import AsyncClient
from g4f.Provider import ProviderUtils
from g4f.providers.retry_provider import RetryProvider

MAX_MSG_HISTORY_LEN = 500


class AiService:
    def __init__(self, config, log: Logger):
        self.users: Dict[int, List[Dict[str, str]]] = {}
        self.client = AsyncClient()
        self.model = config['text_generation']['model']
        self.image_model = config['image_model']
        self.retry_policy = config['retry_policy']
        self.log = log
        self.sys_promt = {
            "role": "system",
            "content": config["sys_promt"]
        }
        self.text_providers = None
        if "providers" in config["text_generation"]:
            providers = config["text_generation"]["providers"].split(",")
            self.text_providers = [ProviderUtils.convert[name] for name in providers]

    def create_user(self, uid: int):
        if uid not in self.users:
            self.log.debug("Created new user with ID: {}", uid)
            self.users[uid] = [self.sys_promt]

    def clear_history(self, uid: int):
        self.users[uid] = [self.sys_promt]

    def add_message(self, uid, role, content):
        self.users[uid].append({
            "role": role,
            "content": content,
        })

    def check_history(self, uid) -> bool:
        if len(self.users[uid]) >= MAX_MSG_HISTORY_LEN:
            self.clear_history(uid)
            return True
        return False

    def change_image_model(self, model: str) -> bool:
        if model in g4f.models._all_models:
            self.log.info("image model was changed {} -> {}", self.image_model, model)
            self.image_model = model
            return True
        return False

    def change_text_model(self, model: str) -> bool:
        if model in g4f.models._all_models:
            self.log.info("text model was changed {} -> {}", self.model, model)
            self.model = model
            return True
        return False

    async def generate_image(self, promt: str, uid: int) -> (str, bool):
        retries = 0
        self.log.info("User request generate_image {}:{}...", uid, promt[:20])
        while retries < self.retry_policy['retry_count']:
            try:
                response, ok = await asyncio.wait_for(
                    self._generate_image(promt),
                    timeout=self.retry_policy['image_timeout']
                )
                if ok:
                    self.log.debug(f"User successfully get response: {response.data[0].url[:20]}...")
                    return response.data[0].url, True
            except asyncio.TimeoutError:
                self.log.debug(
                    f"The _generate_image function timed out (attempt {retries + 1}/{self.retry_policy['retry_count']})")
            except Exception as err:
                self.log.debug(
                    f"The _generate_image returns unexpected error (attempt {retries + 1}/{self.retry_policy['retry_count']})",
                    err)

            if retries < self.retry_policy['retry_count']:
                retries += 1
                await asyncio.sleep(self.retry_policy['retry_timeout'])
            else:
                break

        self.log.warning(
            f"After {self.retry_policy['retry_count']} attempts, failed to receive a response from the server")
        return "Произошла ошибка сервера!", False

    def get_stats(self) -> (str, str):
        """
        returns chat model, image_model
        """
        return self.model, self.image_model

    async def suggest(self, uid, message) -> (str, bool):
        self.create_user(uid)
        if self.check_history(uid):
            self.log.info(f"User {uid} get limit history messages - {MAX_MSG_HISTORY_LEN}")
            return f"Упс, наша история сообщений превысила максимум - {MAX_MSG_HISTORY_LEN} сообщений\nМне пришлось отчистить себе память, задавай вопрос снова!", True

        retries = 0
        self.add_message(uid, "user", message)
        self.log.info("User request suggestion {}:{}...", uid, message[:20])
        while retries < self.retry_policy['retry_count']:
            try:
                response, ok = await asyncio.wait_for(
                    self._suggest(uid),
                    timeout=self.retry_policy['timeout']
                )
                if ok:
                    self.log.debug(f"User successfully get response: {response.choices[0].message.content[:20]}...")
                    self.add_message(uid, "assistant", response.choices[0].message.content)
                    return response.choices[0].message.content, True
            except asyncio.TimeoutError:
                self.log.debug(
                    f"The _suggest function timed out (attempt {retries + 1}/{self.retry_policy['retry_count']})")
            except Exception as err:
                self.log.debug(
                    f"The suggest returns unexpected error (attempt {retries + 1}/{self.retry_policy['retry_count']})",
                    err)

            if retries < self.retry_policy['retry_count']:
                retries += 1
                await asyncio.sleep(self.retry_policy['retry_timeout'])
            else:
                break

        self.log.warning(
            f"After {self.retry_policy['retry_count']} attempts, failed to receive a response from the server")
        self.add_message(uid, "assistant", "error while suggesting.")
        return "Произошла ошибка сервера!", False

    async def _suggest(self, uid: int) -> tuple:

        try:
            prov = None
            if self.text_providers is not None:
                prov = RetryProvider(self.text_providers)
            response = await self.client.chat.completions.create(
                model=self.model,
                messages=self.users[uid],
                web_search=False,
                provider=prov,
            )
            return response, True
        except Exception as e:
            self.log.error("Unexpected error in function _suggest {}", e)
            raise e

    async def _generate_image(self, promt: str):
        try:
            response = await self.client.images.generate(
                model=self.image_model,
                prompt=promt,
                response_format="url",
            )
            return response, True
        except Exception as e:
            self.log.error("Unexpected error in function _generate_image {}", e)
            return None, False
