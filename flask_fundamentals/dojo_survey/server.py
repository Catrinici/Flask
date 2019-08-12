from flask import Flask, render_template, request, redirect
app = Flask(__name__)

@app.route('/')
def index():
    return render_template("index.html")


@app.route('/results', methods=['POST'])
def users_info():
    name = request.form['name']
    location = request.form['location']
    language = request.form['language']
    comment = request.form['comment']
    
    return render_template('result.html')


@app.route('/return', methods=['POST'])
def gohome():
    return render_template('index.html')



if __name__=="__main__":
    app.run(debug=True)
