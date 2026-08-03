import AuthLayout from "../../components/layout/AuthLayout";

export default function RegisterPage() {
  return (
    <AuthLayout>
      <div className="space-y-6">
        <div>
          <h1 className="text-3xl font-bold text-white">
            Create Account
          </h1>

          <p className="text-slate-400 mt-2">
            Join AI Travel Planner
          </p>
        </div>

        <button className="w-full rounded-lg bg-green-600 py-3 font-semibold text-white hover:bg-green-700">
          Register
        </button>
      </div>
    </AuthLayout>
  );
}