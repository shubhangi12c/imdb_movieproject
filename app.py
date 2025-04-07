# Importing necessary packages
import streamlit as st
import pandas as pd
from utils import api_extracter

# Create an instance/object of the class 
client = api_extracter()

# Create webpage title
st.set_page_config(page_title="IMDB Top Movies Project",layout="wide")

# Create website title
st.title("IMDB Top Movies App")

st.subheader("By Shubhangi Chavan")

# create a button which prompts user about top movies data
button = st.button("Click here to view most popular movie titles")

# action to be performed when above button is clicked
if button:
    data = client.get_data()
    #st.text(data)
    #create a dataframe to display the data collected in tabular format
    df = pd.DataFrame(data,columns=["Movie Names","Release Year","Rank"])
    st.dataframe(df)

    csv_data = df.to_csv(index=False).encode("utf-8")

    # TO include a download button
    st.download_button(
        label = "Download above content as csv file",
        data = csv_data,
        file_name = "IMDB Popular Movie data.csv",
        mime = "text/csv"
    )
