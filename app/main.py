from fastapi import FastAPI
from pydantic import BaseModel

from testimonial_agent import process_testimonial

app = FastAPI()


class Testimonial(BaseModel):
    name: str
    role: str
    company: str
    linkedin: str
    testimonial: str


@app.get("/")
def health():
    return {"status": "AI Testimonial Agent running"}


@app.post("/submit")
def submit(testimonial: Testimonial):

    result = process_testimonial(
        testimonial.dict()
    )

    return {
        "message": "Testimonial received",
        "result": result
    }
