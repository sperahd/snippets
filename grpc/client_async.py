import time

import grpc

import example_pb2
import example_pb2_grpc

def run():
    with grpc.insecure_channel('localhost:50051') as channel:
        res = None
        stub = example_pb2_grpc.ExampleStub(channel)
        print(time.time())
        msg  = example_pb2.Req(id=0, query="Do you ack?", req_value=131)
        print(time.time())
        
        ## future allows a wait on the response from the server
        response = stub.RunExample.future(msg)
        res = response.result()

        if res:
            print(f'ASYNC response received {res}')
    #print(f'Example client received response, id: {response.id}, message: {response.res_string}')


if __name__ == '__main__':
    run()
