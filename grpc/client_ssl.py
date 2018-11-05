import time

import grpc

import example_pb2
import example_pb2_grpc

def run():
    certs = None
    with open('server.crt') as f:
        certs = f.read()
    
    #Has to bytes format in python3
    certs = certs.encode('utf-8')
    creds = grpc.ssl_channel_credentials(root_certificates=certs)
    with grpc.secure_channel('127.0.0.1:50051', creds) as channel:
        stub = example_pb2_grpc.ExampleStub(channel)
        a = (time.time())
        msg  = example_pb2.Req(id=0, query="Do you ack?", req_value=131)
        response = stub.RunExample(msg)
        b = (time.time())
    print(b - a)
    print(f'Example client received response, id: {response.id}, message: {response.res_string}')


if __name__ == '__main__':
    run()
