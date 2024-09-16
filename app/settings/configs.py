import os
from dotenv import load_dotenv

load_dotenv("./.env")

# API
API_VERSION = os.environ["API_VERSION"]
API_PATH = os.environ["API_PATH"]
API_DOC = os.environ["API_DOC"]
SERVER_ROLE = os.environ["SERVER_ROLE"]
SECRET_KEY = os.environ["SECRET_KEY"]
HOST = os.environ["HOST"]

########### ACCESS_USER ###########

DEVUSER = os.environ["DEVUSER"]
DEVUSER_PASSWORD = os.environ["DEVUSER_PASSWORD"]
JWT_TOKEN = os.environ["JWT_TOKEN"]

ACCESSTOKEN_FILE_PATH = os.environ["ACCESSTOKEN_FILE_PATH"]

