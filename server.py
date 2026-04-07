from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def home():
    return {"message": "Server is working"}

@app.post("/scan")
def scan(data: dict):
    target = data.get("target")
    return {
        "status": "success",
        "target": target,
        "result": "Fake scan result for now"
    }
