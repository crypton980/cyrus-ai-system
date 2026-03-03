from flask import Flask, jsonify

app = Flask(__name__)


@app.route("/")
def index():
    return jsonify({"name": "Cyrus AI System", "status": "running"})


@app.route("/health")
def health():
    return jsonify({"status": "ok"})


if __name__ == "__main__":
    # For local development only; use gunicorn in production.
    app.run(host="0.0.0.0", port=5000, debug=False)
