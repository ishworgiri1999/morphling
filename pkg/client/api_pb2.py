# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: api.proto
"""Generated protocol buffer code."""
from google.protobuf.internal import builder as _builder
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\tapi.proto\x12\x0b\x61pi.storage\"&\n\x08KeyValue\x12\x0b\n\x03key\x18\x01 \x01(\t\x12\r\n\x05value\x18\x02 \x01(\t\"\x11\n\x0fSaveResultReply\"\x8e\x01\n\x11SaveResultRequest\x12\x11\n\tnamespace\x18\x01 \x01(\t\x12\x12\n\ntrial_name\x18\x02 \x01(\t\x12&\n\x07results\x18\x04 \x03(\x0b\x32\x15.api.storage.KeyValue\x12\x13\n\x0blimitations\x18\x05 \x01(\t\x12\x15\n\rother_metrics\x18\x06 \x01(\t\"9\n\x10GetResultRequest\x12\x11\n\tnamespace\x18\x01 \x01(\t\x12\x12\n\ntrial_name\x18\x02 \x01(\t\"\x8b\x01\n\x0eGetResultReply\x12\x11\n\tnamespace\x18\x01 \x01(\t\x12\x12\n\ntrial_name\x18\x02 \x01(\t\x12&\n\x07results\x18\x04 \x03(\x0b\x32\x15.api.storage.KeyValue\x12\x13\n\x0blimitations\x18\x05 \x01(\t\x12\x15\n\rother_metrics\x18\x06 \x01(\t2\x99\x01\n\x02\x44\x42\x12J\n\nSaveResult\x12\x1e.api.storage.SaveResultRequest\x1a\x1c.api.storage.SaveResultReply\x12G\n\tGetResult\x12\x1d.api.storage.GetResultRequest\x1a\x1b.api.storage.GetResultReplyB\x14Z\x12../grpc_storage/gob\x06proto3')

_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, globals())
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'api_pb2', globals())
if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  DESCRIPTOR._serialized_options = b'Z\022../grpc_storage/go'
  _KEYVALUE._serialized_start=26
  _KEYVALUE._serialized_end=64
  _SAVERESULTREPLY._serialized_start=66
  _SAVERESULTREPLY._serialized_end=83
  _SAVERESULTREQUEST._serialized_start=86
  _SAVERESULTREQUEST._serialized_end=228
  _GETRESULTREQUEST._serialized_start=230
  _GETRESULTREQUEST._serialized_end=287
  _GETRESULTREPLY._serialized_start=290
  _GETRESULTREPLY._serialized_end=429
  _DB._serialized_start=432
  _DB._serialized_end=585
# @@protoc_insertion_point(module_scope)
