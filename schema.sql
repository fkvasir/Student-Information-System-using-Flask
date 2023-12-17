DROP TABLE IF EXISTS college;
CREATE TABLE college (
    collegeCode VARCHAR(5) PRIMARY KEY,
    collegeName VARCHAR(150) NOT NULL
);


DROP TABLE IF EXISTS course;
CREATE TABLE course (
    courseCode VARCHAR(5) PRIMARY KEY,
    courseName VARCHAR(50) NOT NULL,
    college VARCHAR(5),
    FOREIGN KEY (college) REFERENCES college(collegeCode) ON UPDATE CASCADE ON DELETE CASCADE
);


DROP TABLE IF EXISTS student;
CREATE TABLE student (
    studentID VARCHAR(9) PRIMARY KEY,
    studentFname VARCHAR(50) NOT NULL,
    studentLname VARCHAR(50) NOT NULL,
    course VARCHAR(5),
    year VARCHAR(8) NOT NULL,
    gender VARCHAR(6) NOT NULL,
    FOREIGN KEY (course) REFERENCES course(courseCode) ON UPDATE CASCADE ON DELETE CASCADE
);
