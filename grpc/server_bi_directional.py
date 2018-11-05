from concurrent import futures

import grpc

import example_pb2
import example_pb2_grpc
import time
from google.protobuf import json_format as json_format

class Example(example_pb2_grpc.ExampleServicer):
    def RunExample(self, request, context):
        print(json_format.MessageToJson(request))
        if request.req_value == 131:
            yield example_pb2.Res(id=1, res_string="Yes, I ack")
        else:
            yield example_pb2.Res(id=999, res_string="Unidentifed request received, auto destruction in 3...")
        
    #This guy yields rather than returning to simulate server push
    def RunExample2(self, request, context):
        print(json_format.MessageToJson(request))
        if request.req_value == 131:
            return example_pb2.Res(id=1, res_string="Yes, I ack")
        else:
            return example_pb2.Res(id=999, res_string="Unidentifed request received, auto destruction in 3...")
        """
        while True:
            time.sleep(10)
            yield example_pb2.Res(id=1, res_string="I demand you to listen to me")
        """

def serve():
    ## What is this? 
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    
    ##What is this??
    example_pb2_grpc.add_ExampleServicer_to_server(Example(), server)
    
    ##Example of secure port as well
    server.add_insecure_port('[::]:50051')
    
    server.start()
    try:
        while True:
            time.sleep(5)
    except KeyboardInterrupt:
        server.stop(0)


if __name__ == '__main__':
     serve()
