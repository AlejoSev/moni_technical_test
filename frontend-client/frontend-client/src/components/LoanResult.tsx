import { useLocation, useNavigate } from 'react-router-dom';
import './LoanResult.css';

export const LoanResult = () => {
  const location = useLocation();
  const navigate = useNavigate();
  const result = location.state?.result || 'Resultado desconocido';

  return (
    <div className='page-center'>
      <div className="form-container">
      <h2>Resultado de la solicitud</h2>
      <p>{result}</p>
      <button onClick={() => navigate('/')}>Solicitar otro préstamo</button>
    </div>
    </div>
  );
};
