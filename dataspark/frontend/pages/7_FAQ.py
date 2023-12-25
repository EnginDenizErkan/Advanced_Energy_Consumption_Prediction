import streamlit as st
import gui_utils
from PIL import Image
import os

st.set_page_config(
    page_title="Frequently Asked Questions",
    page_icon="❓",
    layout="wide",
)

# Image
image = gui_utils.getImage("faq.png")
# Create a container to center the image
col1_1, col1_2, col1_3 = st.columns([1, 1.5, 1])  # Adjust the column widths as needed

with col1_2:
    st.markdown(
        "<style>div.stImage>div>img { display: block; margin-left: auto; margin-right: auto; }</style>",
        unsafe_allow_html=True,
    )
    st.image(image, width=350, use_column_width=True)   

custom_css = """
<style>
.big-font {
    font-size: 28px !important;
    font-weight: bold !important;
}

.purple-text {
    color: purple !important;
    font-size: 32px !important;
    font-weight: bold !important;
}

</style>
"""

# Seperator
st.subheader("", divider="rainbow")

st.markdown(custom_css, unsafe_allow_html=True)
st.markdown('<p class="big-font"><span class="purple-text">Frequently Asked Questions</span></p>', unsafe_allow_html=True)
st.markdown("")

with st.expander("How accurate are the electricity consumption predictions?"):
    st.write("The accuracy of predictions is measured using various metrics such as RMSE, MAPE, and MAE. You can find these metrics on the Prediction Pages.")

with st.expander("How can I interpret the RMSE-MAPE-MAE value on the Prediction Performance Page?"):
    st.write("RMSE (Root Mean Squared Error), MAPE (Mean Absolute Percentage Error), and MAE (Mean Absolute Error) are metrics that measure the accuracy of predictions. Generally, lower values indicate better accuracy. RMSE measures the average error magnitude, MAPE expresses errors as a percentage of the actual values, and MAE is the average absolute difference between predicted and actual values.")

with st.expander("Can I download the raw dataset for further analysis?"):
    st.write("Yes, you can download the raw dataset for further analysis from the given link on the Business Data Analysis page. Please use the provided dataset files for your analysis.")

with st.expander("What factors are considered in making consumption predictions?"):
    st.write(
        """The electricity consumption predictions are made using the Prophet Time Series Forecasting model with a 30-minute frequency. The model considers a variety of factors and features to enhance prediction accuracy. Here are the key factors and features considered in making consumption predictions:
            \n1. Prophet Model:
               \nThe model of choice for time series forecasting is Prophet. It is designed to handle daily observations that display patterns on different time scales, including holidays and special events.
            \n2. Frequency:
               \nThe time series data is sampled at a 30-minute frequency, capturing fine-grained patterns in electricity consumption.
            \n3. Cross Validation Methods:
               \nTwo different cross-validation methods are employed during training: cross-validation time series and block cross-validation with time series. This helps assess the model's performance under various scenarios.
            \n4. Data Sets:
               \nFour different data sets are utilized:
                 \n-Main data set: Energy consumption of all houses.
                 \n-2nd data set: Energy consumption of families in affluent financial status.
                 \n-3rd data set: Energy consumption of families in comfortable financial status.
                 \n-4th data set: Energy consumption of families in adversity financial status.
            \n5. Generated Features:
               \nNew features are generated to improve the model's predictive capabilities.
                 \n-Date/Time (Date)
                 \n-Energy consumption (Numeric time series)
                 \n-Visibility, windBearing, temperature, dewPoint, pressure, apparentTemperature, windSpeed, precipType, humidity (Numeric time series)
                 \n-Year, month, day, hour, minute (Numeric)
                 \n-Week_day, Season, Holiday (Categorical)
            \n6. Feature Details:
               \nFeatures include both numeric time series and categorical variables, covering various aspects such as weather conditions, date/time components, and socio-economic factors.
               \nDate/Time (Date), energy(kWh/hh) (Numeric time series), visibility (Numeric time series), windBearing (Numeric time series), temperature (Numeric time series), dewPoint (Numeric time series), pressure (Numeric time series), apparentTemperature (Numeric time series), windSpeed (Numeric time series), precipType (Numeric time series), humidity (Numeric time series), year(Numeric), month(Numeric),day(Numeric), hour(Numeric), minute(Numeric), week_day(Categoric), Season(Categoric), Holiday(Categoric)""")

with st.expander("Can I see the energy consumption data for holidays and compare it with real values?"):
    st.write("Yes, you can analyze energy consumption data for holidays. The Average Energy Consumption Based on Days of the Week chart on the Business Data Analysis page, provides insights into consumption patterns on days of week.")

with st.expander("Can I suggest additional data or methods related to the project? If so, can you specify a communication channel?"):
    st.write("Absolutely! We appreciate your input. Please use the designated communication channel or contact the project administrators to suggest additional data or methods. This could include adding features to the prediction model or proposing improvements.")