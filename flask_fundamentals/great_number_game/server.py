from flask import Flask, render_template,request,redirect,session
import random
app = Flask(__name__)
app.secret_key = 'secret'


@app.route('/')
def index():
    if 'message' not in session:
        session["message"] = ""
    if 'number' not in session:
        session['number'] = random.randrange(1, 101)
    return render_template("index.html", message=session['message'])



@app.route('/guess', methods=['POST'])
def guess_num():
    input_num = int(request.form['number'])
    if input_num == session['number']:
        session['message'] = " You won! ## was the number!"
    if input_num > session['number']:
        session['message'] = "Too high!"
    elif input_num < session['number']:
        session['message'] = "Too low!"
        
    return redirect('/')


@app.route('/reset')
def reset():
    session['number']
    session.pop("number")
    session.pop("message")
    return redirect('/')



if __name__=="__main__":
    app.run(debug=True)
