import React from 'react';
import { Link } from 'react-router-dom';

export const Dashboard = () => {
  return (
    <div className="dashboard-container">
      <h2>Dashboard Admin</h2>
      <nav>
        <ul>
          <li><Link to="/admin/loans">Ver Préstamos</Link></li>
        </ul>
      </nav>
    </div>
  );
};
