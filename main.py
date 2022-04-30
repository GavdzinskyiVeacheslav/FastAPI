from fastapi import FastAPI

app = FastAPI()


@app.get('/')
def home():
    return {'key' : 'Hello'}

@app.get('/{pk}')
def get_item(pk: int, q: int = None):
    return {"key": pk, 'q': q}