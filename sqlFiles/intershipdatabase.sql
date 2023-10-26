/*STUDENT INTERNSHIP MANAGMENT SYSTEM*/

/*COMPANY TABLE*/
CREATE TABLE company
(
  cname VARCHAR(30) NOT NULL,
  Email VARCHAR(20) NOT NULL,
  PRIMARY KEY (cname)
);

/*-INSET VALUES FOR COMPANY INFORMATION-*/

INSERT INTO company(cname,Email) VALUES('JP MORGAN','jpmorgan@gmail.com'),('GOLDMAN SACHS','goldmansacks@gmail.com'),('MORGAN STANLEY','morganstanley@gamil.com'),('ATLASSIAN','atlassian@gmail.com'),('ADOBE','adobe@gmail.com'),('GIGSKY','giksky@gmail.com'),('CISCO','cisco@gmail.com'),('PAYPAL','paypal@gmail.com');

/*-------------------------------------------------------------*/

/*COMPANY PHONE NUMBER TABLE*/
CREATE TABLE C_PhoneNO
(
  PhoneNO NUMERIC(12,0) ,
  cname VARCHAR(30) NOT NULL,
  PRIMARY KEY (PhoneNO, cname),
  FOREIGN KEY (cname) REFERENCES company(cname) on delete cascade on update cascade
);

/*-INSET VALUES FOR COMPANY PHONEnO INFORMATION-*/

INSERT INTO C_PhoneNO(cname,PhoneNo) VALUES('JP MORGAN',2122706000),('GOLDMAN SACHS',08041271600),('MORGAN STANLEY',08061041000)
,('ATLASSIAN',08037012649),('ADOBE',08041939500)
,('GIGSKY',08041648199),('CISCO',8041593000),('PAYPAL',6288956221);

/*-------------------------------------------------------------*/

/*COMPANY ADDRESS TABLE*/
CREATE TABLE c_address
(
  address VARCHAR(50) NOT NULL,
  cname VARCHAR(30) NOT NULL,
  PRIMARY KEY (address, cname),
  FOREIGN KEY (cname) REFERENCES company(cname)on delete cascade on update cascade
);

/*-INSET VALUES FOR COMPANY ADDRESS INFORMATION-*/

INSERT INTO c_address(cname,address) VALUES ('JP MORGAN','Prestige Tech Park Banglore'),('GOLDMAN SACHS','HELIOS BUSINESS Park Banglore'),('MORGAN STANLEY','MARATHALLII OUTER RING ROAD Banglore'),('ATLASSIAN','EMBASSY GOLF LINKS BUSINESS PARK Banglore'),('ADOBE','Prestige Tech Park Banglore'),('GIGSKY','TIPPASANDRA Banglore'),('CISCO','M.G.ROAD Banglore'),('PAYPAL','RGA TECH Park Banglore');

/*-------------------------------------------------------------*/

/*MANAGER TABLE*/
CREATE TABLE Manager
(
  MSSN VARCHAR(15) NOT NULL,
  m_Fname VARCHAR(15) NOT NULL,
  m_Lname VARCHAR(15) ,
  Email VARCHAR(20) NOT NULL,
  cname VARCHAR(30) ,
  PRIMARY KEY (MSSN),
  FOREIGN KEY (cname) REFERENCES company(cname) on delete cascade on update cascade
);

/*-INSET VALUES FOR MANAGER INFORMATION-*/

INSERT INTO Manager(MSSN,m_Fname,m_Lname,Email,cname) VALUES
('222-11-3333','Jamie','Dimon','jamie@gamil.com','JP MORGAN'),
('525-11-3344','David','M','david@gamil.com','GOLDMAN SACHS'),
('982-61-0123','James','P','james@gamil.com','MORGAN STANLEY'),
('841-57-7393','Rajeev','Ranjan','rajeev@gamil.com','ATLASSIAN'),
('111-22-3333','Shantanu','Narayen','shantanu@gamil.com','ADOBE'),
('482-71-5073','Ravi','Rishy','ravi@gamil.com','GIGSKY'),
('264-19-8431','Chuck','Robbins','chuck@gamil.com','CISCO'),
('792-55-3639','San','Jose','san@gamil.com','PAYPAL');
/*-------------------------------------------------------------*/


