import streamlit as st
from streamlit_echarts import st_echarts
import os
from PIL import Image
import pandas as pd
import gui_utils
from datetime import datetime,  date
import sys
import plotly.express as px
import plotly.graph_objects as go

st.set_page_config(
    page_title="All Homes Prediction Page",
    page_icon="📈",
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
st.header("All Homes Predictions")
st.write("""Using energy consumption readings for a sample of 5,567 London Households that took part in the Low Carbon London project between November 2011 and February 2014, an energy consumption prediction for high, average and low income households is made, and its results are represented on this page.""")

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

#Predict data via utility function
prediction = get_data(query="all_home_predictions")

# Seperator for Metrics
st.subheader("Prediction Performance", divider="rainbow")

col1, col2 = st.columns(2)

metrics= get_data(query="performance_metrics")
average_income_values = metrics.loc[metrics['income_type'] == 'average_income']

mape = round(average_income_values['mape'].values[0] * 100, 1)
rmse = average_income_values['rmse'].values[0]
mae = average_income_values['mae'].values[0]

with col1:
    options_mape = gui_utils.generate_gauge_options(mape, 'MAPE')
    st_echarts(options_mape, height=320)

with col2:

    with st.expander("MAPE Value Interpretation", expanded=True):

        st.markdown("""
        \nThe colors on the gauge are assigned based on these criteria:
        \n<span style='color:green'>**Green:**</span> If the MAPE value is between 0 and 10%, the model is considered highly successful
        \n<span style='color:blue'>**Blue:**</span> If the MAPE value is between 10% and 20%, the model is considered successful
        \n<span style='color:red'>**Red:**</span> If the MAPE value is greater than 20%, the model is considered unsuccessful
        """, unsafe_allow_html=True)
col1_metric, col2_metric, col3_metric = st.columns(3)
with col1_metric:
    st.metric("MAE", mae, help ="It measures the average absolute difference between the predicted values and the actual values in a dataset.")
with col2_metric:
    st.metric("RMSE", rmse, help ="It measures the average deviation between the predicted values and the actual values in a dataset.")
with col3_metric:
    @st.cache_data
    def convert_df(df):
        return df.to_csv().encode('utf-8')
    
    new_column_names = {'ds': 'Datetime', 'y': 'Actual', 'yhat': 'Predicted', 'yhat_lower': 'Lower Bound', 'yhat_upper': 'Upper Bound'}
    prediction_csv = prediction.rename(columns=new_column_names)

    csv = convert_df(prediction_csv)
    st.download_button(
    label="Download Prediction",
    data=csv,
    file_name='All_Homes_Prediction.csv',
    mime='text/csv',
)
    
st.subheader("Line Chart of Daily Predictions", divider="rainbow")

st.write("""Daily energy consumption estimate is shown in the line chart below. This chart shows the actual value, prediction, lower bound, and upper bound. If the actual values fall within the boundaries, it can be said that a successful prediction has been made.""")
st.markdown("")

prediction_daily = prediction.copy()
prediction_daily['ds'] = pd.to_datetime(prediction_daily['ds'])
prediction_daily = prediction_daily.groupby(prediction_daily['ds'].dt.date)[['y', 'yhat', 'yhat_upper', 'yhat_lower']].sum().reset_index()
new_column_names = {'ds': 'Day', 'y': 'Actual', 'yhat': 'Predicted', 'yhat_lower': 'Lower Bound', 'yhat_upper': 'Upper Bound'}
prediction_daily = prediction_daily.rename(columns=new_column_names)
prediction_daily = prediction_daily.drop(prediction_daily.index[-1])

# Plotly line chart
fig = px.line(prediction_daily, x='Day', y=['Actual', 'Predicted'])

# Get the dates for the start of each week
week_starts = pd.date_range(start=prediction_daily['Day'].min(), end=prediction_daily['Day'].max(), freq='W-MON')

# Modify line colors for predicted and actual lines
fig.update_traces(line=dict(color='darkgreen', width=3), selector=dict(name='Predicted'))
fig.update_traces(line=dict(color='darkred', width=3), selector=dict(name='Actual'))

# Adjust the opacity of the shaded area
for i in range(len(prediction_daily) - 1):
    legend_name = 'Upper and Lower Bounds' if i == 0 else None  # Set legend name only for the first trace
    fig.add_trace(go.Scatter(
        x=[prediction_daily['Day'][i], prediction_daily['Day'][i + 1], prediction_daily['Day'][i + 1], prediction_daily['Day'][i]],
        y=[prediction_daily['Upper Bound'][i], prediction_daily['Upper Bound'][i + 1], prediction_daily['Lower Bound'][i + 1], prediction_daily['Lower Bound'][i]],
        fill='toself',
        fillcolor='rgba(173, 216, 230, 0.3)',  # Reduce the opacity here
        line=dict(color='rgba(0, 0, 0, 0)'),
        showlegend=bool(legend_name),
        name=legend_name, 
        hoverinfo='skip'
    ))

# Add upper bound scatter plot with text display on hover
fig.add_trace(go.Scatter(
    x=prediction_daily['Day'],
    y=prediction_daily['Upper Bound'],
    mode='lines',
    line=dict(color='rgba(0, 0, 0, 0)', width=0), 
    hoverinfo='text',  # Show customized text on hover
    hovertemplate='variable: Upper Bound<br>Day: %{x}<br>value: %{y}',  # Define hover template
    showlegend=False
))

# Add lower bound scatter plot with text display on hover
fig.add_trace(go.Scatter(
    x=prediction_daily['Day'],
    y=prediction_daily['Lower Bound'],
    mode='lines',
    line=dict(color='rgba(0, 0, 0, 0)', width=0),
    hoverinfo='text',  # Show customized text on hover
    hovertemplate='variable: Lower Bound<br>Day: %{x}<br>value: %{y}',  # Define hover template
    showlegend=False
))

fig.update_layout(
    autosize=True,
    margin=dict(l=10, r=10, t=20, b=20),
    yaxis_title='Energy Consumption [kWh]', 
    legend=dict(
        orientation='h',
        x=0,
        y=-0.25,
        traceorder='normal',
        bordercolor='rgba(0, 0, 0, 0)',
        borderwidth=1,
        title=None,
        font=dict(
            family='Arial',
            size=15
        )
    ),
    xaxis=dict(
        tickvals=week_starts,
        tickformat='%b %d\n%Y'
    )
)

# Render Plotly chart in Streamlit
st.plotly_chart(fig, use_container_width=True)

st.subheader("Line Chart of Hourly Predictions", divider="rainbow")
st.write("""After selecting the relevant day from the date tab, the energy consumption estimate for this day is shown in the line chart below. This chart shows the actual value, prediction, lower bound, and upper bound. If the actual values fall within the boundaries, it can be said that a successful prediction has been made.""")

# Date selection 21 sep 2013-27 feb 2014
default_date = datetime(2013, 9, 21)
selected_date = st.date_input('Select a date', default_date)

start_date = date(2013, 9, 21)
end_date = date(2014, 2, 27)
# Date control
if start_date <= selected_date <= end_date:

    # Filter date
    filtered_df = prediction[prediction['ds'].str.contains(str(selected_date))]

    filtered_df['ds'] = pd.to_datetime(filtered_df['ds'])

    selected_columns = ['ds', 'y', 'yhat', 'yhat_lower', 'yhat_upper']
    df_selected = filtered_df[selected_columns]
    new_column_names = {'ds': 'Hour', 'y': 'Actual', 'yhat': 'Predicted', 'yhat_lower': 'Lower Bound', 'yhat_upper': 'Upper Bound'}
    df_selected = df_selected.rename(columns=new_column_names)
    st.markdown("")

    # Plotly line chart
    fig = px.line(df_selected, x='Hour', y=['Actual', 'Predicted'])

    # Modify line colors for predicted and actual lines
    fig.update_traces(line=dict(color='darkgreen', width=3), selector=dict(name='Predicted'))
    fig.update_traces(line=dict(color='darkred', width=3), selector=dict(name='Actual'))
    df_selected = df_selected.reset_index()
    # Adjust the opacity of the shaded area
    for i in range(len(df_selected) - 1):
        legend_name = 'Upper and Lower Bounds' if i == 0 else None  # Set legend name only for the first trace
        fig.add_trace(go.Scatter(
            x=[df_selected['Hour'][i], df_selected['Hour'][i + 1], df_selected['Hour'][i + 1], df_selected['Hour'][i]],
            y=[df_selected['Upper Bound'][i], df_selected['Upper Bound'][i + 1], df_selected['Lower Bound'][i + 1], df_selected['Lower Bound'][i]],
            fill='toself',
            fillcolor='rgba(173, 216, 230, 0.3)',  # Reduce the opacity here
            line=dict(color='rgba(0, 0, 0, 0)'),
            showlegend=bool(legend_name),
            name=legend_name, 
            hoverinfo='skip'
        ))

    # Add upper bound scatter plot with text display on hover
    fig.add_trace(go.Scatter(
        x=df_selected['Hour'],
        y=df_selected['Upper Bound'],
        mode='lines',
        line=dict(color='rgba(0, 0, 0, 0)', width=0), 
        hoverinfo='text',  # Show customized text on hover
        hovertemplate='variable: Upper Bound<br>Hour: %{x}<br>value: %{y}',  # Define hover template
        showlegend=False
    ))

    # Add lower bound scatter plot with text display on hover
    fig.add_trace(go.Scatter(
        x=df_selected['Hour'],
        y=df_selected['Lower Bound'],
        mode='lines',
        line=dict(color='rgba(0, 0, 0, 0)', width=0),
        hoverinfo='text',  # Show customized text on hover
        hovertemplate='variable: Lower Bound<br>Hour: %{x}<br>value: %{y}',  # Define hover template
        showlegend=False
    ))

    fig.update_layout(
        autosize=True,
        margin=dict(l=10, r=10, t=20, b=20),
        yaxis_title='Energy Consumption [kWh]', 
        legend=dict(
            orientation='h',
            x=0,
            y=-0.25,
            traceorder='normal',
            bordercolor='rgba(0, 0, 0, 0)',
            borderwidth=1,
            title=None,
            font=dict(
                family='Arial',
                size=15
            )
        )
    )

    # Render Plotly chart in Streamlit
    st.plotly_chart(fig, use_container_width=True)
   
else:
    st.warning("Selected date is outside the valid range. Please choose a date between 21 September 2013 and 27 February 2014.")

#Distribution graph
prediction_for_distribution = prediction.copy()
# Convert 'ds' column to datetime
prediction_for_distribution['ds'] = pd.to_datetime(prediction_for_distribution['ds'])

# Create a new 'hour' column
prediction_for_distribution['hour'] = prediction_for_distribution['ds'].dt.hour

# Group by 'hour' and calculate the mean of 'yhat'
hourly_mean_yhat = prediction_for_distribution.groupby('hour')['yhat'].mean().reset_index()
mean_list = hourly_mean_yhat['yhat'].tolist()
hour_list = hourly_mean_yhat['hour'].tolist()

electricity_data = mean_list
time_labels = hour_list
morning_start='7'
morning_end='10'
evening_start='17'
evening_end='21'

with st.container():
    st.subheader("Distribution of Electricity", divider="rainbow")
    st.write("""The chart below presents the hourly average of forecast values. This chart highlights the morning and evening peak hours, which are the time periods of the day when the most energy is consumed. By using this chart, energy providers can see the energy consumption that varies during the day more clearly and make their plans accordingly.""")

    option_electricity_distribution = gui_utils.generate_electricity_distribution_options(electricity_data, time_labels, morning_start, morning_end, evening_start, evening_end)
    st_echarts(option_electricity_distribution, height=600)

st.subheader("Data Explainability", divider="rainbow")
# Images
image_all_homes_depence = gui_utils.getImage("shap_dependence_plot_all_homes.png")
image_all_homes_summary = gui_utils.getImage("shap_summary_plot_all_homes.png")
image_all_homes_interaction_summary = gui_utils.getImage("shap_interaction_summary_plot_all_homes.png")
image_all_homes_description = gui_utils.getImage("description_variables.png")

col2_1, col2_2 = st.columns(2)
with col2_1:
   st.image(image_all_homes_depence, caption="Depence Plot")
with col2_2:
    st.image(image_all_homes_summary, caption="Summary Plot")  

col3_1, col3_2 = st.columns(2)
with col3_1:
   st.image(image_all_homes_description, caption="Description Table")
with col3_2:
   st.image(image_all_homes_interaction_summary, caption="Interaction Summary Plot")