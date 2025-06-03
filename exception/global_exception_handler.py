from fastapi import FastAPI, HTTPException
from fastapi.exceptions import RequestValidationError
from starlette import status
from starlette.requests import Request
from starlette.responses import JSONResponse

from exception.exception_response import raise_exception


def register_exception_handler(app: FastAPI):
    @app.exception_handler(RequestValidationError)
    async def validation_exception_handler(_: Request, exception: RequestValidationError) -> JSONResponse:
        content = raise_exception(str(exception.errors()))
        return JSONResponse(
            status_code=status.HTTP_400_BAD_REQUEST,
            content=content.model_dump()
        )

    @app.exception_handler(HTTPException)
    async def http_exception_handler(_: Request, exception: HTTPException) -> JSONResponse:
        content = raise_exception(exception.detail)
        return JSONResponse(
            status_code=exception.status_code,
            content=content.model_dump()
        )

    @app.exception_handler(Exception)
    async def unknown_exception_handler(_: Request, exception: Exception) -> JSONResponse:
        content = raise_exception(str(exception))
        return JSONResponse(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            content=content.model_dump()
        )
