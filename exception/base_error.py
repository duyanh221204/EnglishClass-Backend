from dto.response.base_response import BaseResponse


def base_error(message: str) -> BaseResponse:
    return BaseResponse(
        status="error",
        message=message
    )
