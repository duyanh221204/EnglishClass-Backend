from fastapi import FastAPI, HTTPException
from fastapi.exceptions import RequestValidationError
from starlette import status
from starlette.requests import Request
from starlette.responses import JSONResponse

from exception.exception_raising import base_error, raise_exception


def add_global_exception_handler(app: FastAPI):
    @app.exception_handler(RequestValidationError)
    async def validation_exception_handler(_: Request, exception: RequestValidationError) -> JSONResponse:
        content = base_error(str(exception.errors()))
        return raise_exception(status.HTTP_400_BAD_REQUEST, content)

    @app.exception_handler(HTTPException)
    async def http_exception_handler(_: Request, exception: HTTPException) -> JSONResponse:
        content = base_error(exception.detail)
        return raise_exception(exception.status_code, content)

    @app.exception_handler(Exception)
    async def uncategorized_exception_handler(_: Request, exception: Exception) -> JSONResponse:
        content = base_error(str(exception))
        return raise_exception(status.HTTP_500_INTERNAL_SERVER_ERROR, content)
