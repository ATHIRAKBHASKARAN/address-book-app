from fastapi import FastAPI
from app.core.database import Base, engine
from app.api.v1.address import router
from app.core.config import settings

Base.metadata.create_all(bind=engine)

app = FastAPI(title="Address Book API", debug=settings.DEBUG)

app.include_router(router, prefix=settings.API_V1_PREFIX + "/addresses", tags=["Addresses"])