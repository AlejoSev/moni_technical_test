import { StrictMode } from 'react';
import { createRoot } from 'react-dom/client';
import { BrowserRouter, Routes, Route } from 'react-router-dom';
import './index.css';

import { LoginAdmin } from './components/Admin/LoginAdmin';
import { LoanList } from './components/Admin/LoanList';

createRoot(document.getElementById('root')!).render(
  <StrictMode>
    <BrowserRouter>
      <Routes>
        <Route path="/admin/login" element={<LoginAdmin />} />
        <Route path="/admin/dashboard" element={<LoanList />} />
      </Routes>
    </BrowserRouter>
  </StrictMode>,
);
