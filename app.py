import json
from flask import (Flask,
                   jsonify,
                   request)
from utils.helper import Logger
import logging
from src.post import process_mcco_post
from src.delete import process_mcco_deletion
from src.get import process_mcco_get

__status__ = "development"

log_level = logging.DEBUG if __status__ == "development" else logging.INFO
main_logger = Logger.setup_logger(__name__, "logs/connected_app.log",
                           level=log_level)
app = Flask(__name__)
@app.route('/status', methods=['GET'])
def status():
    main_logger.info("Status endpoint was called.")
    return jsonify({"status": "connected"}), 200

@app.route('/mc_co', methods=['GET', 'POST', 'DELETE'])
def mc_co():
    """
    Endpoint to handle mc_co related requests.
    """
    if request.method == 'POST':
        main_logger.info("mc_co endpoint received POST request.")
        received_data = request.get_json()
        process_mcco_post(received_data)
        return jsonify({"message": "Data received", "data": received_data}), 200
    
    elif request.method == 'GET':
        main_logger.info("mc_co endpoint received GET request.")
        received_data = request.get_json()
        worlds_summary = process_mcco_get(received_data)
        return jsonify(worlds_summary), 200
                
    elif request.method == 'DELETE':
        main_logger.info("mc_co endpoint received DELETE request.")
        received_data = request.get_json()
        process_mcco_deletion(received_data)
        return jsonify({"message": "Status file reset"}), 200
    
def test_client():
    return app.test_client()