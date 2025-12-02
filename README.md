# Kubenertes training

Exercice: implement a service to monitor connected players in a minecraft server, using Kubernetes, front-end: TRMNL

Architecture: 
POST request to receive a new connection 
GET request for TRMNL to get the connected list every x-time

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