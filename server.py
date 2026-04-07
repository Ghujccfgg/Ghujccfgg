from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
import random

app = FastAPI()

# 🔥 مهم عشان الموقع يقدر يتصل بالسيرفر
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/")
def home():
    return {"message": "Server is working 🚀"}

# 🧠 IP Tool
@app.get("/ip")
def get_ip():
    return {
        "ip": f"192.168.{random.randint(1,255)}.{random.randint(1,255)}",
        "country": "Unknown",
        "status": "success"
    }

# 🔍 Search Tool
@app.get("/search")
def search(q: str):
    return {
        "query": q,
        "results": [
            f"Result 1 for {q}",
            f"Result 2 for {q}",
            f"Result 3 for {q}"
        ]
    }

# 🛡 Scan Tool
@app.get("/scan")
def scan(target: str):
    return {
        "target": target,
        "ports_open": [80, 443],
        "status": "scanned"
    }
