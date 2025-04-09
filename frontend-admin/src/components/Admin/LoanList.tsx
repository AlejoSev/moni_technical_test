import React, { useState, useEffect } from 'react';
import axios from 'axios';
import './LoanList.css';

axios.defaults.withCredentials = true;

export const LoanList = () => {
  const [loans, setLoans] = useState([]);
  const [editingId, setEditingId] = useState<number | null>(null);
  const [editForm, setEditForm] = useState({
    first_name: '',
    last_name: '',
    amount: 0,
  });

  useEffect(() => {
    const fetchLoans = async () => {
      const token = localStorage.getItem('authToken');

      console.log(token);
      
      if (!token) {
        alert('No tienes sesión iniciada');
        return;
      }
      
      try {
        const response = await fetch('http://localhost:8000/api/admin/loans', {
          method: 'GET',
          headers: {
            'Authorization': `Bearer ${token}`,
            'Content-Type': 'application/json',
          },
        });

        if (response.ok) {
          const data = await response.json();
          const sortedLoans = data.sort((a, b) =>
            new Date(b.created_at).getTime() - new Date(a.created_at).getTime()
          );
          setLoans(sortedLoans);
        } else {
          alert('Error al cargar los préstamos');
        }
      } catch (err) {
        alert('Error al cargar los préstamos');
      }
    };

    fetchLoans();
  }, []);

  const handleDelete = async (id: number) => {
    const confirm = window.confirm('¿Estás seguro que querés eliminar este préstamo?');
    if (!confirm) return;
  
    const token = localStorage.getItem('authToken');
  
    if (!token) {
      alert('No tienes sesión iniciada');
      return;
    }
  
    try {
      const response = await fetch(`http://localhost:8000/api/admin/loans/${id}/`, {
        method: 'DELETE',
        headers: {
          'Authorization': `Bearer ${token}`,
          'Content-Type': 'application/json',
        },
      });
  
      if (response.ok) {
        setLoans(loans.filter((loan) => loan.id !== id));
      } else {
        alert('Error al eliminar el préstamo');
      }
    } catch (err) {
      alert('Error al eliminar el préstamo');
    }
  };

  const handleEditClick = (loan) => {
    setEditingId(loan.id);
    setEditForm({
      first_name: loan.first_name,
      last_name: loan.last_name,
      amount: loan.amount,
    });
  };

  const handleEditChange = (e) => {
    const { name, value } = e.target;
    setEditForm((prev) => ({ ...prev, [name]: value }));
  };

  const handleSave = async (id: number) => {
    const token = localStorage.getItem('authToken');
  
    if (!token) {
      alert('No tienes sesión iniciada');
      return;
    }
  
    try {
      const response = await fetch(`http://localhost:8000/api/admin/loans/${id}/`, {
        method: 'PATCH',
        headers: {
          'Authorization': `Bearer ${token}`,
          'Content-Type': 'application/json',
        },
        body: JSON.stringify({
          ...editForm,
          amount: parseFloat(editForm.amount as any),
        }),
      });
  
      if (!response.ok) {
        throw new Error('Error al guardar los cambios');
      }
  
      setEditingId(null);
  
      const loansResponse = await fetch('http://localhost:8000/api/admin/loans', {
        method: 'GET',
        headers: {
          'Authorization': `Bearer ${token}`,
          'Content-Type': 'application/json',
        },
      });
  
      if (!loansResponse.ok) {
        throw new Error('Error al cargar los préstamos');
      }
  
      const data = await loansResponse.json();
      const sortedLoans = data.sort((a, b) =>
        new Date(b.created_at).getTime() - new Date(a.created_at).getTime()
      );
      setLoans(sortedLoans);
    } catch (err) {
      alert(err.message || 'Error al guardar los cambios');
    }
  };

  const renderStatusBadge = (approved: boolean) => (
    <span className={`status-badge ${approved ? 'status-approved' : 'status-rejected'}`}>
      {approved ? 'Aprobado' : 'Rechazado'}
    </span>
  );

  return (
    <div className="admin-wrapper">
      <h2 className="fixed-title">Listado de Préstamos</h2>
      <div className="admin-container">
        {loans.length === 0 ? (
          <p>No hay solicitudes registradas.</p>
        ) : (
          <ul className="loan-list">
            {loans.map((loan) => (
              <li key={loan.id} className="loan-card">
                <div className="loan-header">
                  <p><strong>{loan.first_name} {loan.last_name}</strong></p>
                  <span className="loan-date">
                    {new Date(loan.created_at).toLocaleString('es-AR', {
                      day: '2-digit',
                      month: '2-digit',
                      year: 'numeric',
                      hour: '2-digit',
                      minute: '2-digit',
                    })}
                  </span>
                </div>

                {editingId === loan.id ? (
                  <div className="edit-section">
                  <label>
                    Nombre:
                    <input
                      type="text"
                      name="first_name"
                      value={editForm.first_name}
                      onChange={handleEditChange}
                    />
                  </label>
                  <label>
                    Apellido:
                    <input
                      type="text"
                      name="last_name"
                      value={editForm.last_name}
                      onChange={handleEditChange}
                    />
                  </label>
                  <label>
                    Monto:
                    <input
                      type="number"
                      name="amount"
                      value={editForm.amount}
                      onChange={handleEditChange}
                    />
                  </label>
                
                  <p>Estado: {renderStatusBadge(loan.approved)}</p>
                
                  <div className="loan-actions">
                    <button className="edit-btn" onClick={() => handleSave(loan.id)}>Guardar</button>
                    <button className="delete-btn" onClick={() => setEditingId(null)}>Cancelar</button>
                  </div>
                </div>
                ) : (
                  <>
                    <p>Monto solicitado: ${loan.amount}</p>
                    <p>Estado: {renderStatusBadge(loan.approved)}</p>
                    <div className="loan-actions">
                      <button className="edit-btn" onClick={() => handleEditClick(loan)}>Editar</button>
                      <button className="delete-btn" onClick={() => handleDelete(loan.id)}>Eliminar</button>
                    </div>
                  </>
                )}
              </li>
            ))}
          </ul>
        )}
      </div>
    </div>
  );
};