/*MANAGER PHONE NUMBER TABLE*/
CREATE TABLE M_PhoneNo
(
  PhoneNo NUMERIC(10,0) ,
  MSSN VARCHAR(15) NOT NULL,
  PRIMARY KEY (PhoneNo, MSSN),
  FOREIGN KEY (MSSN) REFERENCES Manager(MSSN) on delete cascade on update cascade
);

/*-INSET VALUES FOR MANAGER PHONEno INFORMATION-*/

INSERT INTO M_PhoneNO(MSSN,PhoneNO) VALUES('222-11-3333',7532965244),('525-11-3344',9876965244),('982-61-0123',6332965852),('841-57-7393',9642965542),('111-22-3333',8332965257),('482-71-5073',8932764252),('264-19-8431',9932775241),('792-55-3639',6632205278);

/*-------------------------------------------------------------*/


/*STUDENT INTERN TABLE*/
CREATE TABLE Student_intern
(
  SRN VARCHAR(15) NOT NULL,
  s_Fname VARCHAR(15) NOT NULL,
  s_Lname VARCHAR(15) ,
  DOB DATE ,
  Email VARCHAR(30) NOT NULL,
  Gender VARCHAR(10) ,
  yearOfGraduation NUMERIC(4,0) ,
  MSSN VARCHAR(15) NOT NULL,
  PRIMARY KEY (SRN),
  FOREIGN KEY (MSSN) REFERENCES Manager(MSSN) on delete cascade on update cascade
);

/*-INSET VALUES FOR STUDENT INFORMATION-*/

INSERT INTO Student_intern(SRN,s_Fname,s_Lname,DOB,Email,Gender,yearOfGraduation,MSSN) VALUES('PES1UG20CS100','Mike','k','2002/03/23','mike123@gmail.com','male',2024,'222-11-3333'),('PES1UG20CS200','Suraj','s','2002/07/05','suraj@gmail.com','male',2024,'525-11-3344'),('PES1UG20CS300','Sajay','Murthy','2002/11/13','sanjay@gmail.com','male',2024,'982-61-0123'),('PES1UG20CS400','Nikhil','M','2002/08/04','nikhil@gmail.com','male',2024,'841-57-7393'),('PES1UG20CS250','Vibha','M','2001/06/28','vibha@gmail.com','female',2023,'111-22-3333'),('PES1UG20CS350','xyz','qw','2001/11/20','xyz@gmail.com','female',2024,'482-71-5073'),('PES1UG20CS450','Nischay','Kumar','2002/01/30','nischay@gmail.com','male',2024,'264-19-8431'),('PES1UG20CS164','Hitesh','Bishnoi','2002/11/18','hiteshb@gmail.com','male',2024,'792-55-3639'),('PES1UG20CS140','Chirag','G','2002/08/23','chirag@gmail.com','male',2024,'841-57-7393'),('PES1UG20CS151','Gautham','R A','2002/08/15','gautam@gmail.com','male',2024,'482-71-5073');

/*-------------------------------------------------------------*/



/*STUDENT INTERNSHIP TABLE*/
CREATE TABLE isInternAt
(
  startDate DATE ,
  EndDate DATE ,
  TypeOfInternships VARCHAR(20) ,
  Paid_NotPaid VARCHAR(5) ,
  SRN VARCHAR(15) NOT NULL,
  cname VARCHAR(30) NOT NULL,
  PRIMARY KEY (SRN, cname),
  FOREIGN KEY (SRN) REFERENCES Student_intern(SRN)on delete cascade,
  FOREIGN KEY (cname) REFERENCES company(cname) on delete cascade on update cascade
);

