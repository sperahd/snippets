#!/bin/bash

g++ ./redis_string.cpp -I /usr/local/include/ -L /usr/local/lib64/ -l hiredis -o redis-cpp
