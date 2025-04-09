import React, { useState } from 'react';
import axios from 'axios';
import { useNavigate } from 'react-router-dom';
import api from './api.ts';
import './LoginAdmin.css';
import { getCSRFToken } from './csrf';

axios.defaults.withCredentials = true;

export const LoginAdmin = () => {
  const [username, setUsername] = useState('');
  const [password, setPassword] = useState('');
  const navigate = useNavigate();

  const handleSubmit = async (e: React.FormEvent) => {
    e.preventDefault();
    try {
      
      await getCSRFToken();

      const response = await api.post('admin/login', {
        username,
        password,
      });
      navigate('/admin/dashboard');
    } catch (err) {
      alert('Error de autenticación');
    }
  };

  return (
    <div className='page-center'>
        <div className="form-container">
        <h2>Iniciar sesión (Administrador)</h2>
        <form onSubmit={handleSubmit}>
            <label>Username</label>
            <input
            type="text"
            name="username"
            value={username}
            onChange={(e) => setUsername(e.target.value)}
            required
            />
            <label>Password</label>
            <input
            type="password"
            name="password"
            value={password}
            onChange={(e) => setPassword(e.target.value)}
            required
            />
            <button type="submit">Iniciar sesión</button>
        </form>
        </div>
    </div>
  );
};
