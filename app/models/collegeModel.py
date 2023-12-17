from app import mysql

class College(mysql.Model):
    id = mysql.Column(mysql.Integer, primary_key=True)
    collegeCode = mysql.Column(mysql.String(5), unique=True, nullable=False)
    collegeName = mysql.Column(mysql.String(150), nullable=False)

    def __repr__(self):
        return f"<College {self.collegeCode}>"
