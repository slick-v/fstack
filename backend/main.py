from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware




app = FastAPI()



# Allowing react frontend to call backend

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],

)

@app.get("/")
def hello():
    return {"message": "Hello from Fastapi backend!"}