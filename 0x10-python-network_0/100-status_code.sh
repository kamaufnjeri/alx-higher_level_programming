#!/bin/bash
#Display the status code
curl -Is "$1" | grep "HTTP/1.1" | cut -d " " -f 2
