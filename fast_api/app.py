import uvicorn
from fastapi import FastAPI
from fastapi.responses import ORJSONResponse
from api.v1 import sum


app = FastAPI(
    title="test",
    docs_url='/api/openapi',
    openapi_url='/api/openapi.json',
    default_response_class=ORJSONResponse,
)

app.include_router(sum.router, prefix="/api/v1/test", tags=["test"])

if __name__ == '__main__':
    uvicorn.run(
        'app:app',
        host='0.0.0.0',
        port=8000,
    )
