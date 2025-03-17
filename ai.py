import logging
from concurrent import futures

import grpc

from pypkg import ai_pb2_grpc
from services.AiService import AiService
from services.grpc_service import GRPCService
import os
from dotenv import load_dotenv

load_dotenv()
logging.basicConfig(level=logging.INFO)

def serve(grpc_service, port, logger):
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    ai_pb2_grpc.add_AiServicer_to_server(grpc_service, server)
    server.add_insecure_port(f"[::]:{port}")
    logger.info(f"Сервер запущен и слушает порт {port}")
    server.start()
    server.wait_for_termination()


def main():
    model = os.getenv("AI_MODEL")
    port = os.getenv("GRPC_PORT")

    logger = logging.getLogger(__name__)
    ai_service = AiService(model, logger)
    grpc_service = GRPCService(ai_service, logger)

    serve(grpc_service, port, logger)


if __name__ == "__main__":
    main()
