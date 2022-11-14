# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: service.proto
"""Generated protocol buffer code."""
from google.protobuf.internal import enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\rservice.proto\"C\n\x0fWithdrawRequest\x12\n\n\x02id\x18\x01 \x01(\x05\x12\r\n\x05\x63lock\x18\x02 \x01(\x05\x12\x15\n\x05\x65vent\x18\x03 \x01(\x0b\x32\x06.Event\"B\n\x0e\x44\x65positRequest\x12\n\n\x02id\x18\x01 \x01(\x05\x12\r\n\x05\x63lock\x18\x02 \x01(\x05\x12\x15\n\x05\x65vent\x18\x03 \x01(\x0b\x32\x06.Event\"@\n\x0cQueryRequest\x12\n\n\x02id\x18\x01 \x01(\x05\x12\r\n\x05\x63lock\x18\x02 \x01(\x05\x12\x15\n\x05\x65vent\x18\x03 \x01(\x0b\x32\x06.Event\"X\n\x18WithdrawPropogateRequest\x12\n\n\x02id\x18\x01 \x01(\x05\x12\x10\n\x08\x65vent_id\x18\x02 \x01(\x05\x12\x0f\n\x07\x62\x61lance\x18\x03 \x01(\x05\x12\r\n\x05\x63lock\x18\x04 \x01(\x05\"W\n\x17\x44\x65positPropogateRequest\x12\n\n\x02id\x18\x01 \x01(\x05\x12\x10\n\x08\x65vent_id\x18\x02 \x01(\x05\x12\x0f\n\x07\x62\x61lance\x18\x03 \x01(\x05\x12\r\n\x05\x63lock\x18\x04 \x01(\x05\"A\n\x05\x45vent\x12\n\n\x02id\x18\x01 \x01(\x05\x12\x1d\n\tinterface\x18\x02 \x01(\x0e\x32\n.Interface\x12\r\n\x05money\x18\x03 \x01(\x05\"y\n\x10WithdrawResponse\x12\n\n\x02id\x18\x01 \x01(\x05\x12\x1d\n\tinterface\x18\x02 \x01(\x0e\x32\n.Interface\x12\x17\n\x06result\x18\x03 \x01(\x0e\x32\x07.Result\x12!\n\x0c\x63lock_events\x18\x04 \x03(\x0b\x32\x0b.ClockEvent\"x\n\x0f\x44\x65positResponse\x12\n\n\x02id\x18\x01 \x01(\x05\x12\x1d\n\tinterface\x18\x02 \x01(\x0e\x32\n.Interface\x12\x17\n\x06result\x18\x03 \x01(\x0e\x32\x07.Result\x12!\n\x0c\x63lock_events\x18\x04 \x03(\x0b\x32\x0b.ClockEvent\"b\n\rQueryResponse\x12\n\n\x02id\x18\x01 \x01(\x05\x12\x1d\n\tinterface\x18\x02 \x01(\x0e\x32\n.Interface\x12\r\n\x05money\x18\x03 \x01(\x05\x12\x17\n\x06result\x18\x04 \x01(\x0e\x32\x07.Result\"c\n\x19WithdrawPropogateResponse\x12\n\n\x02id\x18\x01 \x01(\x05\x12\x17\n\x06result\x18\x02 \x01(\x0e\x32\x07.Result\x12!\n\x0c\x63lock_events\x18\x03 \x03(\x0b\x32\x0b.ClockEvent\"b\n\x18\x44\x65positPropogateResponse\x12\n\n\x02id\x18\x01 \x01(\x05\x12\x17\n\x06result\x18\x02 \x01(\x0e\x32\x07.Result\x12!\n\x0c\x63lock_events\x18\x03 \x03(\x0b\x32\x0b.ClockEvent\"G\n\nClockEvent\x12\n\n\x02id\x18\x01 \x01(\x05\x12\x10\n\x08\x65vent_id\x18\x02 \x01(\x05\x12\x0c\n\x04name\x18\x03 \x01(\t\x12\r\n\x05\x63lock\x18\x04 \x01(\x05*.\n\x06Result\x12\n\n\x06uknown\x10\x00\x12\x0b\n\x07success\x10\x01\x12\x0b\n\x07\x66\x61ilure\x10\x02*@\n\tInterface\x12\r\n\tundefined\x10\x00\x12\x0b\n\x07\x64\x65posit\x10\x01\x12\x0c\n\x08withdraw\x10\x02\x12\t\n\x05query\x10\x03\x32\xa4\x02\n\x06\x42ranch\x12,\n\x07\x44\x65posit\x12\x0f.DepositRequest\x1a\x10.DepositResponse\x12/\n\x08Withdraw\x12\x10.WithdrawRequest\x1a\x11.WithdrawResponse\x12&\n\x05Query\x12\r.QueryRequest\x1a\x0e.QueryResponse\x12J\n\x11WithdrawPropogate\x12\x19.WithdrawPropogateRequest\x1a\x1a.WithdrawPropogateResponse\x12G\n\x10\x44\x65positPropogate\x12\x18.DepositPropogateRequest\x1a\x19.DepositPropogateResponseb\x06proto3')

