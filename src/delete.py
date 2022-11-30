import pandas as pd
import streamlit as st
from database import view_all_data, delete_data
from database import if_srn_exists
# from database import viewAllData_after_delete

def delete():
    result = view_all_data()
    student_srn = st.text_input("Enter Student srn to be deleted:")
    current_data = pd.DataFrame(result, columns=['srn', 's_Fname', 's_Lname', 'DOB','Email', 'GENDER','YearOfGraduation','marks','Grade','PhoneNo'])
    with st.expander("Current data",expanded=True):
        st.dataframe(current_data)
    # list_of_dealers = [i[0] for i in view_only_dealer_names()]
    # selected_dealer = st.selectbox("Task to Delete", list_of_dealers)
    # st.warning("Do you want to delete {}".format(student_srn))
    if st.button("Delete STUDENT"):
        #USE HERE NOT EXIST SQL QUERY
        res = if_srn_exists(student_srn)
        print("This is  res ",res)
        if res != []:
            delete_data(student_srn)
            st.success("STUDENT has been deleted successfully")
            # new_result = viewAllData_after_delete()
            # updated_data = pd.DataFrame(new_result, columns=['srn', 's_Fname', 's_Lname', 'Email','Gender', 'yearOfGraduation','Mssn','marks','Grade','PhoneNo'])   
            # with st.expander("Updated data"):
            #     st.dataframe(updated_data)
        else:
            st.success('Data is not present in database to delete')