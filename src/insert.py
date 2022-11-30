import streamlit as st
from database import add_isinternat 
from database import add_student_intern  
from database import add_company
from database import add_sPhoneNo
from database import add_cPhoneNo
from database import add_result
from database import add_caddress
from database import add_manager
from database import add_mPhoneNo
from database import add_managerFeedback
from database import add_student_company

def insert():
    
    student_intern1,student_inter2,student_intern3 = st.columns(3)
    st.subheader("Company Details")
    company1,company2,company3 = st.columns(3)
    st.subheader("Internship Information Details")
    internship1,internship2,internship3 = st.columns(3)
    st.subheader("Manager Information Details")
    manager1,manager2,manager3 = st.columns(3)

    with student_intern1:
        srn = st.text_input("SRN:")
        s_Fname = st.text_input("FName:")
        s_Lname = st.text_input("LName:")
        Dob = st.date_input("DOB:")
    with student_inter2:
        yearOfGrad = st.text_input("yearOfGrad:")
        cname = st.text_input("CName:")
        marks = st.text_input("marks")
        Grade = st.text_input("Grade:")
    with student_intern3:
        Gender = st.text_input("Gender:")
        Mssn = st.text_input("MSSN:")
        Email = st.text_input("Email:")
        sPhone = st.text_input("StudentPhoneNo:")
    
    with company1:
        cEmail = st.text_input("CompanyEmail:")
    with company2:
        caddress = st.text_input("CompanyAddress:")
    with company3:
        cPhone = st.text_input("CompanyContact:")

    with internship1:
        startDate = st.date_input("StartDate:")
    with internship2:
        EndDate = st.date_input("EndDate:")
    with internship3:
        typeOfInternship = st.text_input("TypeOfInternship:")
        Paid_NotPaid = st.text_input("Paid:")

    with manager1:
            m_Fname = st.text_input("ManagerFirstName:")
            m_Lname = st.text_input("ManagerLastName:")
            mEmail = st.text_input("ManagerEmail:")
    with manager2:
            mPhone = st.text_input("ManagerPhoneNo:")
            ManagerFeedback1 = st.text_input("Q_one")
            ManagerFeedback2 = st.text_input("Q_Two")
            
    with manager3:
            
            ManagerFeedback3 = st.text_input("Q_Three")
            ManagerFeedback4 = st.text_input("Q_Four")
            ManagerFeedback5 = st.text_input("Q_Five")
    marks=ManagerFeedback1 + ManagerFeedback2 + ManagerFeedback3 + ManagerFeedback4 + ManagerFeedback5
    if st.button("Add"):

        add_company(cname,cEmail)
        add_cPhoneNo(cname,cPhone)
        add_caddress(cname,caddress)
        add_manager(Mssn,m_Fname,m_Lname,mEmail,cname)
        add_mPhoneNo(Mssn,mPhone)
        add_student_intern(srn,s_Fname,s_Lname,Email,yearOfGrad,Dob,Mssn,Gender)
        add_isinternat(startDate,EndDate,typeOfInternship,Paid_NotPaid,srn,cname)
        add_sPhoneNo(srn,sPhone)
        add_result(srn,marks,Grade)
        add_student_company(srn,cname)
        

        add_managerFeedback(ManagerFeedback1,ManagerFeedback2,ManagerFeedback3,ManagerFeedback4,ManagerFeedback5,srn,Mssn)

        # print('error in insert.py under add_data')
        # st.snow()
        st.success("Successfully added into {}".format('student_intern'))


