# Kubenertes training

Exercice: implement a service to monitor connected players in a minecraft server, using Kubernetes, front-end: TRMNL

Architecture: 
POST request to receive a new connection 
GET request for TRMNL to get the connected list every x-time
DELETE request when a user disconnects itself from a world

expected data

POST: {
    "world_ID": `world_ID`,
    "IDs_connected": {
        `user_ID`: `username`
    },
    "timestamp": `timestamp`
}

GET: {
    "world_ID": `world_ID`
} OR None, therefore you'll receive all data for all world registered

DELETE: {
    "world_ID": `world_ID`,
    "user_ID": `user_ID`,
    "timestamp": `timestamp`
}

mc_co_status.json: 
{
    "worlds": {
        "ex_ID": {
            "IDs_connected": {
                "player1_ID": "player1_name",
                "player2_ID": "player2_name"
            },
            "last_updated": "2024-06-15T12:34:56Z"
        }
    }
}