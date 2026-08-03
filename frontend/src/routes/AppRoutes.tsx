import { Routes, Route, Navigate } from "react-router-dom";

import LoginPage from "../pages/auth/LoginPage";
// import RegisterPage from "../pages/auth/RegisterPage";
// import DashboardPage from "../pages/dashboard/DashboardPage";

export default function AppRoutes() {
  return (
    <Routes>
      <Route path="/" element={<Navigate to="/login" replace />} />

      <Route path="/login" element={<LoginPage />} />

      {/* Uncomment these when you create them */}
      {/* <Route path="/register" element={<RegisterPage />} /> */}
      {/* <Route path="/dashboard" element={<DashboardPage />} /> */}
    </Routes>
  );
}