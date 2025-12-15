# FastAPI Beginner Practice

This is a small practice project built with **FastAPI** to explore the basics of creating routes, handling parameters, and returning JSON responses.

---

## 📖 Overview
The app demonstrates:
- A root endpoint (`/`) that returns a simple "Hello World!" message.
- A dynamic endpoint (`/items/{item_id}`) that:
  - Accepts an integer path parameter.
  - Uses conditional logic to return different responses depending on the value.

---

## 🛠️ Technologies Used
- **Python 3.11+**
- **FastAPI** for building the API
- **Uvicorn** as the ASGI server

---

## 🚀 Getting Started
1. Install dependencies:
   ```bash
   uv add fastapi uvicorn