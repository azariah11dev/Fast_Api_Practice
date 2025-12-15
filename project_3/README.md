# FastAPI Practice – Project 3

This project is part of a series of small practice runs with **FastAPI**.  
The goal is to understand how to define endpoints, work with path parameters, and return JSON responses.

---

## 📖 Overview
This app demonstrates:
- A root endpoint (`/`) that returns a welcome message.
- A dictionary of sample posts (20 entries with titles, content, and locations).
- A dynamic endpoint (`/post/{id}`) that:
  - Accepts an integer path parameter.
  - Looks up a post by its ID.
  - Returns the post if found, or a message if not in the database.

---

## 🛠️ Technologies Used
- **Python 3.11+**
- **FastAPI** for building the API
- **Uvicorn** as the ASGI server

---

## 🚀 Getting Started
1. Install dependencies:
   ```bash
   pip install fastapi uvicorn