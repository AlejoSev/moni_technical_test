import { BrowserRouter as Router, Routes, Route } from 'react-router-dom';
import { LoanForm } from './components/LoanForm';
import { LoanResult } from './components/LoanResult';

function App() {
  return (
    <Router>
      <Routes>
        <Route path="/" element={<LoanForm />} />
        <Route path="/resultado" element={<LoanResult />} />
      </Routes>
    </Router>
  );
}

export default App;