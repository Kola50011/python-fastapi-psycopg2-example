import uvicorn
from fastapi import FastAPI

from model.model import *

app = FastAPI()


@app.get("/")
def read_root():
    return ImageMetadata(some_var="asd")


def start():
    uvicorn.run(app, host="0.0.0.0", port=8080)
