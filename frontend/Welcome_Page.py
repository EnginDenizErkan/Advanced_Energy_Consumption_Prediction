import streamlit as st
import os
from PIL import Image
from streamlit_extras.badges import badge
import time
import pandas as pd

st.set_page_config(
    page_title="DSEnergy Home Page",
    page_icon="👋",
    layout="wide",
)

def imageFromFA(docname):
    dir_root = os.path.dirname(os.path.abspath(__file__))
    path = os.path.join(dir_root, "frontend_artifacts", docname)
    image = Image.open(path)
    return image

def get_github(github_link, github_logo_path):
    # Display clickable image using st.markdown    
    return f'<a href="{github_link}" target="_blank"><img src="file://{github_logo_path}" alt="Go directly to GitHub page." width="100%"></a>'

# Logo
logo = imageFromFA("logo.png")

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
# Slogan
# Custom CSS for styling
custom_css = """
<style>
.big-font {
    font-size: 28px !important;
    font-weight: bold !important;
}

.blue-text {
    color: purple !important;
    font-size: 32px !important;
    font-weight: bold !important;
}

.italic-font {
    font-size: 24px !important;
    font-weight: bold !important;
    font-style: italic !important;
}

.italic-font2 {
    font-size: 16px !important;
    font-weight: bold !important;
    font-style: italic !important;
}

</style>
"""

# Display the custom CSS
st.markdown(custom_css, unsafe_allow_html=True)

# Display the text with the desired styling
#st.markdown('<p class="big-font">Unleashing the Power of Tomorrow\'s Energy Today: Welcome to <span class="blue-text">DSEnergy</span>,<span class="italic-font"> Your Gateway to Intelligent Consumption Forecasting</span></p>', unsafe_allow_html=True)

html_text = """
    <p class="big-font" style="text-align: center;">Unleashing the Power of Tomorrow's Energy Today: Welcome to <span class="blue-text">DSEnergy</span></p>
    <p class="italic-font" style="text-align: center;">Your Gateway to Intelligent Consumption Forecasting</p>
"""

st.markdown(html_text, unsafe_allow_html=True)

# Scope
st.write("Understanding the future trends in energy consumption and how they evolve under specific conditions is a pivotal aspect of the energy sector. This acquired knowledge enables energy companies to make informed strategic decisions, including planning energy supply, enhancing energy efficiency, and optimizing energy costs. As a result, it can offer a significant competitive advantage.")

# Image
image = imageFromFA("OHTL_Tower.jpg")
st.image(image)

# Seperator
st.subheader("", divider="rainbow")

# DataSpark Team

ozer_image = imageFromFA("ozer.png")
engin_image = imageFromFA("engin.png")
furkan_image = imageFromFA("furkan.png")
nilay_image = imageFromFA("nilay.png")
linkedin_badge_ozer = '''[![](https://img.shields.io/badge/linkedin-%230077B5.svg?&style=for-the-badge&logo=linkedin&logoColor=white)](https://www.linkedin.com/in/ozer-tanrisever/)'''
linkedin_badge_engin = '''[![](https://img.shields.io/badge/linkedin-%230077B5.svg?&style=for-the-badge&logo=linkedin&logoColor=white)](https://www.linkedin.com/in/engindenizerkan/)'''
linkedin_badge_furkan = '''[![](https://img.shields.io/badge/linkedin-%230077B5.svg?&style=for-the-badge&logo=linkedin&logoColor=white)](https://www.linkedin.com/in/furkan-%C3%A7inar-a3a331135/)'''
linkedin_badge_nilay = '''[![](https://img.shields.io/badge/linkedin-%230077B5.svg?&style=for-the-badge&logo=linkedin&logoColor=white)](https://www.linkedin.com/in/nilay-yorganc%C4%B1lar-akg%C3%BCl-7502a8180/)'''
github_badge_ozer = '''[![](https://img.shields.io/badge/github-%23181717.svg?&style=for-the-badge&logo=github&logoColor=white)](https://github.com/ozert)'''
github_badge_engin = '''[![](https://img.shields.io/badge/github-%23181717.svg?&style=for-the-badge&logo=github&logoColor=white)](https://github.com/EnginDenizErkan)'''
github_badge_furkan = '''[![](https://img.shields.io/badge/github-%23181717.svg?&style=for-the-badge&logo=github&logoColor=white)](https://github.com/fcinarr)'''
github_badge_nilay = '''[![](https://img.shields.io/badge/github-%23181717.svg?&style=for-the-badge&logo=github&logoColor=white)](https://github.com/niyoni)'''

