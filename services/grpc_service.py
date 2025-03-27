import grpc

from pypkg import ai_pb2_grpc, ai_pb2
from pypkg.ai_pb2 import ChangeModelRequest, GenerateImageRequest, GetInformationRequest, ModelType, SuggestRequest, ClearHistoryRequest
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
    
    def GetInformation(self, request: GetInformationRequest, context):
        chat_model, image_model = self.ai.get_stats()
        response = ai_pb2.GetInformationResponse(
            chat_model=chat_model,
            image_model=image_model
        )
        context.set_code(grpc.StatusCode.OK)
        return response

    def ChangeModel(self, request: ChangeModelRequest, context):
        response = ai_pb2.ChangeModelResponse()
        if request.type == ModelType.MODEL_UNSPECIFIED:
            context.set_code(grpc.StatusCode.NOT_FOUND)
            context.set_details('model type is undefinded')
            return NotImplementedError('model type is undefinded')

        result = False
        if request.type == ModelType.IMAGE_MODEL:
            result = self.ai.change_image_model(request.model_name)
        if request.type == ModelType.IMAGE_MODEL:
            result = self.ai.change_text_model(request.model_name)
        response.ok = result
        if not result:
            response.message = "model not found"
        
        context.set_code(grpc.StatusCode.OK)
        return response
    
    async def GenerateImage(self, request: GenerateImageRequest, context):
        url, ok = await self.ai.generate_image(request.promt, request.uid)
        response = ai_pb2.GenerateImageResponse(
            url=url,
        )
        context.set_code(grpc.StatusCode.OK)
        if not ok:
            context.set_code(grpc.StatusCode.DEADLINE_EXCEEDED)
        return response