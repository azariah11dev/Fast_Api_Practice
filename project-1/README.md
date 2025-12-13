# FastAPI Practice Project

A beginner practice run with **FastAPI**, exploring how to build simple API endpoints, handle path parameters, and return JSON responses. This project is meant as a learning exercise and a starting point for deeper FastAPI development.

---

## 📖 Overview
This app demonstrates:
- A root endpoint (`/`) that returns a "Hello World" message.
- A posts dictionary with sample data.
- A dynamic endpoint (`/post/{id}`) that:
  - Accepts an integer path parameter.
  - Looks up a post by its ID.
  - Returns the post if found, or an error message if not.

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