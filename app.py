from flask import Flask, request, jsonify
from bedrock import generate_text
from content_filter import is_safe
from metrics import log_usage
import os

app = Flask(__name__)
API_KEY = os.getenv("API_KEY")

@app.before_request
def verify_api_key():
    if request.headers.get('x-api-key') != API_KEY:
        return jsonify({'error': 'Unauthorized key'}), 401

@app.route('/generate', methods=['POST'])
def generate():
    data = request.get_json()
    prompt = data.get('prompt', '')

    if not prompt:
        return jsonify({'error': 'Prompt is required'}), 400

    if not is_safe(prompt):
        return jsonify({'error': 'Inappropriate content'}), 400

    try:
        response = generate_text(prompt)
        log_usage(prompt)
        return jsonify({'response': response})
    except Exception as e:
        return jsonify({'error': str(e)}), 500

@app.route('/health', methods=['GET'])
def health():
    return jsonify({'status': 'running'}), 200

if __name__ == "__main__":
    port = int(os.getenv("PORT", 8080))
    app.run(host="0.0.0.0", port=port)