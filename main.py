from fastapi import FastAPI, Form

app = FastAPI()

@app.get("/")
def read_root():
    return {"message": "Hello, world!"}

@app.post("/api/")
def get_answer(question: str = Form(...)):
    # Dummy logic: For now, it just returns "42" for any question
    return {"answer": "42"}

