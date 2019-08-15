from flask import Flask, render_template, request, redirect, session
app = Flask(__name__)
app.secret_key = 'ThisIsSecret'

@app.route('/')
def index():
    return render_template("index.html")


@app.route('/process_money', methods=['POST'])
def process():
    gold = 0

    return redirect("/")

if __name__=="__main__":
    app.run(debug=True)
