#!/usr/bin/env node

"use strict";

if (process.argv.length != 4) {
    console.log(process.argv)
    throw "usage: hello-express <host> <port>";
}

var host = process.argv[2];
var port = parseInt(process.argv[3]);
var addr = "http://" + host + ":" + port.toString();

var m = require("datawire_mdk").mdk.init();                           //////////
var express = require("express");
var app = express();

app.get("/", function (req, res) {
    // Join the logging context from the request, if possible:
    var ssn = m.join(req.get("X-MDK-Context"));                       //////////
    ssn.info("hello-express", "Received a request!");                 //////////
    res.send("Hello World (Node/Express " + port + ")");
});

var server = app.listen(port, host);

m.register("hello", "1.0", addr);                                     //////////
m.start();                                                            //////////

process.on("SIGINT", function (code) {
    m.stop();                                                         //////////
    server.close();
});
