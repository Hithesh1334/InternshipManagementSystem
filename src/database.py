import mysql.connector
import streamlit as st
mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    # password="password",
    database="internshipdatabase"
)
c = mydb.cursor()


#-------------------Insertion of data----------------------------------------------
def add_isinternat(startDate,EndDate,typeOfInternship,Paid_NotPaid,srn,cname):
    c.execute('INSERT INTO isinternat(startDate,EndDate,TypeOfInternships,Paid_NotPaid,srn,cname) VALUES (%s,%s,%s,%s,%s,%s)',(startDate,EndDate,typeOfInternship,Paid_NotPaid,srn,cname))
    mydb.commit()
    
def add_manager(Mssn,m_Fname,m_Lname,mEmail,cname):
    c.execute('INSERT INTO manager(MSSN,m_Fname,m_Lname,Email,cname) VALUES (%s,%s,%s,%s,%s)',(Mssn,m_Fname,m_Lname,mEmail,cname))
    mydb.commit()
    
def add_student_intern(srn,s_Fname,s_Lname,Email,yearOfGrad,Dob,Mssn,Gender):
    c.execute('INSERT INTO student_intern(SRN,s_Fname,s_Lname,Email,yearOfGraduation,DOB,MSSN,Gender) VALUES (%s,%s,%s,%s,%s,%s,%s,%s)',(srn,s_Fname,s_Lname,Email,yearOfGrad,Dob,Mssn,Gender))
    mydb.commit()
    
def add_company(cname,cEmail):
    c.execute('INSERT INTO company(cname,Email) VALUES (%s,%s)',(cname,cEmail))
    mydb.commit()
    
def add_sPhoneNo(srn,sPhone):
    c.execute('INSERT INTO s_phoneno(srn,PhoneNo) VALUES (%s,%s)',(srn,sPhone))
    mydb.commit()
    
def add_cPhoneNo(cname,cPhone):
    c.execute('INSERT INTO c_phoneno(cname,PhoneNo) VALUES (%s,%s)',(cname,cPhone))
    mydb.commit()
    
def add_result(srn,marks,Grade):
    c.execute('INSERT INTO result(srn,marks,Grade) VALUES (%s,%s,%s)',(srn,marks,Grade))
    mydb.commit()
    
def add_caddress(cname,caddress):
    c.execute('INSERT INTO c_address(cname,address) VALUES (%s,%s)',(cname,caddress))
    mydb.commit()
    

def add_mPhoneNo(Mssn,mPhone):
    c.execute('INSERT INTO m_phoneno(Mssn,PhoneNo) VALUES (%s,%s)',(Mssn,mPhone))
    mydb.commit()
    
def add_managerFeedback(q1,q2,q3,q4,q5,srn,Mssn):
    c.execute('INSERT INTO feedback(q_one,q_two,q_three,q_four,q_five,srn,MSSN) VALUES (%s,%s,%s,%s,%s,%s,%s)',(q1,q2,q3,q4,q5,srn,Mssn))
    mydb.commit()

def add_student_company(srn,cname):
    print('-----This is error--------',srn,cname)
    c.execute('INSERT INTO student_company(srn,cname) VALUES (%s,%s);',(srn,cname))
    mydb.commit()
    
#---------------------------------------update data----------------------------------------
# def get_data(srn):
#     c.execute('SELECT s_Fname,s_Lname,sp.phoneno,s.Email,s.Gender,s.yearOfGraduation,sm.marks,sm.Grade,s.DOB,c.cname,c.Email,cp.Phoneno,ca.address,m.MSSN,m.m_Fname,m.m_Lname,mp.Phoneno,m.Email,mf.feedback from student_intern s join s_phoneno sp on s.srn=sp.srn join result sm on s.srn=sm.srn join student_company sc on s.srn=sc.srn join company c on sc.cname=c.cname join c_address ca on c.cname=ca.cname join c_phoneno cp on c.cname=cp.cname join manager m on s.MSSN=m.MSSN join m_phoneno mp on m.MSSN=mp.MSSN join feedback mf on m.MSSN=mf.MSSN where s.srn="{}";'.format(srn))
#     data = c.fetchall()
    # 
    # return data
def update_studentFname_data(sFname,srn):
    er = c.execute('UPDATE student_intern SET s_Fname="{}" WHERE srn="{}";'.format(sFname,srn))
    print("This is er",er)
    mydb.commit()

#---------------------------------------View all data---------------------------------------
def view_student_info(srn):
    c.execute('SELECT s.srn,s_Fname,s_Lname,Email,p.PhoneNo,yearOfGraduation,Gender FROM student_intern s JOIN s_phoneno p ON s.srn=p.srn  WHERE s.srn="{}";'.format(srn))
    data = c.fetchall()
    return data
