import { useForm } from "react-hook-form";
import { zodResolver } from "@hookform/resolvers/zod";
import { toast } from "react-hot-toast";

import AuthLayout from "../../components/layout/AuthLayout";
import { Button } from "../../components/ui/button";
import { Input } from "../../components/ui/input";
import { Label } from "../../components/ui/label";

import {
  loginSchema,
  type LoginForm,
} from "../../lib/validations/auth";

import { login } from "../../services/auth.service";
import { useAuthStore } from "../../store/auth-store";

export default function LoginPage() {
  const setToken = useAuthStore((state) => state.setToken);

  const {
    register,
    handleSubmit,
    formState: { errors, isSubmitting },
  } = useForm<LoginForm>({
    resolver: zodResolver(loginSchema),
  });

  async function onSubmit(data: LoginForm) {
    try {
      const response = await login(data);

      setToken(response.access_token);

      toast.success("Login successful!");
    } catch {
      toast.error("Invalid email or password");
    }
  }

  return (
    <AuthLayout>
      <form
        onSubmit={handleSubmit(onSubmit)}
        className="space-y-6"
      >
        <div>
          <h1 className="text-3xl font-bold text-white">
            Welcome Back 👋
          </h1>

          <p className="mt-2 text-slate-400">
            Sign in to your AI Travel Planner
          </p>
        </div>

        <div className="space-y-2">
          <Label>Email</Label>

          <Input
            type="email"
            placeholder="you@example.com"
            {...register("email")}
          />

          {errors.email && (
            <p className="text-sm text-red-500">
              {errors.email.message}
            </p>
          )}
        </div>

        <div className="space-y-2">
          <Label>Password</Label>

          <Input
            type="password"
            placeholder="••••••••"
            {...register("password")}
          />

          {errors.password && (
            <p className="text-sm text-red-500">
              {errors.password.message}
            </p>
          )}
        </div>

        <Button
          type="submit"
          className="w-full"
          disabled={isSubmitting}
        >
          {isSubmitting ? "Signing in..." : "Login"}
        </Button>
      </form>
    </AuthLayout>
  );
}