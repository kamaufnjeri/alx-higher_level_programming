#!/bin/bash
#Display the status code
curl -s -o /dev/null -w "%{http_code}" "$1"