_RESULT = DESCRIPTOR.enum_types_by_name['Result']
Result = enum_type_wrapper.EnumTypeWrapper(_RESULT)
_INTERFACE = DESCRIPTOR.enum_types_by_name['Interface']
Interface = enum_type_wrapper.EnumTypeWrapper(_INTERFACE)
uknown = 0
success = 1
failure = 2
undefined = 0
deposit = 1
withdraw = 2
query = 3


_WITHDRAWREQUEST = DESCRIPTOR.message_types_by_name['WithdrawRequest']
_DEPOSITREQUEST = DESCRIPTOR.message_types_by_name['DepositRequest']
_QUERYREQUEST = DESCRIPTOR.message_types_by_name['QueryRequest']
_WITHDRAWPROPOGATEREQUEST = DESCRIPTOR.message_types_by_name['WithdrawPropogateRequest']
_DEPOSITPROPOGATEREQUEST = DESCRIPTOR.message_types_by_name['DepositPropogateRequest']
_EVENT = DESCRIPTOR.message_types_by_name['Event']
_WITHDRAWRESPONSE = DESCRIPTOR.message_types_by_name['WithdrawResponse']
_DEPOSITRESPONSE = DESCRIPTOR.message_types_by_name['DepositResponse']
_QUERYRESPONSE = DESCRIPTOR.message_types_by_name['QueryResponse']
_WITHDRAWPROPOGATERESPONSE = DESCRIPTOR.message_types_by_name['WithdrawPropogateResponse']
_DEPOSITPROPOGATERESPONSE = DESCRIPTOR.message_types_by_name['DepositPropogateResponse']
_CLOCKEVENT = DESCRIPTOR.message_types_by_name['ClockEvent']
WithdrawRequest = _reflection.GeneratedProtocolMessageType('WithdrawRequest', (_message.Message,), {
  'DESCRIPTOR' : _WITHDRAWREQUEST,
  '__module__' : 'service_pb2'
  # @@protoc_insertion_point(class_scope:WithdrawRequest)
  })
_sym_db.RegisterMessage(WithdrawRequest)

DepositRequest = _reflection.GeneratedProtocolMessageType('DepositRequest', (_message.Message,), {
  'DESCRIPTOR' : _DEPOSITREQUEST,
  '__module__' : 'service_pb2'
  # @@protoc_insertion_point(class_scope:DepositRequest)
  })
_sym_db.RegisterMessage(DepositRequest)

QueryRequest = _reflection.GeneratedProtocolMessageType('QueryRequest', (_message.Message,), {
  'DESCRIPTOR' : _QUERYREQUEST,
  '__module__' : 'service_pb2'
  # @@protoc_insertion_point(class_scope:QueryRequest)
  })
_sym_db.RegisterMessage(QueryRequest)

WithdrawPropogateRequest = _reflection.GeneratedProtocolMessageType('WithdrawPropogateRequest', (_message.Message,), {
  'DESCRIPTOR' : _WITHDRAWPROPOGATEREQUEST,
  '__module__' : 'service_pb2'
  # @@protoc_insertion_point(class_scope:WithdrawPropogateRequest)
  })
_sym_db.RegisterMessage(WithdrawPropogateRequest)

DepositPropogateRequest = _reflection.GeneratedProtocolMessageType('DepositPropogateRequest', (_message.Message,), {
  'DESCRIPTOR' : _DEPOSITPROPOGATEREQUEST,
  '__module__' : 'service_pb2'
  # @@protoc_insertion_point(class_scope:DepositPropogateRequest)
  })
_sym_db.RegisterMessage(DepositPropogateRequest)

