# pip install requests
import streamlit as st
import pandas as pd
import requests
import plotly.graph_objects as go
import numpy as np
import re

# st.header("Enter the Keyword")
selected_keyword = st.text_input("Enter Keyword")


def clean_data(raw_data):
    # Remove function name and surrounding text
    cleaned_data = re.sub(r'my_amazing_function && my_amazing_function\((.*)\)', r'\1', raw_data)

    # Convert escaped characters to their original form
    cleaned_data = cleaned_data.encode().decode('unicode_escape')

    # Extract keywords using regular expression
    keywords = re.findall(r'"(.+?)"', cleaned_data)

    # Remove unwanted elements and clean keywords
    keywords = [re.sub(r'<\\/b>', '', keyword) for keyword in keywords if not re.match(r'^[a-z]$', keyword)]

    # Remove unwanted elements and clean keywords
    keywords = [re.sub(r'<b>', '', keyword) for keyword in keywords if not re.match(r'^[a-z]$', keyword)]


    return keywords


if selected_keyword:
    st.sidebar.write("Select Region")
    
    # List of options for the dropdown
    options = ['Global','India', 'USA']
    
    # Dropdown widget in the sidebar
    selected_region = st.sidebar.selectbox("Select an option:", options)
    if selected_region == 'Global': selected_option = ''
    elif selected_region == 'India': selected_region = 'in'
    elif selected_region == 'USA': selected_region = 'us'


    # my_data = {
    #     'country': selected_region,
    #     'currency': 'USD',
    #     'dataSource': 'gkp',
    #     'kw[]': selected_keyword
    # }
    # my_headers = {
    #     'Accept': 'application/json',
    #     'Authorization': st.secrets["API"]
    # }

    # response = requests.post(
    #     'https://api.keywordseverywhere.com/v1/get_keyword_data', data=my_data, headers=my_headers)

    # keywords_data = response.json()['data']
    # trend_dict = keywords_data[0]["trend"]
    # keywords_dict = keywords_data[0]

    # trend_list = []
    # for i in trend_dict:
    #     trend_list.append(i["value"])
    

    # date_list = []
    # for i in trend_dict:
    #     date_list.append(i["month"]+  " " + str(i["year"]))

    # keyword = keywords_data[0]["keyword"]
    # df = pd.DataFrame(columns=["vol", "cpc", "competition", "trend"])

    # Volume = keywords_dict["vol"]
    # CPC = keywords_dict["cpc"]["currency"] + keywords_dict["cpc"]["value"]
    # Competition = keywords_dict["competition"]
    # credits = response.json()["credits"]



    #Related Searches
    url = "https://www.google.com/complete/search"
    params = {
    "client": "hp",
    "hl": "en",
    "sugexp": "msedr",
    "gs_rn": "62",
    "gs_ri": "hp",
    "cp": "1",
    "gs_id": "9c",
    "q": selected_keyword,
    "xhr": "t",
    "callback": "hello",
    }

    response = requests.get(url, params=params)
    raw_data = response.text

    keywords = clean_data(raw_data)
    data = keywords[:-2]
    # Regular expression pattern to match URLs
    url_pattern = re.compile(r'https?://\S+|/url\?url=\S+')

    # Remove URLs from the list
    filtered_data = [item for item in data if not url_pattern.search(item)]


    
    # Display the list in the sidebar
    st.sidebar.header("Related Searches")
    for item in filtered_data:
        st.sidebar.write(item)
