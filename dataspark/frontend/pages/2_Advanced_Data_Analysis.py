import pandas as pd
from ydata_profiling import ProfileReport
import streamlit as st
from streamlit_pandas_profiling import st_profile_report
import os
import sys
import gui_utils

st.set_page_config(
    page_title="Advanced Data Analysis Page",
    page_icon="📊",
    layout="wide",
)

# Logo
logo = gui_utils.getImage("logo.png")
# Create a container to center the image
col1_1, col1_2, col1_3 = st.columns([1, 0.5, 1])  # Adjust the column widths as needed

with col1_2:
    st.markdown(
        "<style>div.stImage>div>img { display: block; margin-left: auto; margin-right: auto; }</style>",
        unsafe_allow_html=True,
    )
    st.image(logo, width=250, use_column_width=True)

# Seperator
st.subheader("", divider="rainbow")
st.header("Advanced Data Analysis")

## GET DATA
    
## Add 2 level above to the path. ##
# Get the current directory (where your script is located)
current_dir = os.path.dirname(os.path.abspath(__file__))
# Add the parent directory to the system path
parent_dir = os.path.abspath(os.path.join(current_dir, ".."))
sys.path.append(parent_dir)
# Add the grandparent directory to the system path (2 levels above)
grandparent_dir = os.path.abspath(os.path.join(parent_dir, ".."))
sys.path.append(grandparent_dir)

from utils.utils import predict_data_via_api, get_data_for_gui
@st.cache_data
def get_data(query:str):
    return get_data_for_gui(data_name=query)

@st.cache_resource
def get_profile_report(query:str):
    selected_dataset = get_data(query=query)
    pr = ProfileReport(selected_dataset, title="Report")
    return pr

profile_report = get_profile_report(query="data_describe")
st_profile_report(profile_report)