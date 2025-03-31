from fastapi import FastAPI, Form

app = FastAPI()

@app.get("/")
def read_root():
    return {"message": "Hello, world!"}

from fastapi import FastAPI, Form
import openai
import os

app = FastAPI()

openai.api_key = os.getenv("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")

@app.post("/api/")
async def solve_question(question: str = Form(...)):
    response = openai.ChatCompletion.create(
        model="gpt-4",
        messages=[
            {"role": "system", "content": "You are an expert in IITM Data Science assignments. Answer concisely and accurately."},
            {"role": "user", "content": question}
        ]
    )

    answer = response["choices"][0]["message"]["content"]
    return {"answer": answer}
