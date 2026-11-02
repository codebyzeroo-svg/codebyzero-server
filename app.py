import os
from flask import Flask, jsonify, request

app = Flask(__name__)

@app.route("/", methods=["GET"])
def home():
    return jsonify({
        "server": "CODEBYZERO",
        "status": "online",
        "version": "1.0.0"
    })

@app.route("/api/status", methods=["GET"])
def status():
    return jsonify({
        "online": True,
        "message": "Server is working"
    })

@app.route("/api/data", methods=["POST"])
def receive_data():
    data = request.get_json(silent=True) or {}

    return jsonify({
        "success": True,
        "received": data
    })

if __name__ == "__main__":
    app.run(
        host="0.0.0.0",
        port=int(os.environ.get("PORT", 10000))
    )
