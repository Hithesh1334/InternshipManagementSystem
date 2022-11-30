# import pandas as pd
import streamlit as st
# import plotly.express as px
# from database import view_student_info
# from database import view_StuComp_info
# from database import view_StuManag_info
# from database import view_StuInternship_info
from streamlit_option_menu import option_menu
import time
from read2 import read2
from read1 import read1

def read():
    # placeholder = st.empty()
    # srn = placeholder.text_input('Enter srn')
    menu = option_menu("Search",['View with Srn','View Specific'],icons=['bi bi-person-fill','bi bi-funnel-fill'],orientation='horizontal')
    if menu == 'View with Srn':
        read1()
        # srn = st.text_input('Enter srn:')
        # if st.button("View"):
        #     student_res = view_student_info(srn)
        #     company_res = view_StuComp_info(srn)
        #     manager_res = view_StuManag_info(srn)
        #     internship_res = view_StuInternship_info(srn)
        #     # st.write(student_res)
        #     # student_info = st.columns(1)
        #     student_df = pd.DataFrame(student_res, columns=['SRN', 'StudentFirestName', 'StudentLastName', 'Email', 'Phone','yearOfGraduation','Gender','student_Marks','student_Grade'])
        #     company_df = pd.DataFrame(company_res,columns=['CompanyName','Email','Phone','CompanyAddress'])
        #     manager_df = pd.DataFrame(manager_res,columns=['MSSN','ManagerFirstName','ManagerLastName','Email','Phone','ManagerFeedback'])
        #     internship_df = pd.DataFrame(internship_res,columns=['StartDate','EndDate','TypeOfInternship','Paid_NotPaid'])
        #     with st.expander("Student's Details",expanded=True):
        #         st.dataframe(student_df)
        #     with st.expander("Student's Company Details",expanded=True):
        #         st.dataframe(company_df)
        #     with st.expander("Student's Manager Details",expanded=True):
        #         st.dataframe(manager_df)
        #     with st.expander("Student's Internship Information",expanded=True):
        #         st.dataframe(internship_df)
        #     # srn = placeholder.text_input('Enter srn:',value='',key=1)
        #     # st.snow()
        #     # with st.spinner('Wait for it...'):
        #     #     time.sleep(5)
        #     # st.success('Done!')
        #     with st.expander("Dealer Location"):
        #         task_student_df = student_df['SRN'].value_counts().to_frame()
        #         task_student_df = task_student_df.reset_index()
        #         st.dataframe(task_student_df)
        #         p1 = px.pie(task_student_df, names='index', values='SRN')
        #         st.plotly_chart(p1)

    elif menu=='View Specific':
        read2()
