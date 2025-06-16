from fastapi import FastAPI
from starlette.middleware.cors import CORSMiddleware

from configuration.app_init import lifespan
from exception.global_exception_handler import add_global_exception_handler

app = FastAPI(lifespan=lifespan)

add_global_exception_handler(app)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)