def view_StuComp_info(srn):
    c.execute('SELECT c.cname,c.email,a.address,p.PhoneNo FROM company c JOIN c_address a on c.cname=a.cname join c_phoneno p on c.cname=p.cname JOIN student_company sc ON c.cname=sc.cname join student_intern s on s.srn=sc.srn where s.srn="{}";'.format(srn))
    data = c.fetchall()
    return data
def view_StuManag_info(srn):
    c.execute(' SELECT m.MSSN,m_Fname,m_Lname,m.Email,p.PhoneNo FROM manager m JOIN m_phoneno p ON m.MSSN=p.MSSN JOIN student_intern s ON s.mssn=m.mssn WHERE s.srn="{}";'.format(srn))
    data = c.fetchall()
    return data
def view_StuInternship_info(srn):
    c.execute(' SELECT startDate,EndDate,TypeOfInternships,Paid_NotPaid FROM isinternat i JOIN student_intern s ON s.srn=i.srn WHERE s.srn="{}";'.format(srn))
    data = c.fetchall()
    return data
def view_all_data():
    c.execute('SELECT s.srn,s_Fname,s_Lname,Dob,Email,Gender,yearOfGraduation,r.marks,r.grade,p.phoneno FROM student_intern s JOIN s_phoneno p ON s.srn=p.srn JOIN  result r ON s.srn=r.srn ;')
    data = c.fetchall()
    return data
def delete_data(srn):
    c.execute('DELETE FROM student_intern WHERE srn="{}"'.format(srn))
    mydb.commit()

#-----------------------------------update--------------------------
# def view_tables():
#     c.execute('SELECT *FROM student_intern;')
#     data = c.fetchall()
#     return data
def view_only_srn():
    c.execute('SELECT srn FROM student_intern;')
    data = c.fetchall()
    return data
def get_table_data(srn):
    c.execute('SELECT * FROM student_intern WHERE srn="{}";'.format(srn))
    data = c.fetchall()
    return data
# def edit_data(new_srn,new_Fname,new_Lname,new_dob,new_Email,new_Gender,new_yearOfGraduation,selected_data):
#     c.execute('UPDATE student_intern SET s_Fname="{}",s_Lname="{}",dob="{}",Email="{}",Gender="{}",yearOfGraduation="{}" where srn="{}";'.format(new_srn,new_Fname,new_Lname,new_dob,new_Email,new_Gender,new_yearOfGraduation,selected_data))
# #     print("before  commit")
#     mydb.commit()
#     print("after commit")

def edit_data(new_Fname,new_Lname,new_dob,new_Email,new_Gender,new_yearOfGraduation,selected_data):
    c.execute('UPDATE student_intern SET s_Fname="{}", s_Lname="{}", dob="{}", Email="{}",Gender="{}",yearOfGraduation="{}" where srn="{}";'.format(new_Fname,new_Lname,new_dob,new_Email,new_Gender,new_yearOfGraduation,selected_data))
#     print("before  commit")
    mydb.commit()

def view_only_cname(srn):
    c.execute('SELECT c.cname FROM company c JOIN student_company sc on c.cname=sc.cname join student_intern s on s.srn=sc.srn  where s.srn="{}" ;'.format(srn))
    data = c.fetchone()
    return data

def get_company_data(cname):
    c.execute('SELECT cname,Email FROM company where cname="{}";'.format(cname))
    data  = c.fetchall()
    return data
def edit_company_data(cemail,cname):
    c.execute('UPDATE company SET Email="{}" WHERE cname="{}";'.format(cemail,cname))
    mydb.commit()

def view_only_manager(srn):
    c.execute('SELECT m.mssn,m_Fname,m_Lname,m.email from manager m join student_intern s on m.mssn=s.mssn where s.srn="{}";'.format(srn))
    data = c.fetchall()
    return data
def edit_manager_data(new_m_Fname,new_m_Lname,new_mEmail,new_mssn):
    c.execute('UPDATE manager SET m_Fname="{}", m_Lname="{}",Email="{}" where mssn="{}";'.format(new_m_Fname,new_m_Lname,new_mEmail,new_mssn))
    mydb.commit()

def view_only_internship(srn):
    c.execute('SELECT startDate,EndDate,TypeOfInternships,Paid_NotPaid from isinternat i join student_intern s on s.srn=i.srn where s.srn="{}";'.format(srn))
    data = c.fetchall()
    return data
def edit_internship_data(new_startDate, new_EndDate, new_TypeOfInternships,new_Paid_NotPaid,srn,cname):
    c.execute('UPDATE isinternat SET startDate="{}",EndDate="{}",TypeOfInternships="{}",Paid_NotPaid="{}" where srn="{}" and cname="{}";'.format(new_startDate, new_EndDate, new_TypeOfInternships,new_Paid_NotPaid,srn,cname))
    mydb.commit()
# ------------------------------------------------------------------------------










#---------------------------------sql query-------------------------------------
def sql(query):
    # print("THe is  a sql query",query)
    res = []
    for i in range(len(query)-1):
        # print("this is a query",query[i])
        c.execute('{};'.format(query[i]))
        data = c.fetchall()
        # print(data)
        res.append(data)
        # print("This is res",res)
    mydb.commit ()
    # 
    return res

