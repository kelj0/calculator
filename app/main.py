from fastapi import FastAPI
from .routers import calculator
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

app.include_router(calculator.router)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"]
)