import streamlit as st 
from database import sql


def query():
    st.code('You can execute your sql query here \nYou can execute more than one query at once \nfor Example: \n--SELECT *from tablename;\n--UPDATE tablename SET statment WHERE condition;\n--DELETE FROM tablename WHERE conditons;\nYou can start with\n--SHOW TABLES; ' )

    query = st.text_area("🤖 Enter your Sql command:")
    if st.button("Execute"):
        query = query.split(";")
        data = sql(query)
        print(data)
        for i in range(len(data)):
            # print("This is data[i]",data)
            st.table(data[i])
        # st.write(table)
    