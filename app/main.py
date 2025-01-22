from fastapi import FastAPI
from app.api.v1.endpoints import staffs
from app.db.base import Base
from app.db.session import engine
# create all tables
Base.metadata.create_all(bind=engine)


app = FastAPI(
    title="parking Application",
    description="API for Parking Application",
    version="1.0.0",   
)

# include routers

app.include_router(staffs.router,)
