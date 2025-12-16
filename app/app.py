from flask import (Flask,
                   jsonify,
                   request)
import os
from dotenv import load_dotenv
from utils.helper import Logger
import logging
load_dotenv('cfg/.env')

__status__ = os.getenv("APP_ENV", "development")
LOG_PATH = os.getenv("LOG_PATH", "/app/logs")
PORT = int(os.getenv("PORT", 5000))
LOG_LEVEL = os.getenv("LOG_LEVEL", "info").upper()
log_level = getattr(logging, LOG_LEVEL, logging.INFO)

main_logger = Logger.setup_logger(__name__, f"{LOG_PATH}/connected_app.log",
                           level=log_level)

main_logger.info("="*50)
main_logger.info(f"Application starting in {__status__} mode.")
main_logger.info(f"Current working directory: {os.getcwd()}")
main_logger.info("="*50)

app = Flask(__name__)
@app.route('/status', methods=['GET'])
def status():
    main_logger.info("Status endpoint was called.")
    return jsonify({"status": "connected"}), 200

@app.route('/mcco', methods=['GET', 'POST', 'DELETE'])
def mcco():
    """
    Endpoint to handle mcco related requests.
    """
    try:
        from src.post import process_mcco_post
        from src.delete import process_mcco_deletion
        from src.get import process_mcco_get
    except ImportError as e:
        main_logger.error(f"Error importing modules: {e}")
        return jsonify({"error": "Internal server error"}), 500

    if request.method == 'POST':
        main_logger.info("mcco endpoint received POST request.")
        received_data = request.get_json()
        process_mcco_post(received_data)
        return jsonify({"message": "Data received", "data": received_data}), 200
    
    elif request.method == 'GET':
        main_logger.info("mcco endpoint received GET request.")
        received_data = request.get_json()
        worlds_summary = process_mcco_get(received_data)
        return jsonify(worlds_summary), 200
                
    elif request.method == 'DELETE':
        main_logger.info("mcco endpoint received DELETE request.")
        received_data = request.get_json()
        process_mcco_deletion(received_data)
        return jsonify({"message": "Status file reset"}), 200
    
def test_client():
    return app.test_client()

if __name__ == '__main__':
    main_logger.info(f"Starting Flask app in {__status__} mode.")
    app.run(host='0.0.0.0', port=PORT, debug=True if __status__ == "development" else False)