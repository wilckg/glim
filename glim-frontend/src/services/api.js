import axios from 'axios';

const api = axios.create({
  baseURL: 'https://glim-backend.onrender.com'
});

export default api;