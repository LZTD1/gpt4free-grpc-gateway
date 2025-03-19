import grpc

from pypkg import ai_pb2_grpc, ai_pb2
from pypkg.ai_pb2 import SuggestRequest, ClearHistoryRequest
from services.AiService import AiService


class GRPCService(ai_pb2_grpc.AiServicer):
    def __init__(self, ai: AiService):
        self.ai = ai

    async def GetSuggest(self, request: SuggestRequest, context):
        response, status = await self.ai.suggest(request.uid, request.suggest)
        response = ai_pb2.SuggestResponse(
            ok=status,
            request=response,
        )
        context.set_code(grpc.StatusCode.OK)
        if not status:
            context.set_code(grpc.StatusCode.DEADLINE_EXCEEDED)
        return response

    def ClearHistory(self, request: ClearHistoryRequest, context):
        self.ai.clear_history(request.uid)
        response = ai_pb2.ClearHistoryResponse(
            ok=True,
        )
        context.set_code(grpc.StatusCode.OK)
        return response
