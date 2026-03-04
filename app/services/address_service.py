from typing import List
from sqlalchemy.orm import Session
from geopy.distance import geodesic
from app.models.address import Address
from app.repositories import address_repository

from app.core.logging import get_logger

logger = get_logger(__name__)


def create_address(db: Session, address):
    logger.info("Creating new address")
    return address_repository.create(db, address)


def get_addresses_within_distance(
    db: Session,
    lat: float,
    lon: float,
    distance_km: float
) -> List[Address]:

    logger.info(
        "Searching addresses within %.2f km of (%f, %f)",
        distance_km,
        lat,
        lon
    )

    origin = (lat, lon)
    addresses = address_repository.get_all(db)

    results: List[Address] = []

    for addr in addresses:
        target = (addr.latitude, addr.longitude)
        distance = geodesic(origin, target).km

        if distance <= distance_km:
            results.append(addr)

    logger.info("Found %d matching addresses", len(results))

    return results