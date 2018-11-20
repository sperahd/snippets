## Installation steps:

1. Pull hiredis release tar ball:
~~~~
$ wget https://github.com/redis/hiredis/archive/v0.14.0.tar.gz
$ tar -xvzf v0.14.0.tar.gz
$ cd hiredis-0.14.0
$ make
~~~~

2. Copy libhiredis.a or libhiredis.so to one of the paths in LD_LIBRARY_PATH

3. Copy header files to /usr/local/include:
~~~~
cp *.h /usr/local/include
~~~~
