import streamlit as st
import pandas as pd
# import decode as decode
from database import data_upload
# from database import if_exists_in

def home():
    # st.write("Upload your csv file here")
    data = st.file_uploader("Upload csv file")
    # df = pd.read_csv(data)
    # csv
    if data is not None:
        bytes_of_data = (data.getvalue()).decode("utf8")
        st.write(bytes_of_data)

        # dataframe = pd.read_csv(data)
        # df = pd.DataFrame(dataframe,columns=['Name','DOB','Grade','Company'])
        # st.write(df)

    
    # if_exists_in(data)