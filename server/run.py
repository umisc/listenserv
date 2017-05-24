"""Run a server that takes all GET and POST requests and dumps them."""

from flask import Flask, request, send_from_directory

app = Flask(__name__)


@app.route('/')
def route():
    """Get all GET and POST requests and dump them to logs."""
    # Print, log, and return.
    print(request.url)
    with open("cap.log", "a") as f:
        f.write(str(request.url) + "\n")

    return request.url


# @app.route('/<path:path>')
# def staticserve(path):
#     """Serve a file from your static directory."""
#     return app.send_static_file(path)

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=80)
