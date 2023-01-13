import re

from flask import Flask, jsonify, request

app = Flask(__name__)


@app.route("/process")
def process():
    """Process text"""
    text = request.args.get("text", "")
    preprocessed_text = re.sub(r"\s+", " ", text)
    return jsonify({"originalText": text, "processed": preprocessed_text}), 200
