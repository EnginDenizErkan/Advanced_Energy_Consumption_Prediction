import streamlit as st
import pandas as pd
import os
from PIL import Image

def getPathForFA(docname):
    dir_root = os.path.dirname(os.path.abspath(__file__))
    dir_parent = os.path.abspath(os.path.join(dir_root, os.pardir))
    path = os.path.join(dir_parent, "frontend/frontend_artifacts", docname)
    return path

def getImage(docname):
    path = getPathForFA(docname)
    image = Image.open(path)
    return image

def getDataFrom_csv(docname):

    path = getPathForFA(docname)
    df = pd.read_csv(path, index_col=0)
    return df

def generate_gauge_options(value, name):
    options_gauge = {
        "tooltip": {
            "formatter": '{a} <br/>{b} : {c}%'
        },
        "series": [
            {
                "name": name,
                "type": 'gauge',
                "progress": {
                    "show": False
                },
            "detail": {
                "valueAnimation": True,
                "formatter": '{value}'
            },
            "axisLine": {
                "lineStyle": {
                    "color": [
                        [0.1, 'green'],   # 0-0.1 green
                        [0.2, 'blue'],    # 0.01-0.02 blue
                        [1, 'red']        # 0.02-1 red
                    ]
                }
            },
            "data": [
                {
                    "value": value,
                    "name": name
                }
                ]
            }
        ]
    }
    return options_gauge

def generate_electricity_distribution_options(data, time_labels, morning_start, morning_end, evening_start, evening_end):
    options_electricity_distribution = {

        "tooltip": {
            "trigger": 'axis',
            "axisPointer": {
                "type": 'cross'
            }
        },
        "toolbox": {
            "show": True,

        },
        "xAxis": {
            "type": 'category',
            "boundaryGap": False,
            "data": time_labels,
            "name": 'Time (Hour)'
        },
        "yAxis": {
            "type": 'value',
            "axisLabel": {
                "formatter": '{value} '
            },
            "axisPointer": {
                "snap": True
            },
            "name": 'Energy Consumption (kWh)'
        },
        "visualMap": {
            "show": False,
            "dimension": 0,
            "pieces": [
                {"lte": 7, "color": 'green'},
                {"gt": 7, "lte": 10, "color": 'red'},
                {"gt": 10, "lte": 17, "color": 'green'},
                {"gt": 17, "lte": 21, "color": 'red'},
                {"gt": 21, "color": 'green'}
            ]
        },
        "series": [
            {
                "name": 'Electricity',
                "type": 'line',
                "smooth": True,
                "data": data,
                "markArea": {
                    "itemStyle": {
                        "color": 'rgba(255, 173, 177, 0.4)'
                    },
                    "data": [
                        [
                            {"name": 'Morning Peak', "xAxis": morning_start},
                            {"xAxis": morning_end}
                        ],
                        [
                            {"name": 'Evening Peak', "xAxis": evening_start},
                            {"xAxis": evening_end}
                        ]
                    ]
                }
            }
        ]
    }
    return options_electricity_distribution


def generate_line_chart_options(legend_names, dataframes, dataattribute_value, dataattribute_time):
    options_line_chart = {
        "tooltip": {"trigger": "axis"},
        "legend": {"data": legend_names},
        "grid": {"left": "6%", "right": "4%", "bottom": "3%", "containLabel": True},
        "xAxis": {"type": "category", "boundaryGap": False,'name': 'Date', "data": dataframes[0][dataattribute_time].tolist()},
        "yAxis": {"type": "value",'name': 'Energy Consumption (kWh)'},
        "series": [
            {"name": legend_names[i], "type": "line", "data": dataframes[i][dataattribute_value].tolist()}
            for i in range(len(dataframes))
        ],
    }
    return options_line_chart

