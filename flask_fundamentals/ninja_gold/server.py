import time
from flask import Flask, render_template, request, redirect, session
app = Flask(__name__)
app.secret_key = 'ThisIsSecret'
import random


@app.route('/')
def index():
    if 'gold' not in session:
        session['total'] = 0
    if 'activity' not in session:
        session['activity'] = []

    return render_template("index.html", total=session['total'], activities=session['activity'])


@app.route('/process_money', methods=['POST'])
def process():
    farm_money = random.randint(10, 21)
    cave_money = random.randint(5, 11)
    house_money = random.randint(2, 6)
    casino_money = random.randint(-50, 51)
    timestamp = time.strftime('%Y-%m-%d %H:%M %p')
    message = ""

    if request.form['building'] == 'farm':
        session['total'] += farm_money
        session['activity'].append('Earned  ' + str(farm_money) + " golds from the farm" + "("+timestamp +")")
        
    if request.form['building'] == 'cave':
        session['total'] += cave_money
        session['activity'].append(
            'Earned: ' + str(cave_money) + " golds from the cave" + "("+ timestamp + ")")

    if request.form['building'] == 'house':
        session['total'] += house_money
        session['activity'].append(
            'Earned: ' + str(house_money) + " golds from the house" + "("+ timestamp + ")")

    if request.form['building'] == 'casino':
        if casino_money < 0:
            session['activity'].append(
                'Entered a casino and lost ' + str(casino_money) + " golds... Ouch." + "("+ timestamp + ")")
            session['total'] += casino_money
            if session['total'] <=0:
                session['total'] = 0
                message = "You Lost all your money! You can not play at the casino anymore!"
                
        if casino_money >= 0:
            session['total'] += casino_money
            session['activity'].append(
                'Entered a casino and earned ' + str(casino_money) + " golds. Nice!" + "("+ timestamp + ")")
    return render_template("index.html", total=session['total'], activities = session['activity'], message=message)


@app.route('/reset', methods=['POST'])
def reset():
    session['total']=0
    session['activity']=[]
    return redirect('/')


if __name__=="__main__":
    app.run(debug=True)
