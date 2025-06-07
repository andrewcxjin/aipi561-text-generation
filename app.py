from flask import Flask, request, jsonify, render_template_string
from bedrock import generate_text
from content_filter import is_safe
from metrics import log_usage
import os

app = Flask(__name__)
API_KEY = os.getenv("API_KEY", "testsecretkey0608")

HTML_TEMPLATE = """
<!doctype html>
<html>
<head>
  <title>Text Generator</title>
</head>
<body>
  <h2>Text Generator</h2>
  <input id="prompt" placeholder="Type your prompt..." />
  <button onclick="generate()">Generate</button>
  <pre id="result"></pre>

  <script>
    async function generate() {
      const prompt = document.getElementById("prompt").value;
      const response = await fetch("/generate", {
        method: "POST",
        headers: {
          "Authorization": "Bearer testsecretkey0608",
          "Content-Type": "application/json"
        },
        body: JSON.stringify({ prompt: prompt })
      });
      const data = await response.json();
      document.getElementById("result").innerText = JSON.stringify(data, null, 2);
    }
  </script>
</body>
</html>
"""

@app.route("/")
def index():
    return render_template_string(HTML_TEMPLATE, api_key=API_KEY)

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