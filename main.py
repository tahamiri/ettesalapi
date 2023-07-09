from fastapi import FastAPI , Response
from fastapi.exceptions import RequestValidationError

from app.routers.authentication import auth_router
from app.routers.api import api_router

from app.database import engine
from app import database


database.Base.metadata.create_all(bind=engine)


app = FastAPI()
app.include_router(auth_router, prefix="/authentication")
app.include_router(api_router, prefix="/api")


@app.exception_handler(RequestValidationError)
async def validation_exception_handler(request, exc):
    return Response(content="Invalid input", status_code=400)


if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
