from fastapi import FastAPI
from starlette.middleware.cors import CORSMiddleware

from exception.global_exception_handler import register_global_exception_handler

app = FastAPI()

register_global_exception_handler(app)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)
