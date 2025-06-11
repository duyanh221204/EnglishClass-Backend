from starlette import status
from starlette.responses import JSONResponse

from dto.response.base_response import BaseResponse


def base_error(message: str) -> BaseResponse:
    return BaseResponse(
        status="error",
        message=message
    )


def raise_exception(status_code: status, content: BaseResponse) -> JSONResponse:
    return JSONResponse(
        status_code=status_code,
        content=content.model_dump()
    )
