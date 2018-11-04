## Python GRPC specific

# Installation using pip
pip install grpcio grpcio-tools googleapis-common-protos

# Compiling proto file with proto defs and service defs
python -m grpc.tools.protoc example.proto --proto_path=. --python_out=. --grpc_python_out=.
