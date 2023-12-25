from logger.dataspark_logger import DataSparkLogger
from utils.utils import predict_data_via_api
import subprocess
import time
import sys
import os

# Get the current directory (where your script is located)
current_dir = os.path.dirname(os.path.abspath(__file__))
# Add the parent directory to the system path
parent_dir = os.path.abspath(os.path.join(current_dir, ".."))
sys.path.append(parent_dir)

from config.config import Config


if __name__ == "__main__":
    
    activity_logger = DataSparkLogger()
    app_config = Config()
    
    activity_logger.logger.info("Automatization is starting.....")
    data = {"feature_1":1,"feature_2":2,"feature_3":3,"feature_4":4}
    api_prediction = predict_data_via_api(data=[list(data.values())])
    activity_logger.logger.info(f"ML API predicted the input {[list(data.values())]} as : {api_prediction}")

    ######### Streamlit GUI Serving #########

    # Define the command to run your Streamlit app
    gui_path = app_config.config.get("gui_path")
    streamlit_command = f"streamlit run {gui_path} --server.port=8501 --server.address=0.0.0.0"
    # Start the Streamlit app in the background
    streamlit_process = subprocess.Popen(streamlit_command, shell=True)

    ######### Backend API Serving #########

    deployment_directory = app_config.config.get("serving_script_path")
    # Change the current working directory to the specified directory
    os.chdir(deployment_directory)
    # Define the API serve command for the backend_data_serving.py file
    bentoml_command = "uvicorn backend_data_serving:app --reload"

    activity_logger.logger.info("Streamlit should be up and running.....")
    # Start the API in the background
    bentoml_process = subprocess.Popen(bentoml_command, shell=True)

    activity_logger.logger.info("FastAPI should be up and running.....")
    activity_logger.logger.info("Streamlit and FastAPI are both up and running.")

    try:
        # Monitor the processes and keep the script running
        streamlit_process.wait()
        bentoml_process.wait()
    except KeyboardInterrupt:
        # Terminate the processes when you press Ctrl+C
        streamlit_process.terminate()
        bentoml_process.terminate()
