#!/usr/bin/env python

"""ssn

Usage:
    ssn [options] [--route=<namever>]...
    ssn (-h | --help)
    ssn --version

Options:
    -b --bare                        Omit the header.
    -t --trace=<level>               The trace level.
    -r --route=<override>...         Routing override.
    -h --help                        Show the help.
    --version                        Show the version.
"""

import mdk
from docopt import docopt


def isversion(st):
    stripped = "".join([c for c in st if c.isdigit() or c == "."])
    return stripped == st

errmsg = "routing override must be of the form '<service> [<version>] <target> [<version>]', got %s"


def run(args):
    #from mdk_runtime import fakeRuntime
    #runtime = fakeRuntime()
    #runtime.getEnvVarsService().set("DATAWIRE_TOKEN", "")
    #m = mdk.MDKImpl(runtime)
    #ssn = m.session()

    m = mdk.start()
    ssn = m.session()

    level = args.get("--trace", None)
    if level:
        ssn.trace(level)

    for route in args.get("--route") or ():
        names = []
        versions = []

        parts = route.split()
        if len(parts) < 2 or isversion(parts[0]):
            raise ValueError(errmsg % route)

        if len(parts) == 2:
            if isversion(parts[1]):
                raise ValueError(errmsg % route)
            parts.insert(1, "1.0")
            parts.append("1.0")

        if len(parts) == 3:
            if isversion(parts[1]) and isversion(parts[2]):
                parts.insert(2, parts[0])
            elif isversion(parts[1]):
                parts.append("1.0")
            elif isversion(parts[2]):
                parts.insert(1, "1.0")
            else:
                assert False, parts

        if len(parts) != 4:
            raise ValueError(errmsg % route)
        if isversion(parts[0]):
            raise ValueError(errmsg % route)
        if not isversion(parts[1]):
            raise ValueError(errmsg % route)
        if isversion(parts[2]):
            raise ValueError(errmsg % route)
        if not isversion(parts[3]):
            raise ValueError(errmsg % route)
        ssn.route(*parts)

    if args["--bare"]:
        print ssn.externalize()
    else:
        print "%s: %s" % (m.CONTEXT_HEADER, ssn.externalize())

    m.stop()


def main():
    exit(run(docopt(__doc__, version="ssn 1.0")))

if __name__ == '__main__':
    main()