Event = _reflection.GeneratedProtocolMessageType('Event', (_message.Message,), {
  'DESCRIPTOR' : _EVENT,
  '__module__' : 'service_pb2'
  # @@protoc_insertion_point(class_scope:Event)
  })
_sym_db.RegisterMessage(Event)

WithdrawResponse = _reflection.GeneratedProtocolMessageType('WithdrawResponse', (_message.Message,), {
  'DESCRIPTOR' : _WITHDRAWRESPONSE,
  '__module__' : 'service_pb2'
  # @@protoc_insertion_point(class_scope:WithdrawResponse)
  })
_sym_db.RegisterMessage(WithdrawResponse)

DepositResponse = _reflection.GeneratedProtocolMessageType('DepositResponse', (_message.Message,), {
  'DESCRIPTOR' : _DEPOSITRESPONSE,
  '__module__' : 'service_pb2'
  # @@protoc_insertion_point(class_scope:DepositResponse)
  })
_sym_db.RegisterMessage(DepositResponse)

QueryResponse = _reflection.GeneratedProtocolMessageType('QueryResponse', (_message.Message,), {
  'DESCRIPTOR' : _QUERYRESPONSE,
  '__module__' : 'service_pb2'
  # @@protoc_insertion_point(class_scope:QueryResponse)
  })
_sym_db.RegisterMessage(QueryResponse)

WithdrawPropogateResponse = _reflection.GeneratedProtocolMessageType('WithdrawPropogateResponse', (_message.Message,), {
  'DESCRIPTOR' : _WITHDRAWPROPOGATERESPONSE,
  '__module__' : 'service_pb2'
  # @@protoc_insertion_point(class_scope:WithdrawPropogateResponse)
  })
_sym_db.RegisterMessage(WithdrawPropogateResponse)

DepositPropogateResponse = _reflection.GeneratedProtocolMessageType('DepositPropogateResponse', (_message.Message,), {
  'DESCRIPTOR' : _DEPOSITPROPOGATERESPONSE,
  '__module__' : 'service_pb2'
  # @@protoc_insertion_point(class_scope:DepositPropogateResponse)
  })
_sym_db.RegisterMessage(DepositPropogateResponse)

ClockEvent = _reflection.GeneratedProtocolMessageType('ClockEvent', (_message.Message,), {
  'DESCRIPTOR' : _CLOCKEVENT,
  '__module__' : 'service_pb2'
  # @@protoc_insertion_point(class_scope:ClockEvent)
  })
_sym_db.RegisterMessage(ClockEvent)

_BRANCH = DESCRIPTOR.services_by_name['Branch']
if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  _RESULT._serialized_start=1085
  _RESULT._serialized_end=1131
  _INTERFACE._serialized_start=1133
  _INTERFACE._serialized_end=1197
  _WITHDRAWREQUEST._serialized_start=17
  _WITHDRAWREQUEST._serialized_end=84
  _DEPOSITREQUEST._serialized_start=86
  _DEPOSITREQUEST._serialized_end=152
  _QUERYREQUEST._serialized_start=154
  _QUERYREQUEST._serialized_end=218
  _WITHDRAWPROPOGATEREQUEST._serialized_start=220
  _WITHDRAWPROPOGATEREQUEST._serialized_end=308
  _DEPOSITPROPOGATEREQUEST._serialized_start=310
  _DEPOSITPROPOGATEREQUEST._serialized_end=397
  _EVENT._serialized_start=399
  _EVENT._serialized_end=464
  _WITHDRAWRESPONSE._serialized_start=466
  _WITHDRAWRESPONSE._serialized_end=587
  _DEPOSITRESPONSE._serialized_start=589
  _DEPOSITRESPONSE._serialized_end=709
  _QUERYRESPONSE._serialized_start=711
  _QUERYRESPONSE._serialized_end=809
  _WITHDRAWPROPOGATERESPONSE._serialized_start=811
  _WITHDRAWPROPOGATERESPONSE._serialized_end=910
  _DEPOSITPROPOGATERESPONSE._serialized_start=912
  _DEPOSITPROPOGATERESPONSE._serialized_end=1010
  _CLOCKEVENT._serialized_start=1012
  _CLOCKEVENT._serialized_end=1083
  _BRANCH._serialized_start=1200
  _BRANCH._serialized_end=1492
# @@protoc_insertion_point(module_scope)
