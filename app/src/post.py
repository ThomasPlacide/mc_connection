import json
import os
from datetime import datetime
from utils.helper import Logger
import logging

LOG_PATH = os.getenv("LOG_PATH", "logs")
STATUS_FILE = os.getenv("STATUS_FILE", "status/mcco_post_status.json")
logger = Logger.setup_logger(__name__, f"{LOG_PATH}/mcco_post.log", level=logging.DEBUG)

def process_mcco_post(received_data):

    if _is_status_file_empty():
        logger.info("Status file is empty. Initializing new structure.")
    with open(STATUS_FILE, 'r+') as f:
        status_file = json.load(f)
        logger.debug(f"Current status file content: {status_file}")
    
    logger.debug(f"Received data for processing: {received_data}")

    world_id = received_data.get('world_ID')
    if world_id not in status_file.get('worlds', {}):
        status_file['worlds'].setdefault(world_id, {"IDs_connected": {}, "last_update": ""})
        logger.info(f"Added new world ID to status file: {world_id}")
        
    for ID, username in received_data.get('IDs_connected', {}).items():
        logger.debug(f"Processing ID: {ID}, Username: {username}")
        status_file['worlds'][world_id]["IDs_connected"][ID] = username
    status_file['worlds'][world_id]["last_update"] = received_data.get('timestamp', datetime.now().isoformat())
    logger.debug(f"Initialized new world entry: {status_file['worlds'][world_id]}")

    with open(STATUS_FILE, 'w') as f:
        json.dump(status_file, f, indent=4)

def _is_status_file_empty():
    logger.debug("Checking if status file is empty.")
    with open(STATUS_FILE, 'r+') as f:
        status_file = json.load(f)
    if not bool(status_file.get('worlds', False)):
        status_file = { "worlds": {} }
        logger.debug("Resetting status file to initial empty structure.")
        with open(STATUS_FILE, 'w+') as f:
            json.dump(status_file, f, indent=4)
            logger.debug(f"Status file after reset: {status_file}")
        return True
    return False