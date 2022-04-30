from fastapi import FastAPI, Query
from schemas import Book
from typing import List

app = FastAPI()


# @app.get('/')
# def home():
#     return {'key' : 'Hello'}

# @app.get('/{pk}')
# def get_item(pk: int, q: int = None):
#     return {"key": pk, 'q': q}

# @app.get('/user/{pk}/items/{item}/')
# def get_user_item(pk: int, item: str):
#     return {'user': pk, 'item': item}


@app.post('/book')
def create_book(item: Book):
	return item


@app.get('/book')
def get_book(q: List[str] = Query(["test", "test2"], description="Search book", deprecated=True)):
	return q