#-------------------------------------aggregate query-----------------------------
def count_studentIntern(tablename):
    c.execute('SELECT count(*) FROM {};'.format(tablename))
    data = c.fetchall()
    return data
def count_company(tablename):
    c.execute('SELECT count(*) FROM {};'.format(tablename))
    data = c.fetchall()
    return data
def count_manager(tablename):
    c.execute('SELECT count(*) FROM {};'.format(tablename))
    data = c.fetchall()
    return data
def count_internshipinfo(tablename):
    c.execute('SELECT count(*) FROM {};'.format(tablename))
    data = c.fetchall()
    return data
def count_paidIncampus(tablename):
    c.execute('SELECT count(*) FROM {} where Paid_NotPaid="Paid" AND typeOfInternships="Incampus";'.format(tablename))
    data = c.fetchall()
    return data
def count_paidOffcampus(tablename):
    c.execute('SELECT count(*) FROM {} where Paid_NotPaid="Paid" AND typeOfInternships="offcampus";'.format(tablename))
    data = c.fetchall()
    return data
def count_notpaid_Incampus(tablename):
    c.execute('SELECT count(*) FROM {} where Paid_NotPaid="NotPaid" AND typeOfInternships="Incampus";'.format(tablename))
    data = c.fetchall()
    return data
def count_notpaid_Offcampus(tablename):
    c.execute('SELECT count(*) FROM {} where Paid_NotPaid="NotPaid" AND typeOfInternships="Offcampus";'.format(tablename))
    data = c.fetchall()
    return data

def data_upload(sqlq):
    c.execute('{}'.format(sqlq))
    mydb.commit()

def if_srn_exists(srn):
    c.execute('SELECT s.srn,s.s_Fname,s.s_Lname from student_intern s where EXISTS(select srn from student_intern where srn="{}");'.format(srn))
    data = c.fetchall()
    return data

# ----------------------------------------read2------------------------------------
def view_by_Paid(ans):
    c.execute('SELECT srn,s_Fname,s_Lname,Paid_NotPaid,cname from student where Paid_NotPaid="{}";'.format(ans))
    data = c.fetchall()
    return data
def view_by_marks(ans):
    c.execute('SELECT srn,s_Fname,s_Lname,marks from studentmarks where marks>="{}";'.format(ans))
    data = c.fetchall()
    return data
def view_by_oncmapus(ans):
    c.execute('SELECT srn,s_Fname,s_Lname,TypeOfInternships,cname from student where TypeOfInternships="{}";'.format(ans))
    data = c.fetchall()
    return data
def view_by_cname(ans):
    c.execute('SELECT s.srn,s.s_Fname,s.s_Lname,c.cname from student_company sc join student_intern s on s.srn=sc.srn join company c on sc.cname=c.cname where c.cname="{}"; '.format(ans))
    data = c.fetchall()
    return data
def view_by_year(ans):
    c.execute('SELECT s.srn,s.s_Fname,s.s_Lname,s.yearOfGraduation from student_intern s where yearOfGraduation="{}";'.format(ans))
    data = c.fetchall()
    return data
def view_by_PaidIncampus(ans1,ans2):
    c.execute('SELECT srn,s_Fname,s_Lname,Paid_NotPaid,TypeOfInternships from student where Paid_NotPaid="{}" and typeOfInternships="{}";'.format(ans1,ans2))
    data = c.fetchall()
    return data
def view_by_PaidIncampus2(ans1,ans2):
    c.execute('SELECT srn,s_Fname,s_Lname,Paid_NotPaid,TypeOfInternships from student where typeOfInternships="{}" and Paid_NotPaid="{}";'.format(ans1,ans2))
    data = c.fetchall()
    return data

def view_result_info(srn):
    c.execute('SELECT q_one,q_two,q_three,q_four,q_five,marks,Grade from studentmarks where srn="{}";'.format(srn))
    data = c.fetchall()
    return data

def view_only_result(srn):
    c.execute('SELECT marks,Grade from result where srn="{}";'.format(srn))
    data = c.fetchall()
    return data   
def edit_result_data(new_marks,new_grade,srn):
    c.execute('UPDATE result SET marks="{}",Grade="{}" where srn="{}";'.format(new_marks,new_grade,srn))
    mydb.commit() 

def view_only_feedback(srn):
    c.execute('SELECT q_one,q_two,q_three,q_four,q_five from feedback where srn="{}";'.format(srn))
    data = c.fetchall() 
    return data

def edit_feedback_data(new_qOne,new_qTwo,new_qThree,new_qFour,new_qFive,srn):
    c.execute('UPDATE feedback SET q_one="{}",q_two="{}",q_three="{}",q_four="{}",q_five="{}" where srn="{}";'.format(new_qOne,new_qTwo,new_qThree,new_qFour,new_qFive,srn))
    data = c.fetchall()
    return data

