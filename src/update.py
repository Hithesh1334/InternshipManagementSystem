import streamlit as st 

import pandas as pd

from database import view_only_srn
from database import get_table_data
from  database import edit_data
from database import view_only_cname
from database import get_company_data
from database import edit_company_data
from database import view_only_manager
from database import edit_manager_data
from database import view_only_internship
from database import edit_internship_data
from database import view_only_result
from database import edit_result_data
from database import view_only_feedback
from database import edit_feedback_data


def update():
    # srn = ['PES1UG20CS300','PES1UG20CS100','PES1UG20CS400']

    list_data = [i[0] for i in view_only_srn()]
    selected_data = st.selectbox("Student To edit",list_data)
    res = get_table_data(selected_data)
    # print(res)
    col1,col2 = st.columns(2)
    
    srn = res[0][0]
    s_Fname = res[0][1]
    s_Lname = res[0][2]
    Dob = res[0][3]
    Email = res[0][4]
    Gender = res[0][5]
    yearOfGraduation = res[0][6]
    # sphone = res[0][7]
    with col1:
        new_srn = st.text_input("srn", srn)
        new_Fname = st.text_input("FirstName", s_Fname)
        new_Lname = st.text_input("LastName", s_Lname)
        new_dob = st.date_input("DOB:",Dob)
    with col2:
        new_Email = st.text_input("Email:",Email)
        new_Gender = st.text_input("Gender", Gender)
        new_yearOfGraduation = st.text_input("yearOfGraduation:", yearOfGraduation)
        # new_sphone = st.text_input("Sphone:",sphone)
    # edit_data(new_srn,new_Fname,new_Lname,new_dob,new_Email,new_Gender,new_yearOfGraduation,selected_data)
    edit_data(new_Fname,new_Lname,new_dob,new_Email,new_Gender,new_yearOfGraduation,selected_data)
    # edit_sphone_data(new_sphone,srn,sphone)
   
    cname_data = view_only_cname(srn)
    print("Cname :",cname_data[0])
    res2 = get_company_data(cname_data[0])
    print(res2)
    cname = res2[0][0]
    cemail = res2[0][1]
    # cphone = res2[0][2]
    # caddress = res2[0][3]

    col3,col4 = st.columns(2)
    with col3:
        new_cname = st.text_input("Cname:",cname)
    with col4:
        new_ceamil = st.text_input("CEmail:",cemail)
    edit_company_data(new_ceamil,new_cname)
    # edit_cphone_data(new_cphone,cname,cphone)

    manager_data = view_only_manager(srn)
    # print(manager_data)
    mssn = manager_data[0][0]
    m_Fname = manager_data[0][1]
    m_Lname = manager_data[0][2]
    mEmail = manager_data[0][3]

    col5,col6 = st.columns(2)
    with col5:
        new_mssn = st.text_input("MSSN:",mssn)
        new_m_Fname = st.text_input("ManagerFname:",m_Fname)
    with col6:
        new_m_Lname = st.text_input("ManagerLname:",m_Lname)
        new_mEmail = st.text_input("ManagerEmail:",mEmail)
    
    edit_manager_data(new_m_Fname,new_m_Lname,new_mEmail,new_mssn)


    internship_data = view_only_internship(srn)
    # print(internship_data)
    startDate = internship_data[0][0]
    EndDate = internship_data[0][1]
    TypeOfInternships = internship_data[0][2]
    Paid_NotPaid = internship_data[0][3]

    col7,col8 = st.columns(2)
    with col7:
        new_startDate = st.text_input("StartDate:",startDate)
        new_EndDate = st.text_input("EndDate:",EndDate)
    with col8:
        new_TypeOfInternships = st.text_input("TypeOfInternships:",TypeOfInternships)
        new_Paid_NotPaid = st.text_input("Paid/NotPaid:",Paid_NotPaid)
    print("This srn and canme",srn,cname)
    edit_internship_data(new_startDate, new_EndDate, new_TypeOfInternships,new_Paid_NotPaid,srn,cname)
    

    marks_data = view_only_result(srn)
    # print(internship_data)
    marks = marks_data[0][0]
    Grade = marks_data[0][1]

    col9,col10 = st.columns(2)
    with col9:
        new_marks = st.text_input("Marks:",marks)
    with col10:
        new_grade = st.text_input("Grade:",Grade)
    print("This srn and canme",new_marks,new_grade)
    edit_result_data(new_marks,new_grade,srn)


    feedback_data = view_only_feedback(srn)
    # print(internship_data)
    q_one = feedback_data[0][0]
    q_two = feedback_data[0][1]
    q_Three = feedback_data[0][2]
    q_Four = feedback_data[0][3]
    q_Five = feedback_data[0][4]


    col11,col12 = st.columns(2)
    with col11:
        new_qOne = st.text_input("q_one:",q_one)
        new_qTwo = st.text_input("q_Two:",q_two)
        new_qThree = st.text_input("q_Three:",q_Three)
        
        
    with col12:
        new_qFour = st.text_input("q_four:",q_Four)
        new_qFive = st.text_input("q_five:",q_Five)
    print("This srn and canme",srn,cname)
    edit_feedback_data(new_qOne,new_qTwo,new_qThree,new_qFour,new_qFive,srn)
