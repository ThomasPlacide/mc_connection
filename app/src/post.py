import json
import os
from datetime import datetime
from utils.helper import Logger
import logging

LOG_PATH = os.getenv("LOG_PATH", "logs")
STATUS_FILE = os.getenv("STATUS_FILE", "status/mcco_post_status.json")
logger = Logger.setup_logger(__name__, f"{LOG_PATH}/mcco_post.log", level=logging.DEBUG)

def process_mcco_post(received_data):

    try:
        with open(STATUS_FILE, 'r') as f:
            content = f.read()
            status_file = json.loads(content) if content.strip() else {"worlds": {}}
    except FileNotFoundError:
        os.makedirs(os.path.dirname(STATUS_FILE), exist_ok=True)
        status_file = {"worlds": {}}
        logger.info("Status file not found. Initialized new structure.")
    
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
