from ..schemas import users as user_schema
from ..models import users
from ..database import SessionLocal


def get_user(db: SessionLocal, user: user_schema.User):
    query = db.query(users.User).filter(users.User.username == user.username)
    result = query.first()
    return result


def get_user_with_password(db: SessionLocal, user: user_schema.User):
    query = db.query(users.User).filter(users.User.username == user.username, users.User.password == user.password)
    result = query.first()
    return result


def create_user(db: SessionLocal, user: user_schema.User):
    db_user = users.User(username=user.username, password=user.password)
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user
