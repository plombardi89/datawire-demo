#!/usr/bin/env bash

FRONTEND=http://localhost:5000
OVERRIDE=$(../ovr.py --route='election modified_election')

printf "%s\n\n" "DEBUG :: $OVERRIDE"

curl -H "$OVERRIDE" "$FRONTEND"