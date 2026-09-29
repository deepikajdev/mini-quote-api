# Mini Quote API

A small beginner-friendly REST API built with **Python and FastAPI**.

## Features

* `GET /` — Check if the API is running
* `GET /quote` — Get a random quote
* `GET /quotes` — Get all quotes
* Interactive API documentation with Swagger UI

## Tech Stack

* Python
* FastAPI
* Uvicorn

## Run Locally

Install the dependencies:

```bash
py -m pip install -r requirements.txt
```

Start the server:

```bash
py -m uvicorn main:app --reload
```

The API will run at:

```text
http://127.0.0.1:8000
```

## API Documentation

Open:

```text
http://127.0.0.1:8000/docs
```

FastAPI automatically provides interactive Swagger documentation.

## Project Structure

```text
mini-quote-api/
├── main.py
├── requirements.txt
└── .gitignore
```

## What I Learned

* Creating a FastAPI application
* Creating GET endpoints
* Using FastAPI decorators
* Returning JSON responses
* Running a FastAPI development server
* Testing endpoints with Swagger UI
* Using Git and GitHub for version control

