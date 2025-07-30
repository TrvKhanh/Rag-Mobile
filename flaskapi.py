from generation.core import model
from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

model = model()

class MessageInput(BaseModel):
    message: str

@app.post("/chat")
def chat(input: MessageInput):
    return model.invoke(input.message)
