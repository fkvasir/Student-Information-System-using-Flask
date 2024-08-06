from flask import Flask, render_template, request, redirect, url_for
from flask_mysql_connector import MySQL
from flask_bootstrap import Bootstrap
from config import DB_USERNAME, DB_PASSWORD, DB_NAME, DB_HOST, SECRET_KEY
from flask_wtf.csrf import CSRFProtect
import cloudinary
import cloudinary.uploader
import cloudinary.api
import os

mysql = MySQL()
bootstrap = Bootstrap()


def create_app():
    app = Flask(__name__, instance_relative_config=True)


    app.config.from_mapping(
        SECRET_KEY=SECRET_KEY,
        MYSQL_USER=DB_USERNAME,
        MYSQL_PASSWORD=DB_PASSWORD,
        MYSQL_DATABASE=DB_NAME,
        MYSQL_HOST=DB_HOST,
    )
    bootstrap.init_app(app)
    mysql.init_app(app)
    CSRFProtect(app)

    from .controller.colleges import colleges
    from .controller.courses import courses
    from .controller.students import students


    app.register_blueprint(colleges)
    app.register_blueprint(courses)
    app.register_blueprint(students)



    return app




