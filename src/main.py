from fastapi import FastAPI

from routes import movie_router

from fastapi.exceptions import RequestValidationError
from fastapi.responses import JSONResponse


app = FastAPI(
    title="Movies homework",
    description="Description of project"
)

api_version_prefix = "/api/v1"

app.include_router(movie_router, prefix=f"{api_version_prefix}/theater", tags=["theater"])


@app.exception_handler(RequestValidationError)
async def validation_exception_handler(request, exc):
    return JSONResponse(
        status_code=400,
        content={"detail": "Invalid input data."},
    )
