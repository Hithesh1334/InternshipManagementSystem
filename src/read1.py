import pandas as pd
import streamlit as st
import plotly.express as px
from database import view_student_info
from database import view_StuComp_info
from database import view_StuManag_info
from database import view_StuInternship_info
from database import view_result_info
# import datetime as date


def read1():
    srn = st.text_input('💁 Enter Student SRN:')
    if st.button("View"):
        student_res = view_student_info(srn)
        company_res = view_StuComp_info(srn)
        manager_res = view_StuManag_info(srn)
        internship_res = view_StuInternship_info(srn)
        result_res = view_result_info(srn)
        # st.write(student_res)
        # student_info = st.columns(1)
        # today = date.today()
        # age = today.year - '2002'

        if student_res==[] or company_res==[] or internship_res==[] or result_res==[] or manager_res==[]:
            st.warning("No Information related to the entered srn")
        student_df = pd.DataFrame(student_res, columns=['SRN', 'StudentFirestName', 'StudentLastName', 'Email', 'Phone','yearOfGraduation','Gender'])
        company_df = pd.DataFrame(company_res,columns=['CompanyName','Email','CompanyAddress','Phone'])
        manager_df = pd.DataFrame(manager_res,columns=['MSSN','ManagerFirstName','ManagerLastName','Email','Phone'])
        internship_df = pd.DataFrame(internship_res,columns=['StartDate','EndDate','TypeOfInternship','Paid_NotPaid'])
        result_df = pd.DataFrame(result_res,columns=['Questin_one','Questin_Two','Questin_Three','Questin_Four','Questin_Five','Marks','Grade'])
        with st.expander("Student's Details",expanded=True):
            st.dataframe(student_df)
        with st.expander("Student's Company Details",expanded=True):
            st.dataframe(company_df)
        with st.expander("Student's Manager Details",expanded=True):
            st.dataframe(manager_df)
        with st.expander("Student's Internship Information",expanded=True):
            st.dataframe(internship_df)
        with st.expander("Student's Result Information",expanded=True):
            st.dataframe(result_df)
        # srn = placeholder.text_input('Enter srn:',value='',key=1)
        # st.snow()
        # with st.spinner('Wait for it...'):
        #     time.sleep(5)
        # st.success('Done!')
        # col1,col2 = st.columns(2)
        # # sphone = res[0][7]
        # with col1:
        #     st.text_input("srn", student_res[0][0])
        #     st.text_input("FirstName", student_res[0][0])
        #     st.text_input("LastName", student_res[0][0])
        #     st.date_input("DOB:",Dob)
        # with col2:
        #     st.text_input("Email:",Email)
        #     st.text_input("Gender", Gender)
        #     st.text_input("yearOfGraduation:", yearOfGraduation)

