## Services, Methods, Arguments and Return Types

1. GRPC allows for creation of a service, definition of multiple methods with parameters and return vals.
2. Default Interface definition language is Protocol Buffers.
3. GRPC allows for only one input parameter type and exactly one return value type. If needed multiple messages can be clubbed into a single message using proto definitions to allow for multiple types of message in a single RPC call.
4. GRPC allows a stream of input parameters and a stream of return values of the same type.

# Code Snippets
~~~~

service HelloService {
  rpc SayHello (HelloRequest) returns (HelloResponse);
  rpc SayBye (ByeRequest) returns (ByeResponse);
}
message ByeRequest {
  string greeting = 1;
}

message ByeResponse {
  string reply = 1;
}


message HelloRequest {
  string greeting = 1;
}

message HelloResponse {
  string reply = 1;
}

rpc LotsOfReplies(HelloRequest) returns (stream HelloResponse){
}

rpc LotsOfGreetings(stream HelloRequest) returns (HelloResponse) {
}

rpc BidiHello(stream HelloRequest) returns (stream HelloResponse){
}

~~~~

## Top level API supports
1. Server has to implement the services defined by the grpc service.2
2. Client calls the service methods by creating a local stub.
3. Both Sync and Async rpc calls are allowed.

## RPC life cycle
1. Deadlines/Timeouts - gRPC allows clients to specify how long they are willing to wait for an RPC to complete before the RPC is terminated with the error DEADLINE_EXCEEDED. On the server side, the server can query to see if a particular RPC has timed out, or how much time is left to complete the RPC
2. Cancellation - An RPC call can be terminated by both the client as well as the server, the cancellation is not mandated to be idempotent by the protocol but the implementation can take care of this if requred.
3. Metadata - Metadata is information about a particular RPC call (such as authentication details) in the form of a list of key-value pairs, where the keys are strings and the values are typically strings (but can be binary data). Metadata is opaque to gRPC itself - it lets the client provide information associated with the call to the server and vice versa.
4. Channels - A gRPC channel provides a connection to a gRPC server on a specified host and port and is used when creating a client stub (or just “client” in some languages). Clients can specify channel arguments to modify gRPC’s default behaviour, such as switching on and off message compression. A channel has state, including connected and idle.

## Streaming 

# Unary RPC (https://grpc.io/docs/guides/concepts.html#unary-rpc)
1. Client calls service method on the client stub, the server is notified with client's metadata, method name and the deadline(if applicable). 
2. The server computes the method and the responds to the client's request with it's own metadata and return value.
3. Client receives the return value is done with the RPC.

# Server streaming RPC (https://grpc.io/docs/guides/concepts.html#server-streaming-rpc)
1. Same a unary RPC but the server sends a stream of response after receiving the request and then may/may not send trailing metadata

# Client streaming RPC (https://grpc.io/docs/guides/concepts.html#server-streaming-rpc)
1. Same a server streaming RPC but in this case the client sends a stream of requests before the server calculates the response.

# Bi-directional streaming RPC (https://grpc.io/docs/guides/concepts.html#bidirectional-streaming-rpc)
1. Call is initiated by the client, the server may wait or send response immediately. Next the server and client can talk to each other in any order. Client and server can now ping pong each other.

# Notes
1. Multiple client connections on a single server port are allowed.
2. Are unsolicited messages from the server to client allowed?
