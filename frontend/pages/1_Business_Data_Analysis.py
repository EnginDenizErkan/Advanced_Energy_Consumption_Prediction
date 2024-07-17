import streamlit as st
import pandas as pd
import os
from PIL import Image
from streamlit_echarts import st_echarts
import gui_utils
import sys

st.set_page_config(
    page_title="Business Data Analysis Page",
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
st.header("Dataset")

dataset_resource= "https://data.london.gov.uk/publisher/uk-power-networks"
st.write("**Dataset Name:** Smart Meters in London")
st.markdown(f"**Dataset Owner:** LONDON DATASTORE [UK Power Networks]({dataset_resource})")
st.write("**Dataset Description:** Dataset is based on governmentally provided data collected from smart meter electricity measurements of +5500 households in London. It was created to forecast energy consumption and weather in London and the data was combined. ")

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

# Get data via utility function
data_describe = get_data(query="data_describe_all")

data_describe.set_index('Type of Dataset (Income Based)', inplace=True)
data_describe = data_describe.drop(columns=['Energy Consumption (kw/H)'])

st.subheader("Dataset Description Table", divider="rainbow")
st.write("""Dataset captures the income-based energy consumption across half-hourly timestamps for three distinct household categories: low, average, and high. Within each category, the dataset details the count of observations, the mean energy consumption, standard deviation, minimum and maximum values, as well as quartiles (25th, 50th, and 75th percentiles). This comprehensive breakdown allows for a granular understanding of how energy usage varies across income levels and time intervals.""")

dataset_type = st.multiselect(
    "Choose dataset types", list(data_describe.index), ["All Homes", "Low Income Homes"]
)
if not dataset_type:
    st.error("Please select at least one dataset type.")
else:
    data = data_describe.loc[dataset_type]
    st.write("", data.sort_index())
    data = data.T.reset_index()
    data = pd.melt(data, id_vars=["index"]).rename(
        columns={"index": "Count", "value": "Dataset Descriptive Informations"}
    )

    st.write("Energy Consumption Units: [kWh]")

# Get data via utility function
low_income_df = get_data(query="daily_low")
high_income_df = get_data(query="daily_high")
average_income_df = get_data(query="daily_average")
total_income_df = get_data(query="daily_total")

final_daily = dataframes = [low_income_df, average_income_df, high_income_df, total_income_df]

legend_names = ["Low Income Homes","Average Income Homes","High Income Homes", "All Homes"]

with st.container():
   # Line chart
    st.subheader("Time-Daily Consumption Line Chart", divider="rainbow")
    st.write("""The chart below shows daily energy consumption data from households with different types of income.""")

    line_chart_option = gui_utils.generate_line_chart_options(legend_names, final_daily, dataattribute_value="Consumption", dataattribute_time="Time")
    st_echarts(line_chart_option, height=500)

st.write("")
selected_chart = st.selectbox("Choose a chart type for Time-Monthly Consumption", ["Stacked Line Area Chart", "Stacked Bar Chart"])

# Get data via utility function
monthly_low_income_df = get_data(query="monthly_low")
monthly_high_income_df = get_data(query="monthly_high")
monthly_average_income_df = get_data(query="monthly_average")

final_monthly = [monthly_low_income_df, monthly_average_income_df, monthly_high_income_df]

legend_names = ["Low Income Homes","Average Income Homes","High Income Homes"]

if selected_chart == "Stacked Line Area Chart":
    with st.container():
        # Stacked line chart
        st.subheader("Time-Monthly Consumption Stacked Line Area Chart", divider="rainbow")
        st.write("""The chart below shows monthly energy consumption data from households with different types of income.""")

        stacked_area_option=gui_utils.generate_stacked_area_chart_options(legend_names, final_monthly, dataattribute_value="Consumption", dataattribute_time="Time")
        st_echarts(stacked_area_option, height=500)

elif selected_chart == "Stacked Bar Chart":

    with st.container():
        # Stacked Bar chart
        st.subheader("Time-Monthly Consumption Stacked Bar Chart", divider="rainbow")
        st.write("""The chart below shows monthly energy consumption data from households with different types of income.""")

        stacked_bar_option= gui_utils.generate_stacked_bar_chart_options(legend_names, final_monthly, dataattribute_value="Consumption", dataattribute_time="Time")
        st_echarts(stacked_bar_option, height=500)

x_axis_labels = ['Mon', 'Tue', 'Wed', 'Thu', 'Fri', 'Sat', 'Sun']

daily_total_with_holiday = get_data(query="daily_total_with_holiday")

no_holiday_data = daily_total_with_holiday[daily_total_with_holiday["Type"] == "No holiday"]
no_holiday_data["Time"] = pd.to_datetime(no_holiday_data["Time"])
no_holiday_data["Day_of_Week"] = no_holiday_data["Time"].dt.day_name()
average_consumption_per_day = no_holiday_data.groupby("Day_of_Week")["Consumption"].mean()
other_days_data = average_consumption_per_day.tolist()

holiday_data = daily_total_with_holiday[daily_total_with_holiday["Type"] != "No holiday"]
holiday_data["Time"] = pd.to_datetime(holiday_data["Time"])
holiday_data["Day_of_Week"] = holiday_data["Time"].dt.day_name()
average_consumption_per_day_h = holiday_data.groupby("Day_of_Week")["Consumption"].mean()
holidays_data = average_consumption_per_day_h.tolist()

final_holiday=[holidays_data[2],holidays_data[1],holidays_data[4],holidays_data[5],holidays_data[3],holidays_data[0]]
final_no_holiday=[other_days_data[3],other_days_data[2],other_days_data[5],other_days_data[6],other_days_data[4],other_days_data[0], other_days_data[2]]

with st.container():

    st.subheader("Average Energy Consumption Based on Days of the Week", divider="rainbow")
    st.write("""In the chart below, the average energy consumption data for all houses on each day of the week is shown in two different dimensions: holidays and other days.""")

    option_holiday_other = gui_utils.generate_holiday_otherday_options(x_axis_labels,final_holiday,final_no_holiday)
    st_echarts(option_holiday_other, height=600)