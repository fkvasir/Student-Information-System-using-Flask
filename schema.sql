-- Drop tables if they exist
DROP TABLE IF EXISTS student;
DROP TABLE IF EXISTS course;
DROP TABLE IF EXISTS college;

-- Create tables
CREATE TABLE college (
    collegeCode VARCHAR(5) PRIMARY KEY,
    collegeName VARCHAR(150) NOT NULL,
    createdAt DATETIME NOT NULL DEFAULT CURRENT_TIMESTAMP
);

CREATE TABLE course (
    courseCode VARCHAR(10) PRIMARY KEY,
    courseName VARCHAR(50) NOT NULL,
    college VARCHAR(5),
    FOREIGN KEY (college) REFERENCES college(collegeCode) ON UPDATE CASCADE ON DELETE CASCADE,
    createdAt DATETIME NOT NULL DEFAULT CURRENT_TIMESTAMP
);

CREATE TABLE student (
    studentID VARCHAR(9) PRIMARY KEY,
    studentFname VARCHAR(50) NOT NULL,
    studentLname VARCHAR(50) NOT NULL,
    course VARCHAR(10),
    year VARCHAR(8) NOT NULL,
    gender VARCHAR(6) NOT NULL,
    profile_picture VARCHAR(2048),
    FOREIGN KEY (course) REFERENCES course(courseCode) ON UPDATE CASCADE ON DELETE CASCADE,
    createdAt DATETIME NOT NULL DEFAULT CURRENT_TIMESTAMP
);
