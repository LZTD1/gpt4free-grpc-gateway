from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union
DESCRIPTOR: _descriptor.FileDescriptor

class ModelType(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    MODEL_UNSPECIFIED: _ClassVar[ModelType]
    IMAGE_MODEL: _ClassVar[ModelType]
    TEXT_MODEL: _ClassVar[ModelType]
MODEL_UNSPECIFIED: ModelType
IMAGE_MODEL: ModelType
TEXT_MODEL: ModelType

class GenerateImageRequest(_message.Message):
    __slots__ = ('uid', 'promt')
    UID_FIELD_NUMBER: _ClassVar[int]
    PROMT_FIELD_NUMBER: _ClassVar[int]
    uid: int
    promt: str

    def __init__(self, uid: _Optional[int]=..., promt: _Optional[str]=...) -> None:
        ...

class GenerateImageResponse(_message.Message):
    __slots__ = ('url',)
    URL_FIELD_NUMBER: _ClassVar[int]
    url: str

    def __init__(self, url: _Optional[str]=...) -> None:
        ...

class ChangeModelRequest(_message.Message):
    __slots__ = ('type', 'model_name')
    TYPE_FIELD_NUMBER: _ClassVar[int]
    MODEL_NAME_FIELD_NUMBER: _ClassVar[int]
    type: ModelType
    model_name: str

    def __init__(self, type: _Optional[_Union[ModelType, str]]=..., model_name: _Optional[str]=...) -> None:
        ...

class ChangeModelResponse(_message.Message):
    __slots__ = ('ok', 'message')
    OK_FIELD_NUMBER: _ClassVar[int]
    MESSAGE_FIELD_NUMBER: _ClassVar[int]
    ok: bool
    message: str

    def __init__(self, ok: bool=..., message: _Optional[str]=...) -> None:
        ...

class GetInformationRequest(_message.Message):
    __slots__ = ()

    def __init__(self) -> None:
        ...

class GetInformationResponse(_message.Message):
    __slots__ = ('chat_model', 'image_model')
    CHAT_MODEL_FIELD_NUMBER: _ClassVar[int]
    IMAGE_MODEL_FIELD_NUMBER: _ClassVar[int]
    chat_model: str
    image_model: str

    def __init__(self, chat_model: _Optional[str]=..., image_model: _Optional[str]=...) -> None:
        ...

class SuggestRequest(_message.Message):
    __slots__ = ('uid', 'suggest')
    UID_FIELD_NUMBER: _ClassVar[int]
    SUGGEST_FIELD_NUMBER: _ClassVar[int]
    uid: int
    suggest: str

    def __init__(self, uid: _Optional[int]=..., suggest: _Optional[str]=...) -> None:
        ...

class SuggestResponse(_message.Message):
    __slots__ = ('ok', 'request')
    OK_FIELD_NUMBER: _ClassVar[int]
    REQUEST_FIELD_NUMBER: _ClassVar[int]
    ok: bool
    request: str

    def __init__(self, ok: bool=..., request: _Optional[str]=...) -> None:
        ...

class ClearHistoryRequest(_message.Message):
    __slots__ = ('uid',)
    UID_FIELD_NUMBER: _ClassVar[int]
    uid: int

    def __init__(self, uid: _Optional[int]=...) -> None:
        ...

class ClearHistoryResponse(_message.Message):
    __slots__ = ('ok',)
    OK_FIELD_NUMBER: _ClassVar[int]
    ok: bool

    def __init__(self, ok: bool=...) -> None:
        ...