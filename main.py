import random
from fastapi import FastAPI

app = FastAPI()

# A simple in-memory list of quotes
quotes = [
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

@app.get("/")
def read_root():
    return {"message": "Welcome to the Mini Quote API!"}

@app.get("/quote")
def get_quote():
    return random.choice(quotes)

@app.get("/quotes")
def get_all_quotes():
    return quotes
