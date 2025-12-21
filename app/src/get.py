import json
import os
from datetime import datetime
from utils.helper import Logger
import logging

LOG_PATH = os.getenv("LOG_PATH", "logs")
STATUS_FILE = os.getenv("STATUS_FILE", "status/mcco_post_status.json")
logger = Logger.setup_logger(__name__, f"{LOG_PATH}/mcco_get.log", level=logging.DEBUG)

def process_mcco_get():

    with open(STATUS_FILE, 'r+') as f:
            status_file = json.load(f)
    
    worlds_summary = {'worlds': {"world_ID": { "connected": 0, "last_update": "" }}}
    for world_id, world_data in status_file.get('worlds', {}).items():
        connected = len(world_data.get("IDs_connected", {}))
        last_update = world_data.get("last_update", "")
        worlds_summary['worlds'][world_id] = {
            "connected": connected,
            "last_update": last_update
        }
    return worlds_summary
    