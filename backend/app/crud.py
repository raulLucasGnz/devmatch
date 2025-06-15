from sqlalchemy.orm import Session
from . import models, schemas

#Inserta un nuevo user en la BDD
def create_user(db: Session, user: schemas.UserCreate):
    db_user = models.User(
        username=user.username,
        email=user.username,
        full_name=user.full_name
    )
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user