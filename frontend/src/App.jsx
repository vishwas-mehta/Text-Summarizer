import { useState } from 'react';
import { summarizeText } from './api';
import './App.css';

function App() {
  const [inputText, setInputText] = useState('');
  const [summary, setSummary] = useState('');
  const [isLoading, setIsLoading] = useState(false);
  const [error, setError] = useState('');
  const [stats, setStats] = useState(null);
  const [copied, setCopied] = useState(false);

  const handleSummarize = async () => {
    // Reset states
    setError('');
    setSummary('');
    setStats(null);
    setCopied(false);

    // Validate input
    if (!inputText.trim()) {
      setError('Please enter some text to summarize.');
      return;
    }

    if (inputText.length < 50) {
      setError('Text is too short. Please enter at least 50 characters.');
      return;
    }

    setIsLoading(true);

    try {
      const result = await summarizeText(inputText);
      setSummary(result.summary);
      setStats({
        originalLength: result.original_length,
        summaryLength: result.summary_length,
        reduction: Math.round((1 - result.summary_length / result.original_length) * 100)
      });
    } catch (err) {
      const errorMessage = err.response?.data?.error || 'Failed to summarize. Please try again.';
      setError(errorMessage);
    } finally {
      setIsLoading(false);
    }
  };

  const handleClear = () => {
    setInputText('');
    setSummary('');
    setError('');
    setStats(null);
    setCopied(false);
  };

  const handleCopy = async () => {
    try {
      await navigator.clipboard.writeText(summary);
      setCopied(true);
      setTimeout(() => setCopied(false), 2000);
    } catch (err) {
      console.error('Failed to copy:', err);
    }
  };

  return (
    <div className="app">
      <div className="container">
        {/* Header */}
        <header className="header">
          <div className="logo">
            <span className="logo-icon">✨</span>
            <h1>AI Text Summarizer</h1>
          </div>
          <p className="tagline">Transform long text into concise summaries instantly</p>
        </header>

        {/* Main Content */}
        <main className="main">
          {/* Input Section */}
          <div className="input-section">
            <label htmlFor="input-text" className="section-label">
              <span className="label-icon">📝</span>
              Paste your text
            </label>
            <textarea
              id="input-text"
              className="text-input"
              placeholder="Paste your article, essay, or any long text here... (minimum 50 characters) • Press Ctrl+Enter to summarize"
              value={inputText}
              onChange={(e) => setInputText(e.target.value)}
              onKeyDown={(e) => {
                if ((e.ctrlKey || e.metaKey) && e.key === 'Enter' && inputText.trim() && !isLoading) {
                  handleSummarize();
                }
              }}
              disabled={isLoading}
            />
            <div className="input-footer">
              <span className="char-count">{inputText.length} characters | {inputText.trim() ? inputText.trim().split(/\s+/).length : 0} words</span>
              <div className="button-group">
                <button
                  className="btn btn-secondary"
                  onClick={handleClear}
                  disabled={isLoading || !inputText}
                >
                  Clear
                </button>
                <button
                  className="btn btn-primary"
                  onClick={handleSummarize}
                  disabled={isLoading || !inputText.trim()}
                >
                  {isLoading ? (
                    <>
                      <span className="spinner"></span>
                      Summarizing...
                    </>
                  ) : (
                    <>
                      <span className="btn-icon">🚀</span>
                      Summarize
                    </>
                  )}
                </button>
              </div>
            </div>
          </div>

          {/* Error Message */}
          {error && (
            <div className="error-message">
              <span className="error-icon">⚠️</span>
              {error}
            </div>
          )}

          {/* Result Section */}
          {summary && (
            <div className="result-section">
              <div className="result-header">
                <label className="section-label">
                  <span className="label-icon">✅</span>
                  Summary
                </label>
                <button className="btn btn-copy" onClick={handleCopy}>
                  {copied ? '✓ Copied!' : '📋 Copy'}
                </button>
              </div>
              <div className="result-box">
                <p className="summary-text">{summary}</p>
              </div>
              {stats && (
                <div className="stats">
                  <div className="stat">
                    <span className="stat-value">{stats.originalLength}</span>
                    <span className="stat-label">Original</span>
                  </div>
                  <div className="stat">
                    <span className="stat-value">{stats.summaryLength}</span>
                    <span className="stat-label">Summary</span>
                  </div>
                  <div className="stat highlight">
                    <span className="stat-value">{stats.reduction}%</span>
                    <span className="stat-label">Reduced</span>
                  </div>
                </div>
              )}
            </div>
          )}
        </main>

        {/* Footer */}
        <footer className="footer">
          <p>© 2026 AI Text Summarizer • Powered by Hugging Face Transformers • Built with React & Flask</p>
        </footer>
      </div>
    </div>
  );
}

export default App;
