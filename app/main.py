from fastapi import FastAPI
from testimonial_agent import process_testimonial

app = FastAPI()


@app.post("/submit")
def submit_testimonial(data: dict):

    result = process_testimonial(data)

    return result
