/**
 * API Service Layer for Text Summarizer
 * Handles all communication with the Flask backend
 */

import axios from 'axios';

// API base URL - points to Flask backend
const API_BASE_URL = 'http://localhost:5000';

// Create axios instance with default config
const api = axios.create({
  baseURL: API_BASE_URL,
  headers: {
    'Content-Type': 'application/json',
  },
  timeout: 90000, // 90 seconds timeout for longer summarization tasks
});

/**
 * Check if the API is healthy
 * @returns {Promise<Object>} Health status
 */
export const checkHealth = async () => {
  const response = await api.get('/api/health');
  return response.data;
};

/**
 * Summarize the provided text
 * @param {string} text - The text to summarize
 * @returns {Promise<Object>} Summary result with original and summary lengths
 */
export const summarizeText = async (text) => {
  const response = await api.post('/api/summarize', { text });
  return response.data;
};

/**
 * Get API version and model information
 * @returns {Promise<Object>} Version and config info
 */
export const getVersion = async () => {
  const response = await api.get('/api/version');
  return response.data;
};

export default api;
