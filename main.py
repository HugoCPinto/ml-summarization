from fastapi import FastAPI

app = FastAPI()

@app.get("/up")
def check_up():
    return 'up and running'
