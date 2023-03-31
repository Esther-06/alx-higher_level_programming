#!/bin/bash
# Script that makes a request to 0.0.0.0:5000/catch_me and get the response
curl -sLX PUT -d "You got me!" 0.0.0.0:5000/catch_me
