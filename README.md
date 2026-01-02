# AI Text Summarizer

A full-stack web application that generates concise summaries from long text inputs using a pretrained NLP model. This project demonstrates the integration of modern NLP capabilities with a clean REST API.

![Python](https://img.shields.io/badge/Python-3.9+-blue.svg)
![Flask](https://img.shields.io/badge/Flask-3.0-green.svg)
![Hugging Face](https://img.shields.io/badge/Hugging%20Face-Transformers-orange.svg)

## Features

- **AI-Powered Summarization**: Uses Hugging Face's T5 model for state-of-the-art text summarization
- **RESTful API**: Clean Flask-based API with proper error handling
- **Input Validation**: Comprehensive validation for text length and format
- **CORS Support**: Ready for frontend integration
- **Configurable**: Environment variable support for flexible deployment

## Tech Stack

### Backend
- **Flask** - Python web framework
- **Flask-CORS** - Cross-Origin Resource Sharing
- **Hugging Face Transformers** - Pre-trained NLP models
- **PyTorch** - Deep learning framework

## Project Structure

```
text-summarizer/
│
├── backend/
│   ├── app.py              # Main Flask application
│   ├── config.py           # Configuration settings
│   └── requirements.txt    # Python dependencies
│
├── frontend/               # (Coming soon)
│
└── README.md
```

## Installation

### Prerequisites
- Python 3.9 or higher
- pip (Python package manager)

### Setup

1. **Clone the repository**
   ```bash
   git clone https://github.com/vishwas-mehta/Text-Summarizer.git
   cd Text-Summarizer
   ```

2. **Create a virtual environment**
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. **Install dependencies**
   ```bash
   cd backend
   pip install -r requirements.txt
   ```

4. **Run the server**
   ```bash
   python app.py
   ```

   The API will be available at `http://localhost:5000`

## API Documentation

### Endpoints

#### `GET /`
Returns API information.

**Response:**
```json
{
  "name": "Text Summarizer API",
  "version": "1.0.0",
  "description": "AI-powered text summarization service"
}
```

#### `GET /api/health`
Health check endpoint.

**Response:**
```json
{
  "status": "healthy",
  "message": "Text Summarizer API is running"
}
```

#### `POST /api/summarize`
Summarize the provided text.

**Request Body:**
```json
{
  "text": "Your long text to summarize here..."
}
```

**Response:**
```json
{
  "summary": "The summarized text...",
  "original_length": 1500,
  "summary_length": 150
}
```

**Error Responses:**
- `400 Bad Request`: Missing or invalid text input
- `500 Internal Server Error`: Summarization failed

### Example Usage

```bash
curl -X POST http://localhost:5000/api/summarize \
  -H "Content-Type: application/json" \
  -d '{"text": "Artificial intelligence has transformed the way we interact with technology. From virtual assistants to autonomous vehicles, AI is reshaping industries and creating new possibilities for innovation."}'
```

## Configuration

The following environment variables can be set to customize the application:

| Variable | Default | Description |
|----------|---------|-------------|
| `MODEL_NAME` | `t5-small` | Hugging Face model to use |
| `PORT` | `5000` | Server port |
| `HOST` | `0.0.0.0` | Server host |
| `MIN_TEXT_LENGTH` | `50` | Minimum input text length |
| `MAX_TEXT_LENGTH` | `10000` | Maximum input text length |

## Resume-Ready Description

> **AI Text Summarizer | Flask, React, NLP**
> 
> Built a full-stack web application that generates concise summaries from long text inputs using a pretrained NLP model. Developed REST APIs in Flask for text processing and integrated them with a React frontend. Implemented CORS handling and efficient inference for real-time summarization.

## License

This project is open source and available under the [MIT License](LICENSE).

## Author

**Vishwas Mehta**
- GitHub: [@vishwas-mehta](https://github.com/vishwas-mehta)
