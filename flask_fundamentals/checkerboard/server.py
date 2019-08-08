from flask import Flask, render_template
app = Flask(__name__)

@app.route('/')
def index():
    return render_template("index.html")

@app.route('/<x>/<y>')
def index(num1,num2):
    return render_template("index.html", num1=int(x), num2=int(y))

if __name__=="__main__":
    app.run(debug=True)
