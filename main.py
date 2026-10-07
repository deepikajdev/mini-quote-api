import random
from fastapi import FastAPI, HTTPException, status
from pydantic import BaseModel

app = FastAPI(title="Mini Quote API")


# Request schema for creating a new quote
class QuoteCreate(BaseModel):
    author: str
    text: str


# A simple in-memory list of quotes
quotes = [
    {
        "id": 1,
        "author": "Albert Einstein",
        "text": "Life is like riding a bicycle. To keep your balance, you must keep moving.",
    },
    {
        "id": 2,
        "author": "Steve Jobs",
        "text": "The only way to do great work is to love what you do.",
    },
    {
        "id": 3,
        "author": "Eleanor Roosevelt",
        "text": "The future belongs to those who believe in the beauty of their dreams.",
    },
]


@app.get("/")
def read_root():
    return {"message": "Welcome to the Mini Quote API!"}


@app.get("/quote")
def get_random_quote():
    if not quotes:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail="No quotes found"
        )
    return random.choice(quotes)


@app.get("/quote/{id}")
def get_quote_by_id(id: int):
    for quote in quotes:
        if quote["id"] == id:
            return quote
    raise HTTPException(
        status_code=status.HTTP_404_NOT_FOUND,
        detail=f"Quote with ID {id} not found",
    )


@app.get("/quotes")
def get_all_quotes(author: str | None = None):
    if author:
        filtered = [q for q in quotes if author.lower() in q["author"].lower()]
        return filtered
    return quotes


@app.post("/quotes", status_code=status.HTTP_201_CREATED)
def create_quote(quote: QuoteCreate):
    new_id = max([q["id"] for q in quotes], default=0) + 1
    new_quote = {
        "id": new_id,
        "author": quote.author,
        "text": quote.text,
    }
    quotes.append(new_quote)
    return new_quote
