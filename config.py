import logging
import os
import datetime

CLIENT_ID = os.environ['ALICE_HOME_NAME']
CLIENT_SECRET = os.environ['ALICE_CLIENT_SECRET']
USERS_DIRECTORY = "users"
TOKENS_DIRECTORY = "tokens"
DEVICES_DIRECTORY = "devices"


ENABLE_CONSOLE_LOGGING = False

LOG_FILE = f"/home/pi/Desktop/logs/alice{datetime.datetime.now()}.log"
LOG_LEVEL = logging.DEBUG
LOG_FORMAT = "%(asctime)s %(message)s"
LOG_DATE_FORMAT = "%Y-%m-%d %H:%M:%S"
