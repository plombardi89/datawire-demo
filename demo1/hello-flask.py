#!/usr/bin/env python

# basic imports plus grab our host, port from the command line
import sys
import mdk
import atexit
import traceback
from flask import Flask, request

host, port = sys.argv[1:3]
addr = "http://%s:%s" % (host, port)

app = Flask(__name__)


@app.route("/")
def hello():
    request.ssn = m.join(request.headers.get(m.CONTEXT_HEADER))  # ########
    request.ssn.info("hello-flask", "Received a request!")       # ########
    return "Hello World! (Flask {})".format(port)


@app.errorhandler(Exception)
def unhandled_exception(e):
    err = traceback.format_exc(e)
    request.ssn.error("hello-flask", err)                        # ########
    return err, 500


if __name__ == "__main__":
    # initialize the mdk and register our address
    m = mdk.start()                                              # ########
    m.register("hello", "1.0", addr)                             # ########
    # register a shutdown hook for timely exit notification
    atexit.register(m.stop)                                      # ########

    app.run(host=host, port=port)
