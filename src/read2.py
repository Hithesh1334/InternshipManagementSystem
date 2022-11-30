import streamlit as st 
import pandas as pd
from database import view_by_Paid
from database import view_by_marks
from database import view_by_oncmapus
from database import view_by_cname
from database import view_by_year
from database import view_by_PaidIncampus
from database import view_by_PaidIncampus2

def read2():
    # selected = st.selectbox("select",['Paid/NotPaid','Incampus/Offcampus','companyName','yearOfGraduation','marks'])
    selected = st.multiselect(
    'What are your favorite colors',
    ['Paid','NotPaid','Incampus','Offcampus','CompanyName','yearOfGrad','marks'],
    ['Paid'])
    print('selected',selected)
    if st.button('Fetch'):
        if len(selected)==1:
            if selected[0] == 'Paid' or selected[0]=='NotPaid':
                # paid = st.text_input('APPLY YOUR FILTER')
                # ser = st.button("search")
                # if ser:
                res = view_by_Paid(selected[0])
                df = pd.DataFrame(res,columns=['SRN','FirstName','LastName','Paid_NotPaid','CompnayName'])
                with st.expander("ONlY filter",expanded=True):
                    st.dataframe(df)
            
            if selected[0] == 'Incampus' or selected[0] == 'Offcampus':
                # paid = st.text_input('APPLY YOUR FILTER')
                # ser = st.button("search")
                # if ser:
                res = view_by_oncmapus(selected[0])
                df = pd.DataFrame(res,columns=['SRN','FirstName','LastName','Paid_NotPaid','CompnayName'])
                with st.expander("ONlY filter",expanded=True):
                    st.dataframe(df)
            if selected[0] == 'Offcampus':
                # paid = st.text_input('APPLY YOUR FILTER')
                # ser = st.button("search")
                # if ser:
                res = view_by_oncmapus(selected[0])
                df = pd.DataFrame(res,columns=['SRN','FirstName','LastName','Paid_NotPaid','CompnayName'])
                with st.expander("ONlY filter",expanded=True):
                    st.dataframe(df)
            if selected[0] == 'companyName':
                # paid = st.text_input('APPLY YOUR FILTER')
                # ser = st.button("search")
                # if ser:
                res = view_by_cname(selected[0])
                df = pd.DataFrame(res,columns=['SRN','FirstName','LastName','CompnayName'])
                with st.expander("ONlY filter",expanded=True):
                    st.dataframe(df)
            if selected[0] == 'yearOfGraduation':
                # paid = st.text_input('APPLY YOUR FILTER')
                # ser = st.button("search")
                # if ser:
                res = view_by_year(selected[0])
                df = pd.DataFrame(res,columns=['SRN','FirstName','LastName','yearOfGraduation'])
                with st.expander("ONlY filter",expanded=True):
                    st.dataframe(df)
            if selected[0] == 'marks':
                # marks = st.text_input('APPLY YOUR FILTER')
                # ser = st.button("Search")
                # if ser:
                res = view_by_marks(selected[0])
                df = pd.DataFrame(res,columns=['SRN','FirstName','LastName','Marks']) 
                with st.expander("ONlY filter",expanded=True):
                    st.dataframe(df)
        if len(selected)==2:
            if 'Paid' in selected and 'Incampus' in selected:
                # marks = st.text_input('APPLY YOUR FILTER')
                # ser = st.button("Search")
                # if ser:
                if selected[0] == 'Paid':
                    res = view_by_PaidIncampus(selected[0],selected[1])
                else: 
                    res = view_by_PaidIncampus2(selected[0],selected[1])
                df = pd.DataFrame(res,columns=['SRN','FirstName','LastName','Paid','Incampus']) 
                with st.expander("ONlY filter",expanded=True):
                    st.dataframe(df)
            if 'Paid' in selected and 'Offcampus' in selected:
                # marks = st.text_input('APPLY YOUR FILTER')
                # ser = st.button("Search")
                # if ser:
                res = view_by_PaidIncampus(selected[0],selected[0+1])
                df = pd.DataFrame(res,columns=['SRN','FirstName','LastName','Paid','Incampus']) 
                with st.expander("ONlY filter",expanded=True):
                    st.dataframe(df)
            if 'NotPaid' in selected and 'Incampus' in selected:
                # marks = st.text_input('APPLY YOUR FILTER')
                # ser = st.button("Search")
                # if ser:
                res = view_by_PaidIncampus(selected[0],selected[0+1])
                df = pd.DataFrame(res,columns=['SRN','FirstName','LastName','Paid','Incampus']) 
                with st.expander("ONlY filter",expanded=True):
                    st.dataframe(df)
            if 'NotPaid' in selected and 'Offcampus' in selected:
                # marks = st.text_input('APPLY YOUR FILTER')
                # ser = st.button("Search")
                # if ser:
                res = view_by_PaidIncampus(selected[0],selected[0+1])
                df = pd.DataFrame(res,columns=['SRN','FirstName','LastName','Paid','Incampus']) 
                with st.expander("ONlY filter",expanded=True):
                    st.dataframe(df)