export async function getCSRFToken() {
  console.log("✅ Llamando a getCSRFToken()");
  await fetch("http://localhost:8000/api/csrf", {
    credentials: "include",
  });
}

export function getFromCookie(name: string): string | undefined {
  return document.cookie
    .split("; ")
    .find(row => row.startsWith(name + "="))
    ?.split("=")[1];
}
