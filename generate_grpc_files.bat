@echo off

if not exist account mkdir account
if not exist miiverse mkdir miiverse
if not exist api mkdir api
if not exist friends mkdir friends

python -m grpc_tools.protoc ^
  --proto_path=grpc-protobufs/account ^
  --proto_path=grpc-protobufs/miiverse ^
  --proto_path=grpc-protobufs/api ^
  --proto_path=grpc-protobufs/friends ^
  --python_out=account ^
  --grpc_python_out=account ^
  grpc-protobufs/account/*.proto

python -m grpc_tools.protoc ^
  --proto_path=grpc-protobufs/miiverse ^
  --proto_path=grpc-protobufs/account ^
  --proto_path=grpc-protobufs/api ^
  --proto_path=grpc-protobufs/friends ^
  --python_out=miiverse ^
  --grpc_python_out=miiverse ^
  grpc-protobufs/miiverse/*.proto

python -m grpc_tools.protoc ^
  --proto_path=grpc-protobufs/api ^
  --proto_path=grpc-protobufs/account ^
  --proto_path=grpc-protobufs/miiverse ^
  --proto_path=grpc-protobufs/friends ^
  --python_out=api ^
  --grpc_python_out=api ^
  grpc-protobufs/api/*.proto

python -m grpc_tools.protoc ^
  --proto_path=grpc-protobufs/friends ^
  --proto_path=grpc-protobufs/account ^
  --proto_path=grpc-protobufs/miiverse ^
  --proto_path=grpc-protobufs/api ^
  --python_out=friends ^
  --grpc_python_out=friends ^
  grpc-protobufs/friends/*.proto