/*-INSET VALUES FOR INTERNSHIP INFORMATION-*/
INSERT INTO isInternAt(startDate,EndDate,TypeOfInternships,Paid_NotPaid,SRN,cname) VALUES('2022/01/06','2022/07/31','Incampus','Paid','PES1UG20CS100','JP MORGAN'),('2022/01/06','2022/07/31','Incampus','Paid','PES1UG20CS200','GOLDMAN SACHS'),('2022/01/06','2022/07/31','Incampus','Paid','PES1UG20CS300','MORGAN STANLEY'),('2022/01/06','2022/07/31','Incampus','Paid','PES1UG20CS400','ATLASSIAN'),('2022/01/06','2022/07/31','Incampus','Paid','PES1UG20CS250','ADOBE'),('2022/01/06','2022/07/31','Incampus','Paid','PES1UG20CS350','GIGSKY'),('2022/01/06','2022/07/31','Incampus','Paid','PES1UG20CS450','CISCO'),('2022/01/06','2022/07/31','Incampus','Paid','PES1UG20CS164','PAYPAL'),('2022/01/06','2022/07/31','Incampus','Paid','PES1UG20CS140','CISCO'),('2022/01/06','2022/07/31','Incampus','Paid','PES1UG20CS151','GIGSKY');

/*-------------------------------------------------------------*/

/*STUDNET PHONE NUMBER TABLE*/
CREATE TABLE S_phoneNo
(
  PhoneNo NUMERIC(10,0) ,
  SRN VARCHAR(15) NOT NULL,
  PRIMARY KEY (PhoneNo, SRN),
  FOREIGN KEY (SRN) REFERENCES Student_intern(SRN) on delete cascade on update cascade
);

/*-INSET VALUES FOR STUDENT PHONEnO INFORMATION-*/

INSERT INTO S_phoneNO(SRN,PhoneNO) VALUES('PES1UG20CS100',933675543),('PES1UG20CS200',9008675543),('PES1UG20CS300',9188675543),('PES1UG20CS400',9198675543),('PES1UG20CS250',9098675543),('PES1UG20CS350',9398675543),('PES1UG20CS450',9998675543),('PES1UG20CS164',9898675543),('PES1UG20CS140',9698675543),('PES1UG20CS151',9298675543);

/*-------------------------------------------------------------*/

/*STUDENT RESULT*/
CREATE TABLE Result
(
  marks INT CHECK (marks > 0) ,
  Grade CHAR(2) ,
  SRN VARCHAR(15) NOT NULL,
  PRIMARY KEY (SRN),
  FOREIGN KEY (SRN) REFERENCES Student_intern(SRN) on delete cascade on update cascade
);

/*-INSET VALUES FOR STUDENT RESULT INFORMATION-*/

INSERT INTO Result(SRN,Marks,Grade) VALUES('PES1UG20CS100',45,'S');
INSERT INTO Result(SRN,Marks,Grade) VALUES('PES1UG20CS200',40,'S');
INSERT INTO Result(SRN,Marks,Grade) VALUES('PES1UG20CS300',39,'A');
INSERT INTO Result(SRN,Marks,Grade) VALUES('PES1UG20CS400',35,'A');
INSERT INTO Result(SRN,Marks,Grade) VALUES('PES1UG20CS250',47,'S');
INSERT INTO Result(SRN,Marks,Grade) VALUES('PES1UG20CS350',40,'S');
INSERT INTO Result(SRN,Marks,Grade) VALUES('PES1UG20CS450',38,'A');
INSERT INTO Result(SRN,Marks,Grade) VALUES('PES1UG20CS164',39,'A');
INSERT INTO Result(SRN,Marks,Grade) VALUES('PES1UG20CS140',39,'A');
INSERT INTO Result(SRN,Marks,Grade) VALUES('PES1UG20CS151',39,'A');

/*-------------------------------------------------------------*/


