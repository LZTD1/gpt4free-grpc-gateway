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
logger.add("f_{time}.log", format="{time} | {level} | {name}:{function}:{line} - {message} | {extra}", level="DEBUG",
           rotation="5 MB")


def load_config():
    file_path = os.getenv("CONFIG_PATH")
    if not file_path:
        logger.critical("param file_path not found!", file_path)
    try:
        with open(file_path, 'r') as file:
            cfg = yaml.safe_load(file)
            logger.debug("Config successfully get from file")
        return cfg
    except FileNotFoundError:
        logger.critical('file not found!')
        sys.exit(1)
    except yaml.YAMLError as e:
        logger.critical("configuration file cant parsed!", e)
        sys.exit(1)


config = load_config()
logger.level(config['logging']['level'])


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
