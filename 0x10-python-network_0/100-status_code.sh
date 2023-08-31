#!/bin/bash
#Display the status code
curl -Is 127.0.0.1:5000/npv | grep "HTTP/1.1" | cut -d " " -f 2 -o
