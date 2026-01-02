# AI Text Summarizer

A full-stack web application that generates concise summaries from long text inputs using a pretrained NLP model. This project demonstrates the integration of modern NLP capabilities with a clean REST API and beautiful React frontend.

![Python](https://img.shields.io/badge/Python-3.9+-blue.svg)
![Flask](https://img.shields.io/badge/Flask-3.0-green.svg)
![React](https://img.shields.io/badge/React-18-61dafb.svg)
![Hugging Face](https://img.shields.io/badge/Hugging%20Face-Transformers-orange.svg)

## ✨ Features

- **AI-Powered Summarization**: Uses Hugging Face's T5 model for state-of-the-art text summarization
- **Modern React UI**: Beautiful dark theme with glassmorphism effects and animations
- **RESTful API**: Clean Flask-based API with proper error handling
- **Real-time Stats**: Shows original length, summary length, and reduction percentage
- **Copy to Clipboard**: One-click copy functionality for summaries
- **Responsive Design**: Works seamlessly on desktop and mobile devices
- **Input Validation**: Comprehensive validation for text length and format

## 🛠️ Tech Stack

### Backend
- **Flask** - Python web framework
- **Flask-CORS** - Cross-Origin Resource Sharing
- **Hugging Face Transformers** - Pre-trained NLP models
- **PyTorch** - Deep learning framework

### Frontend
- **React 18** - UI library
- **Vite** - Build tool and dev server
- **Axios** - HTTP client
- **CSS3** - Custom styling with animations

## 📁 Project Structure

```
text-summarizer/
│
├── backend/
│   ├── app.py              # Main Flask application
│   ├── config.py           # Configuration settings
│   └── requirements.txt    # Python dependencies
│
├── frontend/
│   ├── src/
│   │   ├── App.jsx         # Main React component
│   │   ├── api.js          # API service layer
│   │   ├── index.css       # Global styles
│   │   └── main.jsx        # React entry point
│   ├── index.html          # HTML template
│   ├── package.json        # Node dependencies
│   └── vite.config.js      # Vite configuration
│
└── README.md
```

## 🚀 Installation

### Prerequisites
- Python 3.9 or higher
- Node.js 18 or higher
- npm or yarn

### Backend Setup

1. **Navigate to backend directory**
   ```bash
   cd backend
   ```

2. **Create a virtual environment**
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

4. **Run the server**
   ```bash
   python app.py
   ```
   The API will be available at `http://localhost:5000`

### Frontend Setup

1. **Navigate to frontend directory**
   ```bash
   cd frontend
   ```

2. **Install dependencies**
   ```bash
   npm install
   ```

3. **Start development server**
   ```bash
   npm run dev
   ```
   The app will be available at `http://localhost:5173`

## 📖 API Documentation

### Endpoints

#### `GET /`
Returns API information.

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

### Example Usage

```bash
curl -X POST http://localhost:5000/api/summarize \
  -H "Content-Type: application/json" \
  -d '{"text": "Artificial intelligence has transformed the way we interact with technology..."}'
```

## ⚙️ Configuration

Environment variables for the backend:

| Variable | Default | Description |
|----------|---------|-------------|
| `MODEL_NAME` | `t5-small` | Hugging Face model to use |
| `PORT` | `5000` | Server port |
| `MIN_TEXT_LENGTH` | `50` | Minimum input text length |
| `MAX_TEXT_LENGTH` | `10000` | Maximum input text length |

## 📝 Resume-Ready Description

> **AI Text Summarizer | Flask, React, NLP**
> 
> Built a full-stack web application that generates concise summaries from long text inputs using a pretrained NLP model. Developed REST APIs in Flask for text processing and integrated them with a React frontend. Implemented CORS handling and efficient inference for real-time summarization.

## 🖼️ Screenshots

The application features:
- Dark theme with gradient accents
- Glassmorphism card effects
- Smooth animations and transitions
- Real-time character counting
- Statistics showing text reduction

## 📄 License

This project is open source and available under the [MIT License](LICENSE).

## 👤 Author

**Vishwas Mehta**
- GitHub: [@vishwas-mehta](https://github.com/vishwas-mehta)
