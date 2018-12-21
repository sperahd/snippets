## Run a consul server

~~~~
$ docker run  -p 8500:8500 -p 8600:8600/udp --name=consul consul:latest agent -server -bootstrap -ui -client=0.0.0.0
~~~~

## Putting a value using curl

~~~~
$ curl -X PUT -d 'abcdefghi' http://127.0.0.1:8500/v1/kv/foo/boo/goo/roo
~~~~
returns true if key created

## Getting a value using curl

~~~~
curl http://127.0.0.1:8500/v1/kv/foo/boo/goo/roo
~~~~

Response:
~~~~
[{"LockIndex":0,"Key":"foo/boo/goo/roo","Flags":0,"Value":"YWJjZGVmZ2hp","CreateIndex":63,"ModifyIndex":63}]
~~~~

The value part of the above json is base64 encoded. To get raw string value:

~~~~
curl http://127.0.0.1:8500/v1/kv/foo/boo/goo/roo?raw
~~~~
Response

~~~~
abcdefghi
~~~~

## Putting a file using curl
example.json
~~~~
{
    "ip": "w.x.y.z",
    "port": "9090"
}
~~~~

Curl call
~~~~
curl -X PUT -d @example.json http://127.0.0.1:8500/v1/kv/my_service/json/discover
~~~~

Get for a file is same as for a key

~~~~
curl http://127.0.0.1:8500/v1/kv/my_service/json/discover?raw
~~~~

Response:
~~~~
{    "ip": "w.x.y.x",    "port": "9090"}
~~~~

## List all the entries under a hierarchy

~~~~
curl -s 'http://127.0.0.1:8500/v1/kv/my_service?recurse=true
~~~~
Note: recurse does not work with raw

## Place a watch on a key

Prerequisites: The key to watch should be present, else we should set some default value.

Get the current ModifyIndex of the key:

~~~~
curl -s 'http://127.0.0.1:8500/v1/kv/my_service/json/discovery'
~~~~

Response

~~~~
[{"LockIndex":0,"Key":"my_service/json/discovery","Flags":0,"Value":"eyAgICAiaXAiOiAidy54LnkueCIsICAgICJwb3J0IjogIjkwOTAifQ==","CreateIndex":450,"ModifyIndex":451}]
~~~~

Place a watch:

~~~~
curl -s 'http://127.0.0.1:8500/v1/kv/my_service/json/discovery?index=451'
~~~~
The above command will block until the key is modified.(Updated or deleted)
