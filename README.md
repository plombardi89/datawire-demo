# Phil Lombardi's Demo Script

I wrote my own demo script because I wanted one *I understood* the mechanics of using completely and could modify or adapt on the fly.

## Setup Instructions

1. Ensure `MDK_EXPERIMENTAL=1` is set in `~/.bashrc`
2. Ensure `screen` app is installed.
3. Run `make all`

## Demo 1: Discovery and Modifying a Simple Topology

Demonstrates adding a new service to an existing topology and how a client can just seemlessly integrate with a new service written in a totally different language and framework.

1. Open Mission Control UI

   ```./missionctl`
2. Open demo directory `cd demo1`
3. Launch the initial topology `./hello-flask-up.sh`
4. Open a 2nd terminal and run `./client.py` 

