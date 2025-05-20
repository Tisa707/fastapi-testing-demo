# main.py
from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def read_root():
    return {"message": "App is running"}

@app.get("/add")
def add_numbers(a: int, b: int):
    return {"result": a + b}

