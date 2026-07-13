# Simple FastAPI Task Manager API

## Project Description

This is a simple Task Manager REST API developed using FastAPI.
It allows users to perform CRUD (Create, Read, Update, Delete)
operations on tasks.

Each task contains:

- Title
- Description
- Status (Pending / Completed)

The project uses SQLite as the database and SQLAlchemy ORM for
database operations. Pydantic is used for request validation.

---

## Technologies Used

- Python
- FastAPI
- SQLite
- SQLAlchemy ORM
- Pydantic
- Uvicorn

---

## Project Structure

```
Simple FastAPI Task Manager API/

│── main.py
│── database.py
│── models.py
│── schemas.py
│── crud.py
│── requirements.txt
│── README.md
│── task.db
└── task.py
```

---

## Installation

Clone the repository.
Install the required packages.

## Running the Application
Start the FastAPI server.

py -m uvicorn main:app --reload


If the application starts successfully, you will see:

INFO: Uvicorn running on http://127.0.0.1:8000
```

http://127.0.0.1:8000/docs.siddarthha paste this link in a browser you will get
