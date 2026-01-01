"""
Configuration settings for the Text Summarizer API.
"""

import os


class Config:
    """Application configuration."""
    
    # Flask settings
    DEBUG = os.getenv('FLASK_DEBUG', 'True').lower() == 'true'
    PORT = int(os.getenv('PORT', 5000))
    HOST = os.getenv('HOST', '0.0.0.0')
    
    # Model settings
    MODEL_NAME = os.getenv('MODEL_NAME', 't5-small')
    
    # Summarization parameters
    MAX_SUMMARY_LENGTH = int(os.getenv('MAX_SUMMARY_LENGTH', 150))
    MIN_SUMMARY_LENGTH = int(os.getenv('MIN_SUMMARY_LENGTH', 30))
    
    # Input validation
    MIN_TEXT_LENGTH = int(os.getenv('MIN_TEXT_LENGTH', 50))
    MAX_TEXT_LENGTH = int(os.getenv('MAX_TEXT_LENGTH', 10000))
    
    # CORS settings
    ALLOWED_ORIGINS = os.getenv(
        'ALLOWED_ORIGINS',
        'http://localhost:3000,http://localhost:5173'
    ).split(',')
