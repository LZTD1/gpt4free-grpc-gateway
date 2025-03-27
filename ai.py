import asyncio
import os
import sys

import grpc
import loguru
import yaml

from pypkg import ai_pb2_grpc
from services.AiService import AiService
from services.grpc_service import GRPCService

# Initialize logger
logger = loguru.logger
logger.remove()


def load_text_file(file_path):
    if os.path.exists(file_path):
        with open(file_path, "r", encoding="utf-8") as file:
            return file.read()
    return ""


def load_config():
    file_path = os.getenv("CONFIG_PATH")
    if not file_path:
        print(f"param file_path is not found in dir, get default {file_path}")
        file_path = './config/prod.cfg.yaml'
    try:
        with open(file_path, 'r') as file:
            cfg = yaml.safe_load(file)
            cfg['ai']["sys_promt"] = load_text_file(cfg['ai']["sys_promt_path"])
            print("Config successfully get from file")

        return cfg
    except FileNotFoundError:
        print('file not found!')
        sys.exit(1)
    except yaml.YAMLError as e:
        print("configuration file cant parsed!", e)
        sys.exit(1)

config = load_config()
logger.add(sys.stdout, level=config['logging']['level'])
if config['logging']['in_file']:
    logger.add("f_{time}.log", format="{time} | {level} | {name}:{function}:{line} - {message} | {extra}",level="DEBUG",rotation="5 MB")



async def serve(grpc_service):
    server = grpc.aio.server()
    ai_pb2_grpc.add_AiServicer_to_server(grpc_service, server)
    server.add_insecure_port(f"{config['server']['host']}:{config['server']['port']}")
    logger.info("Server successfully starter, and listen addr {}", config['server'])
    await server.start()
    await server.wait_for_termination()


async def main():
    ai_service = AiService(config['ai'], logger)
    grpc_service = GRPCService(ai_service)
    await serve(grpc_service)


if __name__ == "__main__":
    asyncio.run(main())
