import axios from 'axios';
import { getFromCookie, getCSRFToken } from './csrf';

const api = axios.create({
  baseURL: 'http://localhost:8000/api',
  withCredentials: true,
});

api.interceptors.request.use(
  async (config) => {
    const methodsWithCSRF = ['post', 'put', 'patch', 'delete'];

    if (methodsWithCSRF.includes(config.method?.toLowerCase() || '')) {
      await getCSRFToken();

      const csrfToken = getFromCookie('csrftoken');
      if (csrfToken) {
        config.headers['X-CSRFToken'] = csrfToken;
      }
    }

    return config;
  },
  (error) => Promise.reject(error)
);

export default api;
