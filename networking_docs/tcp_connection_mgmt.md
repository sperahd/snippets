# Master link

http://www.pcvr.nl/tcpip/tcp_conn.htm

# Notes
1. TCP connection is full-duplex one i.e. data can flow in any direction independently and each direction should shut down independently.

2. TCP also works on a conecpt of half-close, i.e. one end can close the connection(FIN) but the other end can be still be in an active connection and keep sending data in the other direction(NON FIN)

# Connection establishment protocol

Three-way handshake

1. Client sends a SYN segment specifying the port number of the server that the client wants to connect to, client also sends its ISN(Initial sequence number).

2. The server responds to this SYN from client with the following info, 1. server's ISN, 2. ACKing the client's SYN by adding one to client's ISN.

3. The client again responds to this SYN from server by adding one to the server's SYN and ACKing it to the server.

The side that sends the first SYN is said to perform an active open. The other side, which receives this SYN and sends the next SYN, performs a passive open

# Connection termination protocol

1. Client sends a FIN.
2. Server acknowledges this FIN by ACKing incremented client's ISN
3. Server sends a FIN.
4. Client acknowledges this FIN by ACKing incremented server's ISN.
