from pydantic import BaseModel


class ResultModel(BaseModel):
    x: int
    y: int
    result: float


class ErrorModel(BaseModel):
    Error: str
    ErrorMessage: str
    RequestData: str
