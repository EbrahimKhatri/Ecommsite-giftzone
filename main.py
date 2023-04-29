

from ctypes import c_ssize_t
from pydoc import render_doc
from re import M, template

from flask_sqlalchemy import SQLAlchemy
from flask import Flask, render_template , request , redirect, url_for, session, Response
from datetime import datetime
import mysql.connector
from flask_mysqldb import MySQL
import MySQLdb.cursors
import re



app = Flask(__name__)
app.secret_key= 'your secret key'
app.config['MYSQL_HOST']= 'localhost'
app.config['MYSQL_USER']= 'root'
app.config['MYSQL_PASSWORD']= ''
app.config['MYSQL_DB']= ''
app.config["MYSQL_CURSORCLASS"]=""
mysql= MySQL(app)


@app.route("/min", methods= ['GET', 'POST'])
def mini():
    return render_template('foundpage.html')


@app.route("/important")
def imp():
       return render_template('mainpage.html')

@app.route("/shoes")
def viewp():
    return render_template('shoes.html')

@app.route("/headphone")
def headphone():
    return render_template('headphone.html')

@app.route("/contact")
def contact():
    return render_template('index.html')





@app.route("/tshirt")
def index():
    return render_template('tshirt.html')
app.run(debug=True)

@app.route("/per")
def perfume():
    return render_template('per.html')
app.run(debug=True)






@app.route("/mp")
def mp():
    return render_template('view.html' )
app.run(debug=True) 