#!/bin/bash
# JSON FILE post
curl -X POST -d @"$2" -sH "Content-Type: application/json" "$1"
