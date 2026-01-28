from flask import Flask, request, jsonify
import sys

app = Flask(__name__)
storage = {}

@app.route("/put", methods=["PUT"])
def put_value():
    data = request.json
    key = data.get("key")
    value = data.get("value")

    if key is None or value is None:
        return jsonify({"error": "key and value required"}), 400

    storage[key] = value
    return jsonify({"status": "ok"}), 200


@app.route("/get", methods=["GET"])
def get_value():
    key = request.args.get("key")
    if key not in storage:
        return jsonify({"error": "key not found"}), 404

    return jsonify({"value": storage[key]}), 200


if __name__ == "__main__":
    port = int(sys.argv[1]) if len(sys.argv) > 1 else 5000
    app.run(port=port)
