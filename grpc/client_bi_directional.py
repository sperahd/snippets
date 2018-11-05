import time

import grpc

import example_pb2
import example_pb2_grpc

def run():
    with grpc.insecure_channel('localhost:50051') as channel:
        stub = example_pb2_grpc.ExampleStub(channel)
        print(time.time())
        msg  = example_pb2.Req(id=0, query="Do you ack?", req_value=131)
        print(time.time())
        response1 = stub.RunExample2(msg)
        print(f'Example client received response, id: {response1.id}, message: {response1.res_string}')
        #response1 = stub.RunExample2.future(msg)
        #res1 = response1.result()
        #response2 = stub.RunExample(msg)
        #print(f'Example client received response, id: {response2.id}, message: {response2.res_string}')

        #if res1:
            #print(f'Unsolicited(fake) response received {res}')
    print('connection terminated')

if __name__ == '__main__':
    run()
