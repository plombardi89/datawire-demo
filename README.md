# Phil Lombardi's Demo Script

I wrote my own demo script because I wanted one *I understood* the mechanics of using completely and could modify or adapt on the fly.

## Setup Instructions

1. Ensure `MDK_EXPERIMENTAL=1` is set in `~/.bashrc`
2. Ensure `screen` app is installed.

    Fedora 23/24:
    `sudo -s dnf install screen`
    
3. Ensure runtime dependencies are installed.

    `make all`

## Demo 1: Discovery and Modifying a Simple Topology

Demonstrates adding a new service to an existing topology and how a client can just seamlessly integrate with a new service written in a totally different language and framework.

1. Open Mission Control UI

   `./missionctl`
   
2. Open demo1 directory and launch the base topology.

    ```bash
    cd demo1/
    ./setup-hello-flask.sh
    ```
    
3. Open another terminal and run the simple client.

    ```bash
    . ../venv/bin/activate
    ./client.py
    ```
    
4. Launch the `hello` service written in Node/Express.
    
   `./setup-hello-express.sh`  
    
5. Client has started routing to the Node/Express service as well as the Flask implementations in real time. 
6. Kill the Node/Express implementation `./teardown-hello-express.js`.
7. Client has stopped routing to the Node/Express service but is still talking to the Flask implementations.
8. Cleanup `./teardown-all.sh`

## Demo 2: Integration Bug!

Demonstrates how an existing topology can be safely modified. An existing system with several systems is extended with a broken service. The MDK circuit breaker component kicks-in and stops the bleeding.

1. Open demo2 directory and launch the base topology using microcosm

## Demo 3: Per-request Routing Overrides!

