import json
from datetime import datetime
from utils.helper import Logger
import logging
logger = Logger.setup_logger(__name__, "logs/mcco_get.log", level=logging.DEBUG)

def process_mcco_get(received_data):

    with open('status/mcco_post_status.json', 'r+') as f:
            status_file = json.load(f)
    
    if received_data:
        world_id = received_data.get('world_ID')
        if world_id and world_id in status_file.get('worlds', {}):
            connected = len(status_file['worlds'][world_id]["IDs_connected"])
            last_update = status_file['worlds'][world_id].get("last_update", datetime.now().isoformat())
            return {"connected": connected, "last_update": last_update}
    else:
        worlds_summary = dict('worlds', {"world_ID": { "connected": 0, "last_update": "" }})
        for world_id, world_data in status_file.get('worlds', {}).items():
            connected = len(world_data.get("IDs_connected", {}))
            last_update = world_data.get("last_update", "")
            worlds_summary['worlds'][world_id] = {
                "connected": connected,
                "last_update": last_update
            }
        return worlds_summary
    