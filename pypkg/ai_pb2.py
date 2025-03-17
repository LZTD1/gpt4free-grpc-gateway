"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import runtime_version as _runtime_version
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder

_runtime_version.ValidateProtobufRuntimeVersion(_runtime_version.Domain.PUBLIC, 5, 29, 0, '', 'ai.proto')
_sym_db = _symbol_database.Default()
DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(
    b'\n\x08ai.proto\x12\x05pypkg".\n\x0eSuggestRequest\x12\x0b\n\x03uid\x18\x01 \x01(\x03\x12\x0f\n\x07suggest\x18\x02 \x01(\t".\n\x0fSuggestResponse\x12\n\n\x02ok\x18\x01 \x01(\x08\x12\x0f\n\x07request\x18\x02 \x01(\t""\n\x13ClearHistoryRequest\x12\x0b\n\x03uid\x18\x01 \x01(\x03""\n\x14ClearHistoryResponse\x12\n\n\x02ok\x18\x01 \x01(\x082\x8a\x01\n\x02Ai\x12;\n\nGetSuggest\x12\x15.pypkg.SuggestRequest\x1a\x16.pypkg.SuggestResponse\x12G\n\x0cClearHistory\x12\x1a.pypkg.ClearHistoryRequest\x1a\x1b.pypkg.ClearHistoryResponseb\x06proto3')
_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'ai_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
    DESCRIPTOR._loaded_options = None
    _globals['_SUGGESTREQUEST']._serialized_start = 19
    _globals['_SUGGESTREQUEST']._serialized_end = 65
    _globals['_SUGGESTRESPONSE']._serialized_start = 67
    _globals['_SUGGESTRESPONSE']._serialized_end = 113
    _globals['_CLEARHISTORYREQUEST']._serialized_start = 115
    _globals['_CLEARHISTORYREQUEST']._serialized_end = 149
    _globals['_CLEARHISTORYRESPONSE']._serialized_start = 151
    _globals['_CLEARHISTORYRESPONSE']._serialized_end = 185
    _globals['_AI']._serialized_start = 188
    _globals['_AI']._serialized_end = 326
