import { api } from "../lib/api";

export async function login(data: {
  email: string;
  password: string;
}) {
  const form = new URLSearchParams();

  form.append("username", data.email);
  form.append("password", data.password);

  const response = await api.post("/auth/login", form, {
    headers: {
      "Content-Type": "application/x-www-form-urlencoded",
    },
  });

  return response.data;
}