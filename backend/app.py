"""
Text Summarizer Backend
A Flask API for text summarization using Hugging Face transformers.
"""

import logging
from flask import Flask, jsonify, request
from flask_cors import CORS
from transformers import pipeline
from config import Config

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s'
)
logger = logging.getLogger(__name__)

# Initialize Flask app
app = Flask(__name__)

# Initialize the summarization pipeline with a pretrained model
logger.info(f"Loading summarization model: {Config.MODEL_NAME}")
logger.info("This may take a moment on first run...")
summarizer = pipeline("summarization", model=Config.MODEL_NAME)
logger.info("Model loaded successfully!")

# Enable CORS for all routes (allows frontend to make requests)
CORS(app, resources={
    r"/api/*": {
        "origins": Config.ALLOWED_ORIGINS,
        "methods": ["GET", "POST", "OPTIONS"],
        "allow_headers": ["Content-Type"]
    }
})
logger.info(f"CORS enabled for origins: {Config.ALLOWED_ORIGINS}")


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
        if len(text) < Config.MIN_TEXT_LENGTH:
            logger.warning(f"Text too short: {len(text)} chars (min: {Config.MIN_TEXT_LENGTH})")
            return jsonify({
                'error': f'Text too short. Minimum {Config.MIN_TEXT_LENGTH} characters required for summarization.'
            }), 400
        
        # Validate maximum text length to prevent memory issues
        if len(text) > Config.MAX_TEXT_LENGTH:
            logger.warning(f"Text too long: {len(text)} chars (max: {Config.MAX_TEXT_LENGTH})")
            return jsonify({
                'error': f'Text too long. Maximum {Config.MAX_TEXT_LENGTH:,} characters allowed.'
            }), 400
        
        logger.info(f"Processing text of {len(text)} characters")
        
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
        
        logger.info(f"Summary generated: {len(summary)} chars from {len(text)} chars")
        
        return jsonify({
            'summary': summary,
            'original_length': len(text),
            'summary_length': len(summary)
        })
        
    except Exception as e:
        logger.error(f"Summarization failed: {str(e)}")
        return jsonify({
            'error': f'Summarization failed: {str(e)}'
        }), 500

if __name__ == '__main__':
    logger.info(f"Starting server on {Config.HOST}:{Config.PORT}")
    app.run(debug=Config.DEBUG, host=Config.HOST, port=Config.PORT)
