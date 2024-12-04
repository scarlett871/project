import logging_config
import logging

logging.basicConfig(filename='inventory_system.log', level=logging.INFO,
                    format='%(asctime)s - %(levelname)s - %(message)s')

def log_action(action):
    logging.info(action)
