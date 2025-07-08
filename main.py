from fastapi import FastAPI
from typing import List

app = FastAPI()

# Mock in-memory database
mock_products = [
    {"id": 1, "name": "Laptop", "price": 1200},
    {"id": 2, "name": "Mouse", "price": 25},
    {"id": 3, "name": "Keyboard", "price": 70}
]

@app.get("/products", response_model=List[dict])
def get_products():
    return mock_products
