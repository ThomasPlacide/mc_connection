import json
import os
from utils.helper import Logger
import logging
from datetime import datetime

LOG_PATH = os.getenv("LOG_PATH", "logs")
STATUS_FILE = os.getenv("STATUS_FILE", "status/mcco_post_status.json")
logger = Logger.setup_logger(__name__, f"{LOG_PATH}/mcco_delete.log", level=logging.DEBUG)

def process_mcco_deletion(received_data):
    """
    Remove user id when user disconnects itself. 
    """

    world_id = received_data.get("world_ID")
    user_id = received_data.get("user_ID")
    logger.debug(f"Processing deletion for world_id: {world_id}, user_id: {user_id}")
    with open(STATUS_FILE, 'r') as f:
        status_file = json.load(f)

    if world_id in status_file.get("worlds", {}):
        if user_id in status_file['worlds'][world_id]["IDs_connected"]:
            logger.debug(f"Removing user_id: {user_id} from world_id: {world_id}")
            status_file['worlds'][world_id]["IDs_connected"].pop(user_id)
            status_file['worlds'][world_id]["last_update"] = received_data.get("timestamp", datetime.now().isoformat())
            with open(STATUS_FILE, 'w') as f:
                json.dump(status_file, f, indent=4)

