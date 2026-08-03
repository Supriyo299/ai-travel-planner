import AuthLayout from "../../components/layout/AuthLayout";

export default function LoginPage() {
  return (
    <AuthLayout>
      <div className="space-y-6">
        <div>
          <h1 className="text-3xl font-bold text-white">
            Welcome Back 👋
          </h1>

          <p className="text-slate-400 mt-2">
            Sign in to your AI Travel Planner
          </p>
        </div>

        <button className="w-full rounded-lg bg-blue-600 py-3 font-semibold text-white hover:bg-blue-700">
          Login
        </button>
      </div>
    </AuthLayout>
  );
}