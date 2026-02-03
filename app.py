
from flask import Flask, jsonify
import socket
import datetime

app = Flask(__name__)

@app.route("/")
def home():
    return jsonify({
        "message": "CI/CD Pipeline Working Successfully",
        "version": "v2.0",
        "server": socket.gethostname(),
        "time": datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    })

@app.route("/health")
def health():
    return {"status": "UP"}

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
