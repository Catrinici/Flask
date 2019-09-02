
from flask import Flask, render_template, redirect, request, session, flash
import re
from mysqlconnection import connectToMySQL
from flask_bcrypt import Bcrypt
app = Flask(__name__)
bcrypt = Bcrypt(app)
app.secret_key = "itslogintime"
EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')
NAME_REGEX = re.compile(r'^[a-zA-Z]+$')


@app.route('/')
def index():
    
    return render_template('index.html')



if __name__ == "__main__":
    app.run(debug=True)
