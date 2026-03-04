from sqlalchemy.orm import Session
from app.repositories import address_repository
from app.utils.distance import calculate_distance
from app.core.logging import logger


def create_address(db: Session, address):
    logger.info("Creating new address")
    return address_repository.create(db, address)


def get_addresses_within_distance(db: Session, lat, lon, distance_km):
    addresses = address_repository.get_all(db)
    result = []

    for addr in addresses:
        dist = calculate_distance(lat, lon, addr.latitude, addr.longitude)
        if dist <= distance_km:
            result.append(addr)

    return result