#!/usr/bin/env python 

import mdk
import time
import requests
import sys

m = mdk.start()
ssn = m.session()

try:
    while True:
        try:
            print requests.get(ssn.resolve("hello", "1.0").address).text
            time.sleep(1.0)
        except:
            pass
except KeyboardInterrupt:
    sys.exit(0)
