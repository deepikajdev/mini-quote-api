# Mini Quote API

A small beginner-friendly REST API built with **Python and FastAPI**.

## Features

* `GET /` — Check if the API is running
* `GET /quote` — Get a random quote
* `GET /quote/{id}` — Get a specific quote by ID (returns 404 if not found)
* `GET /quotes` — Get all quotes
* `GET /quotes?author=NAME` — Filter quotes by author name (case-insensitive)
* `POST /quotes` — Add a new quote with automatic ID assignment
* Interactive API documentation with Swagger UI

## Tech Stack

* Python
* FastAPI
* Uvicorn
* Pydantic

## Run Locally

1. Install the dependencies:

```bash
py -m pip install -r requirements.txt
```

2. Start the server:

```bash
py -m uvicorn main:app --reload
```

3. The API will run at:

```text
http://127.0.0.1:8000
```

## API Endpoints & Examples

### 1. Check API Status
* **Endpoint:** `GET /`
* **Description:** Basic health check message.
* **Example Request:**
  ```bash
  curl http://127.0.0.1:8000/
  ```
* **Example Response (200 OK):**
  ```json
  {
    "message": "Welcome to the Mini Quote API!"
  }
  ```

---

### 2. Get a Random Quote
* **Endpoint:** `GET /quote`
* **Description:** Returns a random quote from the collection.
* **Example Request:**
  ```bash
  curl http://127.0.0.1:8000/quote
  ```
* **Example Response (200 OK):**
  ```json
  {
    "id": 2,
    "author": "Steve Jobs",
    "text": "The only way to do great work is to love what you do."
  }
  ```

---

### 3. Get Quote by ID
* **Endpoint:** `GET /quote/{id}`
* **Description:** Retrieves a quote by its integer ID.
* **Example Request:**
  ```bash
  curl http://127.0.0.1:8000/quote/1
  ```
* **Example Response (200 OK):**
  ```json
  {
    "id": 1,
    "author": "Albert Einstein",
    "text": "Life is like riding a bicycle. To keep your balance, you must keep moving."
  }
  ```
* **Error Example (404 Not Found):**
  ```bash
  curl http://127.0.0.1:8000/quote/999
  ```
  ```json
  {
    "detail": "Quote with ID 999 not found"
  }
  ```

---

### 4. Get All Quotes
* **Endpoint:** `GET /quotes`
* **Description:** Returns a list of all stored quotes.
* **Example Request:**
  ```bash
  curl http://127.0.0.1:8000/quotes
  ```
* **Example Response (200 OK):**
  ```json
  [
    {
      "id": 1,
      "author": "Albert Einstein",
      "text": "Life is like riding a bicycle. To keep your balance, you must keep moving."
    },
    {
      "id": 2,
      "author": "Steve Jobs",
      "text": "The only way to do great work is to love what you do."
    },
    {
      "id": 3,
      "author": "Eleanor Roosevelt",
      "text": "The future belongs to those who believe in the beauty of their dreams."
    }
  ]
  ```

---

### 5. Filter Quotes by Author
* **Endpoint:** `GET /quotes?author=NAME`
* **Description:** Filters quotes by author name (case-insensitive partial matching).
* **Example Request:**
  ```bash
  curl "http://127.0.0.1:8000/quotes?author=steve"
  ```
* **Example Response (200 OK):**
  ```json
  [
    {
      "id": 2,
      "author": "Steve Jobs",
      "text": "The only way to do great work is to love what you do."
    }
  ]
  ```
* If no author matches the query, an empty list `[]` is returned.

---

### 6. Add a New Quote
* **Endpoint:** `POST /quotes`
* **Description:** Adds a new quote with `author` and `text`. Generates a new `id` automatically.
* **Request Header:** `Content-Type: application/json`
* **Example Request:**
  ```bash
  curl -X POST http://127.0.0.1:8000/quotes \
    -H "Content-Type: application/json" \
    -d "{\"author\": \"Maya Angelou\", \"text\": \"There is no greater agony than bearing an untold story inside you.\"}"
  ```
* **Example Response (201 Created):**
  ```json
  {
    "id": 4,
    "author": "Maya Angelou",
    "text": "There is no greater agony than bearing an untold story inside you."
  }
  ```
* **Error Example (422 Unprocessable Entity):**
  If a required field (such as `author` or `text`) is missing, FastAPI automatically returns a `422` validation error explaining the missing field.

---

## Interactive API Documentation

FastAPI automatically provides interactive Swagger documentation. Start the server and visit:

```text
http://127.0.0.1:8000/docs
```

Or alternative ReDoc documentation:

```text
http://127.0.0.1:8000/redoc
```

## Project Structure

```text
mini-quote-api/
├── main.py
├── requirements.txt
├── README.md
└── .gitignore
```

## What I Learned

* Creating a FastAPI application
* Path parameters (`/quote/{id}`) and Query parameters (`/quotes?author=NAME`)
* Handling request bodies with Pydantic (`BaseModel`)
* HTTP status codes (`200 OK`, `201 Created`, `404 Not Found`, `422 Unprocessable Entity`)
* Error handling with `HTTPException`
* Running and testing endpoints using Swagger UI and cURL
