from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def home():
    return {"message": "Server is working"}

@app.get("/tools/ip")
def get_ip():
    return {"ip": "127.0.0.1"}
