from app import mysql

class Student(mysql.Model):
    studentID = mysql.Column(mysql.String(9), primary_key=True)
    studentFname = mysql.Column(mysql.String(50), nullable=False)
    studentLname = mysql.Column(mysql.String(50), nullable=False)
    course = mysql.Column(mysql.String(5), mysql.ForeignKey('course.courseCode', onupdate='CASCADE', ondelete='CASCADE'), nullable=False)
    year = mysql.Column(mysql.String(8), nullable=False)
    gender = mysql.Column(mysql.String(6), nullable=False)

    def __repr__(self):
        return f"<Student {self.studentID}>"
