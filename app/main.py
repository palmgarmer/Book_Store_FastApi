from app.settings.configs import API_VERSION, API_PATH, API_DOC
from app.endpoint import api_router

from fastapi import FastAPI
from starlette.middleware.cors import CORSMiddleware

from datetime import datetime
from loguru import logger
import os

stamp_today = datetime.now()
today = stamp_today.strftime("%Y%m%d")
path_log = os.path.abspath("app/log/{}.log".format(today))
logger.add(path_log, encoding='utf-8', diagnose=True, rotation="00:00", retention="180 days")
logger.debug(path_log)

app = FastAPI(
    title="BOOK STORE API",
    description="BOOK STORE API",
    version=API_VERSION,
    docs_url=API_DOC,
    redoc_url=None,
    openapi_url=f"{API_DOC}/openapi.json"
)

# Set all CORS enabled origins
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(api_router, prefix=API_PATH)