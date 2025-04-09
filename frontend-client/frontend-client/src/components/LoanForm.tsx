import React, { useState } from 'react';
import axios from 'axios';
import { useNavigate } from 'react-router-dom';
import './LoanForm.css';


export const LoanForm = () => {
	const [formData, setFormData] = useState({
		dni: '',
		first_name: '',
		last_name: '',
		gender: 'M',
		email: '',
		amount: '',
	});

	const handleChange = (e: React.ChangeEvent<HTMLInputElement | HTMLSelectElement>) => {
		setFormData({ ...formData, [e.target.name]: e.target.value });
	};

	const navigate = useNavigate();

	const handleSubmit = async (e: React.FormEvent) => {
		e.preventDefault();
		try {
		  const response = await axios.post('/api/loans/', formData);
		  const resultMessage = response.data.msg;
		  navigate('/resultado', { state: { result: resultMessage } });
		} catch (err) {
		  alert('Error al enviar el formulario');
		}
	  };

	return (
		<div className="page-center">
			<div className="form-container">
			<h2>Solicitar Préstamo</h2>
			<form onSubmit={handleSubmit}>
				<label>DNI</label>
				<input type="text" name="dni" value={formData.dni} onChange={handleChange} required />

				<label>Nombre</label>
				<input type="text" name="first_name" value={formData.first_name} onChange={handleChange} required />

				<label>Apellido</label>
				<input type="text" name="last_name" value={formData.last_name} onChange={handleChange} required />

				<label>Género</label>
				<select name="gender" value={formData.gender} onChange={handleChange}>
					<option value="M">Masculino</option>
					<option value="F">Femenino</option>
					<option value="O">Otro</option>
				</select>

				<label>Email</label>
				<input type="email" name="email" value={formData.email} onChange={handleChange} required />

				<label>Monto solicitado</label>
				<input type="number" name="amount" value={formData.amount} onChange={handleChange} required />

				<button type="submit">Enviar solicitud</button>
			</form>
		</div>
		</div>
	);
};
