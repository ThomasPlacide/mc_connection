import json
from utils.helper import Logger
import logging
from datetime import datetime
logger = Logger.setup_logger(__name__, "logs/mcco_delete.log", level=logging.DEBUG)

def process_mcco_deletion(received_data):
    """
    Remove user id when user disconnects itself. 
    """

    world_id = received_data.get("world_ID")
    user_id = received_data.get("user_ID")
    logger.debug(f"Processing deletion for world_id: {world_id}, user_id: {user_id}")
    with open('status/mcco_post_status.json', 'r') as f:
        status_file = json.load(f)

    if world_id in status_file.get("worlds", {}):
        if user_id in status_file['worlds'][world_id]["IDs_connected"]:
            logger.debug(f"Removing user_id: {user_id} from world_id: {world_id}")
            status_file['worlds'][world_id]["IDs_connected"].pop(user_id)
            status_file['worlds'][world_id]["last_update"] = received_data.get("timestamp", datetime.now().isoformat())
            with open('status/mcco_post_status.json', 'w') as f:
                json.dump(status_file, f, indent=4)

