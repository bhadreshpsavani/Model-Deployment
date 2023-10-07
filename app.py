# app.py
from fastapi import FastAPI, APIRouter
import uvicorn
import logging
from transformers import pipeline


logging.basicConfig(level = logging.INFO)

pipe = pipeline("text-classification", model="distilbert-base-uncased-emotion")
router = APIRouter()
app = FastAPI()

@router.get("/")
async def home():
  return {"message": "Machine Learning service"}

@router.post("/sentiment")
async def data(data: dict):
  try:
    input_text = data["text"]
    res = pipe(input_text)
    return res
  except Exception as e:
    logging.error("Something went wrong")

app.include_router(router)

if __name__ == "__main__":
  uvicorn.run("app:app", reload=True, port=6000, host="0.0.0.0")