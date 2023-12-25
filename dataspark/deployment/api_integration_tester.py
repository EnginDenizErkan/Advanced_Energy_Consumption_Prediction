import requests
import pandas as pd
import os
import sys

## ADD 2 level above to the path. ##
# Get the current directory (where your script is located)
current_dir = os.path.dirname(os.path.abspath(__file__))
# Add the parent directory to the system path
parent_dir = os.path.abspath(os.path.join(current_dir, ".."))
sys.path.append(parent_dir)
# Add the grandparent directory to the system path (2 levels above)
grandparent_dir = os.path.abspath(os.path.join(parent_dir, ".."))
sys.path.append(grandparent_dir)

# Add the greatgrandparent directory to the system path (2 levels above)
greatgrandparent = os.path.abspath(os.path.join(grandparent_dir, ".."))
sys.path.append(greatgrandparent)

from logger.dataspark_logger import DataSparkLogger
from utils.utils import predict_data_via_api, get_data_for_gui
from config.config import Config



#Predict data via utility function
prediction = get_data_for_gui(data_name="affluent_home_predictions")
print(prediction)

prediction = get_data_for_gui(data_name="adversity_home_predictions")
print(prediction)