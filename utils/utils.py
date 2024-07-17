import pandas as pd
import requests
import os
import sys

# Get the current directory (where your script is located)
current_dir = os.path.dirname(os.path.abspath(__file__))
# Add the parent directory to the system path
parent_dir = os.path.abspath(os.path.join(current_dir, ".."))
sys.path.append(parent_dir)

from config.config import Config
from logger.dataspark_logger import DataSparkLogger

def predict_data_via_api(data: str) -> dict:
    """
    Send a POST request to the AI model server and get predictions.

    Args:
        data (str): Feature values to be predicted.

    Returns:
        dict: AI model prediction as a dictionary.
    """
   
    #Read Configuration file
    app_config = Config("config/config.yml")

    #Activate Logging Module
    activity_logger = DataSparkLogger(log_file_path="logs/log_file.log" , config_file="config/config.yml")

    # Define the API endpoint
    api_url = app_config.config.get("api_url")

    # Define the headers for the POST request
    headers = {"content-type": "application/json"}
    
    try:
        # Make the POST request to the model
        activity_logger.logger.debug(f"The type of the given data to predict is: {type(data)}")
        activity_logger.logger.debug(f"Data given data to predict is: {data}")
        response = requests.post(api_url, headers=headers, data=data)
        activity_logger.logger.debug(f"Type response type of the return is: {type(response)}")
        # Check if the request was successful
        if response.status_code == 200:
            prediction = response.json()  # Assuming the response is in JSON format
            
            activity_logger.logger.debug(f"The status code is: {response.status_code}")
            activity_logger.logger.debug(f"Type of the return is: {type(prediction)}")
            activity_logger.logger.debug(f"Return is: {prediction}")
            return prediction
        else:
            activity_logger.logger.error(f"Error: Failed to get a valid response. Status code: {response.status_code}")
            return None
    except Exception as e:
        activity_logger.logger.error(f"Exception occurred in model prediction: {str(e)}")
        return None

def get_data_for_gui(data_name: str, use_api=False) -> dict:
    #Logging functionality as well as configruration management is removed for resolving a bug.
    """
    Retrieve data from FastAPI using a GET request.

    Args:
        data_name (str): The name of the data to be requested.

    Returns:
        dict or None: A dictionary representing the requested data in CSV format.
                     Returns None if the request fails or encounters an exception.
    """

    #Read Configuration file
    #app_config = Config(r"C:\Users\Catorsem\Desktop\DI502Repo\dataspark\config\config.yml")

    #Activate Logging Module
    #activity_logger = DataSparkLogger(log_file_path=r"C:\Users\Catorsem\Desktop\DI502Repo\dataspark\logs\log_file.log" , config_file=r"C:\Users\Catorsem\Desktop\DI502Repo\dataspark\config\config.yml")
    
    #Read Configuration file
    app_config = Config()

    if use_api:
        try:
            # Make the GET request to the model

            # Define the API endpoint
            api_url = "http://127.0.0.1:8000" #app_config.config.get("api_url")

            prepared_url = api_url + "/get_analysed_dataset_outputs/" + data_name

            #activity_logger.logger.debug(f"Prepared API request url: {prepared_url}")

            response = requests.get(prepared_url)

            #activity_logger.logger.debug(f"FastAPI response received.")
            
            # Check if the request was successful
            if response.status_code == 200:
                prediction = response.json()  # Assuming the response is in JSON format            
                #activity_logger.logger.debug(f"The status code is: {response.status_code}")
                #activity_logger.logger.debug(f"Type of the return is: {type(prediction)}")
                #activity_logger.logger.debug(f"Return is: {prediction}")
                return pd.DataFrame(prediction)
            else:
                #activity_logger.logger.error(f"Error: Failed to get a valid response. Status code: {response.status_code}")
                return None
        except Exception as e:
            #activity_logger.logger.error(f"Exception occurred in model prediction: {str(e)}")
            return None
    else:
        try:
                    
            input_to_dataset_mapper = {
                #"model_performance_related_data":app_config.config.get("model_performance_related_data"),
                #"xgboost_model_path":app_config.config.get("xgboost_model_path"),
                #"dataset_description":app_config.config.get("dataset_description"),
                
                "adversity_home_predictions":app_config.config.get("adversity_home_predictions"),
                "affluent_home_predictions":app_config.config.get("affluent_home_predictions"),
                "all_home_predictions":app_config.config.get("all_home_predictions"),
                "comfortable_home_predictions":app_config.config.get("comfortable_home_predictions"),
                "daily_average":app_config.config.get("daily_average"),
                "daily_average_with_holiday":app_config.config.get("daily_average_with_holiday"),
                "daily_high":app_config.config.get("daily_high"),
                "daily_high_with_holiday":app_config.config.get("daily_high_with_holiday"),
                "daily_low":app_config.config.get("daily_low"),
                "daily_low_with_holiday":app_config.config.get("daily_low_with_holiday"),
                "daily_total":app_config.config.get("daily_total"),
                "daily_total_with_holiday":app_config.config.get("daily_total_with_holiday"),
                "data_describe":app_config.config.get("data_describe"),
                "data_describe_all":app_config.config.get("data_describe_all"),
                "monthly_average":app_config.config.get("monthly_average"),
                "monthly_high":app_config.config.get("monthly_high"),
                "monthly_low":app_config.config.get("monthly_low"),
                "monthly_total":app_config.config.get("monthly_total"),
                "uk_bank_holidays":app_config.config.get("uk_bank_holidays"),
                "performance_metrics":app_config.config.get("performance_metrics")
            }

            df = pd.read_csv(input_to_dataset_mapper[data_name])

            return df

        except Exception as e:
            #activity_logger.logger.error(f"Exception occurred in data acquisition: {str(e)}")
            return None


   
    
if __name__ == "__main__":
    #Test Code
    print(get_data_for_gui(data_name="data_describe_all"))