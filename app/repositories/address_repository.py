from sqlalchemy.orm import Session
from app.models.address import Address


def create(db: Session, address):
    db_address = Address(**address.dict())
    db.add(db_address)
    db.commit()
    db.refresh(db_address)
    return db_address


def get_all(db: Session):
    return db.query(Address).all()


def get_by_id(db: Session, address_id: int):
    return db.query(Address).filter(Address.id == address_id).first()


def update(db: Session, db_address, update_data):
    for key, value in update_data.dict().items():
        setattr(db_address, key, value)
    db.commit()
    db.refresh(db_address)
    return db_address


def delete(db: Session, db_address):
    db.delete(db_address)
    db.commit()