import re
from flask import Flask, render_template, request, redirect, session, flash
EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')
LETTER_REGEX = re.compile(r'[a-zA-Z]-[^0-9]')
app = Flask(__name__)
app.secret_key = 'KeepItSecretKeepItSafe'

@app.route('/')
def index():
    return render_template("index.html")


@app.route('/register', methods=['POST'])
def register():
    session['email'] = request.form['email']
    session['first_name'] = request.form['first_name']
    session['last_name'] = request.form['last_name']
    session['password'] = request.form['password']
    session['confirm_password'] = request.form['confirm_password']

    if len(request.form['email']) < 1:
        flash("Email cannot be blank!", 'email')
    elif not EMAIL_REGEX.match(request.form['email']):
        flash("Invalid Email Address!", 'email')
    if len(request.form['first_name']) < 1:
        flash("First Name cannot be blank!", 'first_name')
    if len(request.form['first_name']) <= 3:
        flash("Fisrt Name must be 3+ characters", 'first_name')
        
    if len(request.form['last_name']) < 1:
        flash("Last Name cannot be blank!", 'last_name')
    if len(request.form['last_name']) <= 3:
        flash("Last Name must be 3+ characters", 'last_name')

    if len(request.form['password']) < 1:
        flash("Password cannot be blank!", 'password')
    if len(request.form['password']) > 1 and len(request.form['password']) < 9:
        flash("The password is too short. It must be 8 characters log")
    if not request.form['password'] == request.form['confirm_password']:
        flash("Passwords dont match! Try again.")
    if '_flashes' in session.keys():
        return redirect("/")
    else:
        return render_template("success.html")

@app.route('/return', methods=['POST'])
def gohome():
    return render_template('index.html')







if __name__ == "__main__":
    app.run(debug=True)
