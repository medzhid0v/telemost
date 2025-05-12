from pathlib import Path
import os

from dotenv import load_dotenv

load_dotenv(Path(__file__).resolve().parent.parent / '.env.local')

# base conf
BASE_URL = 'https://cloud-api.yandex.net/v1/telemost-api/'

# env
CLIENT_ID = os.getenv('CLIENT_ID')
CLIENT_SECRET = os.getenv('CLIENT_SECRET')
OAUTH_TOKEN = os.getenv('OAUTH_TOKEN')
