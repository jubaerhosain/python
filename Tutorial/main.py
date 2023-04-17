from fastapi import FastAPI

# Create a new FastAPI instance
app = FastAPI()


# Define a root endpoint for the app
@app.get("/")
def read_root():
    return {"Hello": "World"}


# Define a custom endpoint for the app
@app.get("/items/{item_id}")
def read_item(item_id: int, q: str = None):
    return {"item_id": item_id, "q": q}
