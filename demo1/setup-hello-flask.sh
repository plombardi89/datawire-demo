#!/usr/bin/env bash

screen -dmS hf1 ./hello-flask.py localhost 5000
screen -dmS hf2 ./hello-flask.py localhost 5001
