import streamlit as st
from streamlit_option_menu import option_menu
# from create import create
# from database import create_table
from home import home
from delete import delete
from read import read
from insert import insert
from update import update
from query import query
from databaseinformation import dataInfo
from test import test
import base64

def get_base64(bin_file):
    with open(bin_file,'rb') as f:
        data = f.read()
    return base64.b64encode(data).decode()


def set_background(png_file):
    bin_str = get_base64(png_file)
    page_bg_img = "<style> .stApp{background-image: url('data:image/png;base64,%s');background-size: contain;background-repeat: no-repeat;}</style>"%bin_str  
    st.markdown(page_bg_img,unsafe_allow_html=True)

# set_background('E:\\CSE\\cs5sem\\DBMS\\Intership managment system\\python\\testimg1.jpg')
# set_background('E:\\CSE\\cs5sem\\DBMS\\Intership managment system\\19873.jpg')
set_background('C:\\Users\\Hithesh Patel\\Downloads\\42494.jpg')
# set_background('C:\\Users\\\Hithesh Patel\\Downloads\\1902.i039.011.P.m004.c30.cloud services isometric icons-08.jpg')
def main():
    with st.sidebar:
        # menu = ["Add", "View", "Edit", "Remove"]
        # icons = ["database-fill-add","house","gear","0-square"]
        selected = option_menu("Main menu", ["Home","Add","View", "Update", "Remove","Query","Database"], icons=["bi bi-house","bi bi-cloud-plus","bi bi-search","bi bi-pencil-square","bi bi-trash","bi bi-terminal","bi bi-file-earmark-bar-graph"],menu_icon="cast",default_index=0)
        
        # selected
    # st.title("Welcome")
    
    # choice = st.sidebar.selectbox("Menu",menu)
    # create_table()
    with open("index.css") as source_css:
        st.markdown(f"<style>{source_css.read()}</style>",unsafe_allow_html=True)

    if selected == "Home":
        st.subheader("Internship Management system")
        home()
    if selected == "Add":
        st.header("Enter Student Details:")
        insert()
    elif selected == "View":
        st.subheader("View created tasks")
        read()
    elif selected == "Update":
        st.subheader("Update created tasks")
        update()
    elif selected == "Remove":
        st.subheader("Delete created tasks")
        delete()
    elif selected == "Query":
        st.subheader("Enter your query")
        query()
    elif selected == "Database":
        st.subheader("Database Information")
        dataInfo()
    # elif selected == "Test":
    #     st.subheader("Test here")
    #     test()
    # else:
    #     st.subheader("You may have reached this section due to some error please reload your page once")
if __name__ == '__main__':
    main()
