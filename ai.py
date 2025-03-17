from concurrent import futures

import grpc
import logging

from pypkg import ai_pb2_grpc
from services.AiService import AiService
from services.grpc_service import GRPCService

logging.basicConfig(level=logging.INFO)


def serve(grpc_service, port, logger):
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    ai_pb2_grpc.add_AiServicer_to_server(grpc_service, server)
    server.add_insecure_port(f"[::]:{port}")
    logger.info(f"Сервер запущен и слушает порт {port}")
    server.start()
    server.wait_for_termination()

def main():
    logger = logging.getLogger(__name__)
    ai_service = AiService("gpt-4o-mini", logger)
    grpc_service = GRPCService(ai_service, logger)

    serve(grpc_service, "50051", logger)

if __name__ == "__main__":
    main()