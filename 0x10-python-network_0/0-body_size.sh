#!/usr/bin/env bash
#Size in bites using curl
curl -Is "$1" | grep "Content-Length:" | cut  -d " " -f 2 
