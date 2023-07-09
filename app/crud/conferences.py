from ..schemas import conferences as conference_schema
from ..models import conferences
from ..database import SessionLocal


def create_conference(db: SessionLocal, conference: conference_schema.Conference):
    new_conference = conferences.Conference(title=conference.title,
                                            description=conference.description,
                                            start_time=conference.start_time,
                                            end_time=conference.end_time,
                                            Capacity=conference.Capacity,
                                            items=conference.items,)
    db.add(new_conference)
    db.commit()
    db.refresh(new_conference)
    return new_conference


def get_all_conferences(db: SessionLocal):
    conference = db.query(conferences.Conference).all()
    serialized_objects = []
    for conf in conference:
        data = conference_schema.Conference(
                id=conf.id,
                title=conf.title,
                description=conf.description,
                start_time=conf.start_time,
                end_time=conf.end_time,
                Capacity=conf.Capacity,
                items=conf.items,
         )
        serialized_objects.append(conference_schema.Conference.serialize(data))

    return serialized_objects


def update_conference(db: SessionLocal, conference_id: int, conference: conference_schema.Conference):
    query = db.query(conferences.Conference).filter(conferences.Conference.id == conference_id)
    result = query.first()
    if result:
        result.title = conference.title
        result.description = conference.description
        result.start_time = conference.start_time
        result.end_time = conference.end_time
        result.Capacity = conference.Capacity
        result.items = conference.items

        db.add(result)
        db.commit()
        db.refresh(result)

    return result


def delete_conference(db: SessionLocal, conference_id: int):
    query = db.query(conferences.Conference).filter(conferences.Conference.id == conference_id)
    result = query.first()
    if result:
        db.delete(result)
        db.commit()
        db.refresh(result)
