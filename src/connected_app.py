import json
from flask import (Flask,
                   jsonify,
                   request)
from utils.helper import setup_logger
import logging
__status__ = "development"

log_level = logging.DEBUG if __status__ == "development" else logging.INFO
main_logger = setup_logger(__name__, "log/connected_app.log",
                           level=log_level)
app = Flask(__name__)
@app.route('/status', methods=['GET'])
def status():
    main_logger.info("Status endpoint was called.")
    return jsonify({"status": "connected"}), 200

@app.route('/mc_co', methods=['GET', 'POST'])
def mc_co():
    """
    Endpoint to handle mc_co related requests.
    """
    if request.method == 'POST':
        main_logger.info("mc_co endpoint received POST request.")
        received_data = request.get_json()

        main_logger.debug(f"Received data: {received_data}")
        return jsonify({"message": "Data received", "data": received_data}), 200
    
    elif request.method == 'GET':
        main_logger.info("mc_co endpoint received GET request.")
        return jsonify({"message": "mc_co GET endpoint"}), 200