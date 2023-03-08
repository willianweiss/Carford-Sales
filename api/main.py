from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from api.cars.routes import router as car_router
from api.owners.routes import router as owner_router
from api.users.routes import router as user_router
from api.settings import settings

app = FastAPI(
    title=settings.APP_NAME,
    version=settings.APP_VERSION,
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=settings.ALLOWED_HOSTS,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(car_router)
app.include_router(owner_router)
app.include_router(user_router)
