from fastapi import status
from fastapi.responses import JSONResponse


def not_implemented(detail: str) -> JSONResponse:
    return JSONResponse(
        status_code=status.HTTP_501_NOT_IMPLEMENTED,
        content={"status": "not_implemented", "detail": detail},
    )
