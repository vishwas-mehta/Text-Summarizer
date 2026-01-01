"""
Text Summarizer Backend
A Flask API for text summarization using Hugging Face transformers.
"""

from flask import Flask, jsonify, request
from flask_cors import CORS
from transformers import pipeline

# Initialize Flask app
app = Flask(__name__)

# Initialize the summarization pipeline with a pretrained model
# Using t5-small for faster inference (smaller model size)
print("Loading summarization model... This may take a moment on first run.")
summarizer = pipeline("summarization", model="t5-small")
print("Model loaded successfully!")

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
        - text (str): The text to summarize (minimum 50 characters)
    
    Returns:
        - summary (str): The summarized text
        - original_length (int): Character count of original text
        - summary_length (int): Character count of summary
    """
    try:
        data = request.get_json()
        
        # Validate request body exists
        if not data:
            return jsonify({
                'error': 'Invalid request: JSON body required'
            }), 400
        
        # Validate text field exists
        if 'text' not in data:
            return jsonify({
                'error': 'Missing required field: text'
            }), 400
        
        text = data['text'].strip()
        
        # Validate text is not empty
        if not text:
            return jsonify({
                'error': 'Text cannot be empty'
            }), 400
        
        # Validate minimum text length for meaningful summarization
        if len(text) < 50:
            return jsonify({
                'error': 'Text too short. Minimum 50 characters required for summarization.'
            }), 400
        
        # Validate maximum text length to prevent memory issues
        if len(text) > 10000:
            return jsonify({
                'error': 'Text too long. Maximum 10,000 characters allowed.'
            }), 400
        
        # Generate summary using Hugging Face pipeline
        # Adjust max_length and min_length based on input length
        max_len = min(150, max(30, len(text.split()) // 2))
        min_len = min(30, max_len // 2)
        
        result = summarizer(
            text,
            max_length=max_len,
            min_length=min_len,
            do_sample=False
        )
        
        summary = result[0]['summary_text']
        
        return jsonify({
            'summary': summary,
            'original_length': len(text),
            'summary_length': len(summary)
        })
        
    except Exception as e:
        return jsonify({
            'error': f'Summarization failed: {str(e)}'
        }), 500


if __name__ == '__main__':
    app.run(debug=True, port=5000)