/*MANAGER FEEDBACK*/
CREATE TABLE feedback
(
  q_one int ,
  q_two int ,
  q_three int ,
  q_four int ,
  q_five int ,
  MSSN VARCHAR(15) NOT NULL,
  SRN VARCHAR(15) NOT NULL,
  PRIMARY KEY (MSSN, SRN),
  FOREIGN KEY (MSSN) REFERENCES Manager(MSSN) on delete cascade on update cascade,
  FOREIGN KEY (SRN) REFERENCES Student_intern(SRN) on delete cascade on update cascade
);

/*-INSET VALUES FOR STUDENT FEEDBACK INFORMATION-*/

INSERT INTO feedback(SRN,MSSN,q_one,q_two,q_three,q_four,q_five) VALUES('PES1UG20CS100','222-11-3333',10,10,9,9,7);
INSERT INTO feedback(SRN,MSSN,q_one,q_two,q_three,q_four,q_five) VALUES('PES1UG20CS200','525-11-3344',8,7,9,9,7);
INSERT INTO feedback(SRN,MSSN,q_one,q_two,q_three,q_four,q_five) VALUES('PES1UG20CS300','982-61-0123',8,7,7,9,7);
INSERT INTO feedback(SRN,MSSN,q_one,q_two,q_three,q_four,q_five) VALUES('PES1UG20CS400','841-57-7393',7,7,7,8,7);
INSERT INTO feedback(SRN,MSSN,q_one,q_two,q_three,q_four,q_five) VALUES('PES1UG20CS250','111-22-3333',10,10,8,10,7);
INSERT INTO feedback(SRN,MSSN,q_one,q_two,q_three,q_four,q_five) VALUES('PES1UG20CS350','482-71-5073',8,7,9,9,7);
INSERT INTO feedback(SRN,MSSN,q_one,q_two,q_three,q_four,q_five) VALUES('PES1UG20CS450','264-19-8431',7,7,8,9,7);
INSERT INTO feedback(SRN,MSSN,q_one,q_two,q_three,q_four,q_five) VALUES('PES1UG20CS164','792-55-3639',10,10,6,6,7);
INSERT INTO feedback(SRN,MSSN,q_one,q_two,q_three,q_four,q_five) VALUES('PES1UG20CS140','841-57-7393',10,10,6,6,7);
INSERT INTO feedback(SRN,MSSN,q_one,q_two,q_three,q_four,q_five) VALUES('PES1UG20CS151','482-71-5073',10,10,6,6,7);

/*-------------------------------------------------------------*/

/*STUDNET COMPANY TABLE*/
CREATE TABLE student_company
(
  SRN VARCHAR(15) NOT NULL,
  cname VARCHAR(30) NOT NULL,
  PRIMARY KEY (SRN, cname),
  FOREIGN KEY (SRN) REFERENCES Student_intern(SRN) on delete cascade on update cascade,
  FOREIGN KEY (cname) REFERENCES company(cname) on delete cascade on update cascade
);

/*-INSERT VALUES FOR STUDENT COMPANY INFORMATION-*/

INSERT INTO student_company(srn,cname) VALUES('PES1UG20CS100','JP MORGAN');
INSERT INTO student_company(srn,cname) VALUES('PES1UG20CS200','GOLDMAN SACHS');
INSERT INTO student_company(srn,cname) VALUES('PES1UG20CS300','MORGAN STANLEY');
INSERT INTO student_company(srn,cname) VALUES('PES1UG20CS400','ATLASSIAN');
INSERT INTO student_company(srn,cname) VALUES('PES1UG20CS250','ADOBE');
INSERT INTO student_company(srn,cname) VALUES('PES1UG20CS350','GIGSKY');
INSERT INTO student_company(srn,cname) VALUES('PES1UG20CS450','CISCO');
INSERT INTO student_company(srn,cname) VALUES('PES1UG20CS164','PAYPAL');
INSERT INTO student_company(srn,cname) VALUES('PES1UG20CS140','CISCO');
INSERT INTO student_company(srn,cname) VALUES('PES1UG20CS151','GIGSKY');
/*-------------------------------------------------------------*/
