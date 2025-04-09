import { Routes, Route } from 'react-router-dom';
import { Dashboard } from '../components/Admin/Dashboard';
import { LoginAdmin } from '../components/Admin/LoginAdmin';
import { LoanList } from '../components/Admin/LoanList';

export const AdminRoutes = () => {
  return (
    <Routes>
      <Route path="/admin/login" element={<LoginAdmin />} />
      <Route path="/admin/dashboard" element={<Dashboard />} />
      <Route path="/admin/loans" element={<LoanList />} />
    </Routes>
  );
};
