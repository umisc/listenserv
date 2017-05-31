listenserv
==========

A Python Flask server that logs all requests to the server in custom database.

Introduction
------------

We shouldn't need to create one of these every time we want to do a specific attack; we should just be able to clone, run, and go. A common tool we need is the ability to capture information sent via HTTP GET request to a host we own. Sometimes we want to be able to send information/files as well. This project allows for both with very little configuration.

Installation
------------

You will need:

-	python >= 2.7, >= 3.5
-	flask
-	flask-cors

Then:

```bash
$ sudo python run.py
```

Server will be running on localhost:80.

Considerations
--------------

You may want to edit the run.py file or add your static files to the static/ directory. Static serving files is enabled by default.

Do not run this with a web server such as nginx; there are a few considerable security risks depending on the running version of Flask. Just use this as an example or during CTFs and competitions as a quick and dirty capture server.
