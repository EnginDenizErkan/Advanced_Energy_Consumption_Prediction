import logging
from logging.handlers import TimedRotatingFileHandler
import yaml
import sys
import os

# Get the current directory (where your script is located)
current_dir = os.path.dirname(os.path.abspath(__file__))
# Add the parent directory to the system path
parent_dir = os.path.abspath(os.path.join(current_dir, ".."))
sys.path.append(parent_dir)

from config.config import Config

class DataSparkLogger:
    def __init__(self, log_file_path="logs/log_file.log" , config_file="config/config.yml"):
        # Load logging configuration from the YAML file
        
        #Reading Config
        app_config = Config(config_file=config_file)
        # Default to DEBUG if not specified in the config
        conf_log_level = app_config.config.get("log_level",   "DEBUG")
        conf_log_path = app_config.config.get("log_path")
        conf_logger_name = app_config.config.get("logger_name")

        log_file_path = conf_log_path

        self.logger = logging.getLogger(conf_logger_name)
        self.logger.setLevel(conf_log_level)

        formatter = logging.Formatter('Timestamp [%(asctime)s] - Logger Name [%(name)s] - Logging Level [%(levelname)s] - Log Origin [%(filename)s:%(funcName)s:%(lineno)d] - Log Message [%(message)s]')     

        handler = TimedRotatingFileHandler(conf_log_path, when="midnight", interval=1, backupCount=5)
        handler.setFormatter(formatter)
        self.logger.addHandler(handler)


if __name__ == "__main__":
    activity_logger = DataSparkLogger()
    activity_logger.logger.info("Testing No 55")