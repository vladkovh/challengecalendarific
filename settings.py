import os

import dotenv


dotenv.load_dotenv()

CALENDAR_API_KEY = os.getenv('CALENDAR_API_KEY')
BASE_CALENDAR_API_URL = os.getenv('BASE_CALENDAR_API_URL')
HOLIDAYS_SUBDIR=os.getenv('HOLIDAYS_SUBDIR')
