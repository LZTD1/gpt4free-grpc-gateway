from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Optional as _Optional
DESCRIPTOR: _descriptor.FileDescriptor

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