
from flask import Flask, render_template, request, redirect, session
app = Flask(__name__)
app.secret_key = 'ThisIsSecret'

@app.route('/')
def index():
    if 'visits' in session:
        session['visits'] = session.get('visits') + 1
    else:
        session['visits'] = 1
    return render_template('index.html')


@app.route('/increment', methods=['POST'])
def increment_by_two():
    session['visits'] += 1
    #We only increment by 1 since reloading the page also increments
    return redirect('/')


@app.route('/clear', methods=['POST'])
def clear():
    session['visits'] = 0
    return redirect('/')

if __name__=="__main__":
    app.run(debug=True)
