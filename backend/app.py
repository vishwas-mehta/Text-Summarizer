"""
Text Summarizer Backend
A Flask API for text summarization using Hugging Face transformers.
"""

from flask import Flask, jsonify
from flask_cors import CORS

# Initialize Flask app
app = Flask(__name__)

# Enable CORS for all routes (allows frontend to make requests)
CORS(app, resources={
    r"/api/*": {
        "origins": ["http://localhost:3000", "http://localhost:5173"],
        "methods": ["GET", "POST", "OPTIONS"],
        "allow_headers": ["Content-Type"]
    }
})


@app.route('/')
def index():
    """Root endpoint with API information."""
    return jsonify({
        'name': 'Text Summarizer API',
        'version': '1.0.0',
        'description': 'AI-powered text summarization service'
    })


@app.route('/api/health', methods=['GET'])
def health_check():
    """Health check endpoint for monitoring."""
    return jsonify({
        'status': 'healthy',
        'message': 'Text Summarizer API is running'
    })


if __name__ == '__main__':
    app.run(debug=True, port=5000)
