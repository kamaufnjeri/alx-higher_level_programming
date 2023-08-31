#!/bin/bash
#Allowed methods
curl -sI  "$1"/route_4 | grep "Allow" | cut -d " " -f 2-
