import logging
import os

CLIENT_ID = os.environ['ALICE_HOME_NAME']
CLIENT_SECRET = os.environ['ALICE_CLIENT_SECRET']
USERS_DIRECTORY = "users"
TOKENS_DIRECTORY = "tokens"
DEVICES_DIRECTORY = "devices"


# Uncomment to enable logging
# LOG_FILE = "/home/pi/Desktop/logs/alice.log"
LOG_LEVEL = logging.DEBUG
LOG_FORMAT = "%(asctime)s %(message)s"
LOG_DATE_FORMAT = "%Y-%m-%d %H:%M:%S"
