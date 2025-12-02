import json
from datetime import datetime
def process_mcco_post(received_data):

    with open('status/mcco_post_status.json', 'r') as f:
        status_file = json.load(f)
    
    world_id = received_data.get('world_ID')
    if world_id not in status_file.get('worlds', {}):
        for ID, username in received_data.get('IDs_connected', {}).items():
            status_file['worlds'][world_id]["IDs_connected"].append({
                "ID": ID,
                "username": username
            })
        status_file[world_id]["last_update"] = received_data.get('timestamp', datetime.now().isoformat())

    with open('status/mcco_post_status.json', 'w') as f:
        json.dump(status_file, f, indent=4)

    

        