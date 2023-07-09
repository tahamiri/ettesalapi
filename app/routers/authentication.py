from fastapi import APIRouter
from fastapi.responses import JSONResponse
from fastapi import Depends, Response
from fastapi_jwt_auth import AuthJWT

from ..database import SessionLocal
from ..schemas import settings
from ..schemas import users as user_schema
from ..crud import users as user_crud


auth_router = APIRouter()


db = SessionLocal()


@AuthJWT.load_config
def get_config():
    return settings.Settings()


@auth_router.post('/users/', response_model=user_schema.User)
def create_user(user: user_schema.User):
    result = user_crud.get_user(db, user)

    if not result:
        user_crud.create_user(db, user)
    else:
        return Response(content="Invalid input", status_code=400)

    return Response(content="User registered", status_code=201)


@auth_router.post('/login/', description="Login successful", status_code=200)
def login(user: user_schema.User, Authorize: AuthJWT = Depends()):
    result = user_crud.get_user_with_password(db, user)
    if result:
        access_token = Authorize.create_access_token(subject=user.username)
        refresh_token = Authorize.create_refresh_token(subject=user.username)
        response_obj = {"access_token": access_token, "refresh_token": refresh_token}

        return JSONResponse(content=response_obj, status_code=200)
    else:
        return Response(content="Invalid username or password", status_code=401)


