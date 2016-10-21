#!/usr/bin/env python
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
    request.ssn = m.join(request.headers.get(m.CONTEXT_HEADER))
    request.ssn.debug("election", "%s hey, we got a request" % addr)
    return "Oops, this is a bug!"  # valid service would return JSON


@app.errorhandler(Exception)
def unhandled_exception(e):
    err = traceback.format_exc(e)
    request.ssn.error("election-1.3", err)
    return err, 500


if __name__ == "__main__":
    # initialize the mdk and register our address
    m = mdk.start()
    m.register("election", "1.1.0", addr)

    # register a shutdown hook for timely exit notification
    atexit.register(m.stop)

    app.run(host=host, port=port)
