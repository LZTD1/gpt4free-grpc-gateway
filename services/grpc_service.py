from logging import Logger

from pypkg import ai_pb2_grpc, ai_pb2
from pypkg.ai_pb2 import SuggestRequest, ClearHistoryRequest
from services.AiService import AiService


class GRPCService(ai_pb2_grpc.AiServicer):
    def __init__(self, ai: AiService, logger: Logger):
        self.ai = ai
        self.log = logger

    def GetSuggest(self, request: SuggestRequest, context):
        self.log.info(f"Получен запрос от клиента: {request}")
        response, status = self.ai.suggest(request.uid, request.suggest)
        response = ai_pb2.SuggestResponse(
            ok=status,
            request=response,
        )
        self.log.info(f"Отправка ответа: {response}")
        return response

    def ClearHistory(self, request: ClearHistoryRequest, context):
        self.log.info(f"Получен запрос от клиента: {request}")
        self.ai.clear_history(request.uid)
        response = ai_pb2.ClearHistoryResponse(
            ok=True,
        )
        self.log.info(f"Отправка ответа: {response}")
        return response
