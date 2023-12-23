import uvicorn
from fastapi import FastAPI
from controller.summarization_controller import summarization_controller

app = FastAPI()

@app.get("/up")
def check_up():
    return 'up and running'

@app.get("/summarization")
def summarization(request: str, lang: str):
    return summarization_controller(request, lang)

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=5000)