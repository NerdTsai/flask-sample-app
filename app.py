from flask import Flask
import socket

app = Flask(__name__)


@app.route("/")
def hello():
    #hostname = socket.gethostname()
    #IPAddr = socket.gethostbyname(hostname)
    return "Hello! This is a test from IBM."


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
