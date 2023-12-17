from app import mysql

class Course(mysql.Model):
    courseCode = mysql.Column(mysql.String(5), primary_key=True)
    courseName = mysql.Column(mysql.String(50), nullable=False)
    college = mysql.Column(mysql.String(5), mysql.ForeignKey('college.collegeCode', onupdate='CASCADE', ondelete='CASCADE'), nullable=False)

    def __repr__(self):
        return f"<Course {self.courseCode}>"
