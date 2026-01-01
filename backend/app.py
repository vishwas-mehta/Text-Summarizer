"""
Text Summarizer Backend
A Flask API for text summarization using Hugging Face transformers.
"""

from flask import Flask, jsonify, request
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


@app.route('/api/summarize', methods=['POST'])
def summarize():
    """
    Summarize the provided text.
    
    Request body:
        - text (str): The text to summarize
    
    Returns:
        - summary (str): The summarized text
        - original_length (int): Character count of original text
        - summary_length (int): Character count of summary
    """
    data = request.get_json()
    
    if not data or 'text' not in data:
        return jsonify({
            'error': 'Missing required field: text'
        }), 400
    
    text = data['text']
    
    # TODO: Implement actual summarization with Hugging Face
    summary = f"Summary placeholder for text of length {len(text)}"
    
    return jsonify({
        'summary': summary,
        'original_length': len(text),
        'summary_length': len(summary)
    })


if __name__ == '__main__':
    app.run(debug=True, port=5000)
