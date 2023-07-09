from fastapi import APIRouter
from fastapi import Depends, HTTPException, Response
from fastapi_jwt_auth import AuthJWT

from ..database import SessionLocal
from ..schemas import conferences as conference_schema
from ..crud import conferences as conference_crud


api_router = APIRouter()
db = SessionLocal()


@api_router.post('/conferences/')
def create_conference(conference: conference_schema.Conference, Authorize: AuthJWT = Depends()):
    try:
        Authorize.jwt_required()
    except Exception:
        raise HTTPException(status_code=401, detail="Unauthorized")

    conference_crud.create_conference(db, conference)

    return Response(content="Conference created", status_code=201)


@api_router.get('/conferences/', description="Successful operation", status_code=200)
def get_all_conferences(Authorize: AuthJWT = Depends()):
    try:
        Authorize.jwt_required()
    except Exception:
        return Response(content="Unauthorized", status_code=401)

    serialized_objects = conference_crud.get_all_conferences(db)

    return serialized_objects


@api_router.put('/conferences/{conference_id}')
def update_an_existing_conference(conference: conference_schema.Conference, conference_id: int, Authorize: AuthJWT = Depends()):
    try:
        Authorize.jwt_required()
    except Exception as e:
        raise HTTPException(status_code=401, detail="Unauthorized")

    result = conference_crud.update_conference(db, conference_id, conference)
    if result:
        return Response(content="Conference updated", status_code=200)
    else:
        return Response(content="Conference not found", status_code=404)


@api_router.delete('/conferences/{conference_id}', status_code=204)
def delete_an_existing_conference(conference_id: int, Authorize: AuthJWT = Depends()):
    try:
        Authorize.jwt_required()
    except Exception:
        raise HTTPException(status_code=401, detail="Unauthorized")

    result = conference_crud.delete_conference(db, conference_id)
    if result:
        return Response(content="Conference deleted", status_code=204)
    else:
        return Response(content="Conference not found", status_code=404)
