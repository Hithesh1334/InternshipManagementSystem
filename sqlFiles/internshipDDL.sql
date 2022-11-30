/*STUDENT INTERNSHIP MANAGMENT SYSTEM*/

/*COMPANY TABLE*/
CREATE TABLE company
(
  cname VARCHAR(30) NOT NULL,
  Email VARCHAR(20) NOT NULL,
  PRIMARY KEY (cname)
);

/*COMPANY PHONE NUMBER TABLE*/
CREATE TABLE C_PhoneNO
(
  PhoneNO NUMERIC(12,0) ,
  cname VARCHAR(30) NOT NULL,
  PRIMARY KEY (PhoneNO, cname),
  FOREIGN KEY (cname) REFERENCES company(cname) on delete cascade on update cascade
);

/*COMPANY ADDRESS TABLE*/
CREATE TABLE c_address
(
  address VARCHAR(50) NOT NULL,
  cname VARCHAR(30) NOT NULL,
  PRIMARY KEY (address, cname),
  FOREIGN KEY (cname) REFERENCES company(cname)on delete cascade on update cascade
);

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

/*MANAGER PHONE NUMBER TABLE*/
CREATE TABLE M_PhoneNo
(
  PhoneNo NUMERIC(10,0) ,
  MSSN VARCHAR(15) NOT NULL,
  PRIMARY KEY (PhoneNo, MSSN),
  FOREIGN KEY (MSSN) REFERENCES Manager(MSSN) on delete cascade on update cascade
);


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


/*STUDNET PHONE NUMBER TABLE*/
CREATE TABLE S_phoneNo
(
  PhoneNo NUMERIC(10,0) ,
  SRN VARCHAR(15) NOT NULL,
  PRIMARY KEY (PhoneNo, SRN),
  FOREIGN KEY (SRN) REFERENCES Student_intern(SRN) on delete cascade on update cascade
);

/*STUDENT RESULT*/
CREATE TABLE Result
(
  marks INT CHECK (marks > 0) ,
  Grade CHAR(2) ,
  SRN VARCHAR(15) NOT NULL,
  PRIMARY KEY (SRN),
  FOREIGN KEY (SRN) REFERENCES Student_intern(SRN) on delete cascade on update cascade
);

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


/*STUDNET COMPANY TABLE*/
CREATE TABLE student_company
(
  SRN VARCHAR(15) NOT NULL,
  cname VARCHAR(30) NOT NULL,
  PRIMARY KEY (SRN, cname),
  FOREIGN KEY (SRN) REFERENCES Student_intern(SRN) on delete cascade on update cascade,
  FOREIGN KEY (cname) REFERENCES company(cname) on delete cascade on update cascade
);
