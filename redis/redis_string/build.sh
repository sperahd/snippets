#!/bin/bash

g++ redis_client.cpp -I /usr/local/include/ -l hiredis -o redis-cpp
