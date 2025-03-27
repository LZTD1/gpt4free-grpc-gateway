"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import runtime_version as _runtime_version
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
_runtime_version.ValidateProtobufRuntimeVersion(_runtime_version.Domain.PUBLIC, 5, 29, 0, '', 'ai.proto')
_sym_db = _symbol_database.Default()
DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x08ai.proto\x12\x05pypkg"2\n\x14GenerateImageRequest\x12\x0b\n\x03uid\x18\x01 \x01(\x03\x12\r\n\x05promt\x18\x02 \x01(\t"$\n\x15GenerateImageResponse\x12\x0b\n\x03url\x18\x01 \x01(\t"H\n\x12ChangeModelRequest\x12\x1e\n\x04type\x18\x01 \x01(\x0e2\x10.pypkg.ModelType\x12\x12\n\nmodel_name\x18\x02 \x01(\t"2\n\x13ChangeModelResponse\x12\n\n\x02ok\x18\x01 \x01(\x08\x12\x0f\n\x07message\x18\x02 \x01(\t"\x17\n\x15GetInformationRequest"A\n\x16GetInformationResponse\x12\x12\n\nchat_model\x18\x01 \x01(\t\x12\x13\n\x0bimage_model\x18\x02 \x01(\t".\n\x0eSuggestRequest\x12\x0b\n\x03uid\x18\x01 \x01(\x03\x12\x0f\n\x07suggest\x18\x02 \x01(\t".\n\x0fSuggestResponse\x12\n\n\x02ok\x18\x01 \x01(\x08\x12\x0f\n\x07request\x18\x02 \x01(\t""\n\x13ClearHistoryRequest\x12\x0b\n\x03uid\x18\x01 \x01(\x03""\n\x14ClearHistoryResponse\x12\n\n\x02ok\x18\x01 \x01(\x08*C\n\tModelType\x12\x15\n\x11MODEL_UNSPECIFIED\x10\x00\x12\x0f\n\x0bIMAGE_MODEL\x10\x01\x12\x0e\n\nTEXT_MODEL\x10\x022\xeb\x02\n\x02Ai\x12;\n\nGetSuggest\x12\x15.pypkg.SuggestRequest\x1a\x16.pypkg.SuggestResponse\x12G\n\x0cClearHistory\x12\x1a.pypkg.ClearHistoryRequest\x1a\x1b.pypkg.ClearHistoryResponse\x12M\n\x0eGetInformation\x12\x1c.pypkg.GetInformationRequest\x1a\x1d.pypkg.GetInformationResponse\x12D\n\x0bChangeModel\x12\x19.pypkg.ChangeModelRequest\x1a\x1a.pypkg.ChangeModelResponse\x12J\n\rGenerateImage\x12\x1b.pypkg.GenerateImageRequest\x1a\x1c.pypkg.GenerateImageResponseb\x06proto3')
_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'ai_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
    DESCRIPTOR._loaded_options = None
    _globals['_MODELTYPE']._serialized_start = 495
    _globals['_MODELTYPE']._serialized_end = 562
    _globals['_GENERATEIMAGEREQUEST']._serialized_start = 19
    _globals['_GENERATEIMAGEREQUEST']._serialized_end = 69
    _globals['_GENERATEIMAGERESPONSE']._serialized_start = 71
    _globals['_GENERATEIMAGERESPONSE']._serialized_end = 107
    _globals['_CHANGEMODELREQUEST']._serialized_start = 109
    _globals['_CHANGEMODELREQUEST']._serialized_end = 181
    _globals['_CHANGEMODELRESPONSE']._serialized_start = 183
    _globals['_CHANGEMODELRESPONSE']._serialized_end = 233
    _globals['_GETINFORMATIONREQUEST']._serialized_start = 235
    _globals['_GETINFORMATIONREQUEST']._serialized_end = 258
    _globals['_GETINFORMATIONRESPONSE']._serialized_start = 260
    _globals['_GETINFORMATIONRESPONSE']._serialized_end = 325
    _globals['_SUGGESTREQUEST']._serialized_start = 327
    _globals['_SUGGESTREQUEST']._serialized_end = 373
    _globals['_SUGGESTRESPONSE']._serialized_start = 375
    _globals['_SUGGESTRESPONSE']._serialized_end = 421
    _globals['_CLEARHISTORYREQUEST']._serialized_start = 423
    _globals['_CLEARHISTORYREQUEST']._serialized_end = 457
    _globals['_CLEARHISTORYRESPONSE']._serialized_start = 459
    _globals['_CLEARHISTORYRESPONSE']._serialized_end = 493
    _globals['_AI']._serialized_start = 565
    _globals['_AI']._serialized_end = 928