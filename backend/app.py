"""
Text Summarizer Backend
A Flask API for text summarization using Hugging Face transformers.
"""

from flask import Flask, jsonify

# Initialize Flask app
app = Flask(__name__)


@app.route('/')
def index():
    """Root endpoint with API information."""
    return jsonify({
        'name': 'Text Summarizer API',
        'version': '1.0.0',
        'description': 'AI-powered text summarization service'
    })


if __name__ == '__main__':
    app.run(debug=True, port=5000)
