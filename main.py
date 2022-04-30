from fastapi import FastAPI
from schemas import Book

app = FastAPI()


@app.get('/')
def home():
    return {'key' : 'Hello'}

@app.get('/{pk}')
def get_item(pk: int, q: int = None):
    return {"key": pk, 'q': q}

@app.get('/user/{pk}/items/{item}/')
def get_user_item(pk: int, item: str):
    return {'user': pk, 'item': item}


@app.post('/book')
def create_book(item: Book):
	pass

