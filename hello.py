## Git test

from flask import Flask
import socket

## Get my machine hostname
if socket.gethostname().find('.') >= 0:
    hostname=socket.gethostname()
else:
    hostname=socket.gethostbyaddr(socket.gethostname())[0]

app = Flask(__name__)

@app.route('/')
def hello():
    return "Hey IoT World from RPi3: " + hostname

## Run the website and make sure to make
##  it externally visible with 0.0.0.0:5000 (default port)
if __name__ == '__main__':
    app.run(host='0.0.0.0')
