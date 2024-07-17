from typing import Union
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
import pandas as pd
import sys
import os

# Get the current directory (where your script is located)
current_dir = os.path.dirname(os.path.abspath(__file__))
# Add the parent directory to the system path
parent_dir = os.path.abspath(os.path.join(current_dir, ".."))
sys.path.append(parent_dir)

from config.config import Config

app_config = Config(r"../config/config.yml")

app = FastAPI()

@app.get("/get_analysed_dataset_outputs/{input_str}")
def predict(input_str: str):

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
    df = pd.read_csv("../" + input_to_dataset_mapper[input_str])

    return df.to_dict(orient='records')

@app.get("/")
def predict(input_str: str):

    return "Nice Job!, For example GUI input, go -> get_analysed_dataset_outputs/monthly_total"