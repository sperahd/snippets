# Commands to figure out common network/socket actiivity

## To check all the open tcp connections

~~~~
$ ss -t -a
~~~~

## To check which process is bound to a port(listening on a port)

~~~~
$ netstat -nlp | grep -i "$port"
~~~~
