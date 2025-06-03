from dto.response.base_response import BaseResponse


def raise_exception(message: str) -> BaseResponse:
    return BaseResponse(
        status="error",
        message=message
    )
