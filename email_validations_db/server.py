from flask import Flask, render_template, request, redirect,flash
import re
from mysqlconnection import connectToMySQL
from flask_bcrypt import Bcrypt
emailRegex = re.compile(r'^[a-zA-Z0-9\.\+_-]+@[a-zA-Z0-9\._-]+\.[a-zA-Z]*$')

app = Flask(__name__)
bcrypt = Bcrypt(app)  
app.secret_key = "afalnvnrivinroiberv"
mysql = connectToMySQL('mydb')


@app.route('/')
def index():
    # mysql = connectToMySQL('user_dash')
    
    return render_template('index.html')

@app.route('/create', methods=["POST"])
def create():
    mysql = connectToMySQL('emails')
    if len(request.form['email']) < 1:
        flash("email cannot be blank")
    elif not emailRegex.match(request.form['email']):
        flash("Email is invalid!")
    
    else:
        query = ("INSERT INTO users (users.email, created_at, updated_at) " +
                 "VALUES (%(email)s, NOW(), NOW())")
        print (request.form['email'])
        data = {
            'email':request.form['email']
        }
        all_users = mysql.query_db("SELECT * FROM users")
        print(all_users)
        return render_template('success.html',users=all_users)
    return redirect('/')





if __name__ == "__main__":
    app.run(debug=True)
