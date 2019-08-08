from flask import Flask
app = Flask(__name__)

@app.route('/')
def hello():
    return "Hello World!"

@app.route('/dojo')
def dojo():
    return "Dojo!"

@app.route('/say/<name>')
def say(name):
    return "Hi "+ name

@app.route('/repeat/<num>/<str>')
def repeat(num,str):
    print (int(num) * str)
    return int(num)* str





if __name__=="__main__":
    app.run(debug=True)