def generate_stacked_bar_chart_options(legend_names, dataframes, dataattribute_value, dataattribute_time):
    options_stacked_bar = {
        "tooltip": {"trigger": "axis", "axisPointer": {"type": "shadow"}},
        "legend": {
            "data": legend_names,
        },
        "grid": {"left": "6%", "right": "4%", "bottom": "3%", "containLabel": True, "width": "85%"},
        "xAxis": {"type": "value",
                  'name': 'Energy Consumption (kWh)',
                  },
        "yAxis": {
            "type": "category",
            "data": dataframes[0][dataattribute_time].tolist(),  # 'time' column from the first dataframe
            'name': 'Date'
        },
        "series": [
            {
                "name": legend_names[i],
                "type": "bar",
                "stack": "total",
                "emphasis": {"focus": "series"},
                "data": dataframes[i][dataattribute_value].tolist(),  # 'consumption' column from each dataframe
            }
            for i in range(len(dataframes))
        ],
    }
    return options_stacked_bar

def generate_stacked_area_chart_options(legend_names, dataframes, dataattribute_value, dataattribute_time):
    options_stacked_area = {
        "tooltip": {
            "trigger": 'axis',
        },
        "legend": {
            "data": legend_names,
        },
        "grid": {
            "left": '3%',
            "right": '4%',
            "bottom": '3%',
            "containLabel": True
        },
        "xAxis": [
            {
                "type": 'category',
                "boundaryGap": False,
                "data": dataframes[0][dataattribute_time].tolist(),  # 'time' column from the first dataframe
                'name': 'Date'
            }
        ],
        "yAxis": [
            {
                "type": 'value',
                'name': 'Energy Consumption (kWh)'
            }
        ],
        "series": [
            {
                "name": legend_names[i],
                "type": 'line',
                "stack": 'Total',
                "areaStyle": {},
                "emphasis": {
                    "focus": 'series'
                },
                "data": dataframes[i][dataattribute_value].tolist(),  # 'consumption' column from each dataframe
            }
            for i in range(len(dataframes))
        ],
    }
    return options_stacked_area

def generate_holiday_otherday_options(x_axis_labels,holidayslist,otherdays_list):
    echarts_option = {
    'tooltip': {
        'trigger': 'axis',
        'axisPointer': {
            'type': 'shadow'
        }
    },
    'legend': {
        'data': ['Holidays', 'Other Days']
    },
    'toolbox': {
        'show': True,
        'orient': 'vertical',
        'left': 'right',
        'top': 'center',
        'feature': {
            'mark': {'show': True},
            'dataView': {'show': True, 'readOnly': False},
            'magicType': {'show': True, 'type': ['line', 'bar', 'stack']},
            'restore': {'show': True},
        }
    },
    'xAxis': [
        {
            'type': 'category',
            'axisTick': {'show': False},
            'data': x_axis_labels,
            'name': 'Days'
        }
    ],
    'yAxis': [
        {
            'type': 'value',
            'name': 'Energy Consumption (kWh)'
        }
    ],
    'series': [
        {
            'name': 'Holidays',
            'type': 'bar',
            'barGap': 0,
            'label': {
                'show': False,
                'position': 'insideBottom',
                'distance': 15,
                'align': 'left',
                'verticalAlign': 'middle',
                'rotate': 90,
                'formatter': '{c}  {name|{a}}',
                'fontSize': 16,
                'rich': {
                    'name': {}
                }
            },
            'emphasis': {
                'focus': 'series'
            },
            'data': holidayslist
        },
        {
            'name': 'Other Days',
            'type': 'bar',
            'label': {
                'show': False,
                'position': 'insideBottom',
                'distance': 15,
                'align': 'left',
                'verticalAlign': 'middle',
                'rotate': 90,
                'formatter': '{c}  {name|{a}}',
                'fontSize': 16,
                'rich': {
                    'name': {}
                }
            },
            'emphasis': {
                'focus': 'series'
            },
            'data': otherdays_list
        }
    ]
    }
    return echarts_option
