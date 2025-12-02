import json

def process_mcco_deletion(received_data):
    """
    Remove user id when user disconnects itself. 
    """

    world_id = received_data.get("world_id")
    user_id = received_data.get("user_id")
    with open('status/mcco_status.json', 'r') as f:
        status_file = json.load(f)

    if world_id in status_file:
        if user_id in status_file[world_id]["IDs_connected"]:
            status_file[world_id]["IDs_connected"].remove(user_id)
            with open('status/mcco_status.json', 'w') as f:
                json.dump(status_file, f, indent=4)

