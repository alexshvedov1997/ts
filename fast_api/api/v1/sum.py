from fastapi import APIRouter, status, HTTPException, Query
from schemas.sum_schema import ResultModel, ErrorModel
import asyncio
import random


router = APIRouter()


@router.get(
    "/calculate",
    response_model=ResultModel,
    responses={status.HTTP_400_BAD_REQUEST: {"model": ErrorModel}}
)
async def calculate(x: int = Query(..., description="x must be an integer"),
                    y: int = Query(..., description="y must be an integer")):
    await asyncio.sleep(random.uniform(0, 3))
    try:
        if y == 0:
            raise ValueError("Division by zero is not allowed.")
        random_factor = random.uniform(-10, 10)
        result = (x / y) * random_factor
        return {
            "x": x,
            "y": y,
            "result": result
        }
    except Exception as e:
        raise HTTPException(
            status_code=400,
            detail={
                "Error": type(e).__name__,
                "ErrorMessage": str(e),
                "RequestData": f"x = {x}; y = {y}"
            }
        )