st.subheader("Who we are, DataSpark")
st.write("DataSpark is a team established by METU Informatics Institute Data Informatics and Information Systems graduate students, who are the founders of DSEnergy company. DSEnergy offers artificial intelligence and machine learning solutions to its customers in the energy domain since 2023.")

col1, col2, col3, col4  = st.columns(4)

with col1:
    st.image(ozer_image)
    st.markdown('<p class="italic-font">Solution Architect<span class="italic-font2" style="font-weight: smaller;"> (Özer TANRISEVER)</span></p>', unsafe_allow_html=True)
    ozer_c1, ozer_c2 = st.columns(2)
    with ozer_c1:
        st.markdown(linkedin_badge_ozer, unsafe_allow_html=True)
    with ozer_c2:
        st.markdown(github_badge_ozer, unsafe_allow_html=True)

with col2:
    st.image(engin_image)
    st.markdown('<p class="italic-font">Data Scientist<span class="italic-font2" style="font-weight: smaller;"> (Engin Deniz ERKAN)</span></p>', unsafe_allow_html=True)
    engin_c1, engin_c2 = st.columns(2)
    with engin_c1:
        st.markdown(linkedin_badge_engin, unsafe_allow_html=True)
    with engin_c2:
        st.markdown(github_badge_engin, unsafe_allow_html=True)

with col3:
    st.image(furkan_image)
    st.markdown('<p class="italic-font">Back-end Developer<span class="italic-font2" style="font-weight: smaller;"> (Furkan ÇINAR)</span></p>', unsafe_allow_html=True)
    furkan_c1, furkan_c2 = st.columns(2)
    with furkan_c1:
        st.markdown(linkedin_badge_furkan, unsafe_allow_html=True)
    with furkan_c2:
        st.markdown(github_badge_furkan, unsafe_allow_html=True)

with col4:
    st.image(nilay_image)
    st.markdown('<p class="italic-font">Front-end Developer<span class="italic-font2" style="font-weight: smaller;"> (Nilay AKGÜL)</span></p>', unsafe_allow_html=True)
    nilay_c1, nilay_c2 = st.columns(2)
    with nilay_c1:
        st.markdown(linkedin_badge_nilay, unsafe_allow_html=True)
    with nilay_c2:
        st.markdown(github_badge_nilay, unsafe_allow_html=True)

st.markdown('')
st.markdown('')

# Insert containers separated into tabs:
tab1, tab2 = st.tabs(["Contact Info", "Get in Touch"])
tab1.write("Here's how you can reach us.")
tab2.write("Want to get in touch? We'd love to hear from you. Here you can reach us.")

with tab1:
    
    df = pd.DataFrame({'lat': [51.50003], 'lon': [-0.157058]})
    st.map(df)
    st.markdown(":pushpin: Location: 5 - 7 Kinnerton St, Belgravia, London")
    st.markdown(":telephone: Telephone: 020 7235 2166 ")
    st.markdown(":mailbox_with_no_mail: Mail: dataspark@gmail.com")

with tab2:
    st.text_input('First Name')
    st.text_input('Last Name')
    st.text_input('E-mail')
    st.text_area('What can we help you with?', help="You can express your opinions, suggestions and complaints about us in this area.")
    # Create a button
    button_clicked = st.button("Submit")

    # Display spinner if the button is clicked
    if button_clicked:
        with st.spinner("Waiting for sending"):
            # Simulate a long-running process
            time.sleep(3)
            st.success("Sent Successfully")