## To map a container port to a host port in docker run

~~~~
docker run -p 80:8080
~~~~
The above docker run command exposes docker port 80 as 8080 on the host

## Sending data from container to Host on UDP

~~~~
docker run -p 12345:12345/udp
~~~~
