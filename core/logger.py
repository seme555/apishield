import os
import logging
import sys

logger = logging.getLogger()

formatter = logging.Formatter(
    fmt="%(asctime)s - %(levelname)s - %(message)s"
)

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
LOG_FILENAME_INFO = BASE_DIR + "/core/logs/app.log"
os.makedirs(os.path.join(BASE_DIR, 'core/logs'), exist_ok=True)

# Check if the log file exists, and create it if it doesn't
if not os.path.isfile(LOG_FILENAME_INFO):
    with open(LOG_FILENAME_INFO, 'w') as log_file:
        log_file.write("Log file created\n")
