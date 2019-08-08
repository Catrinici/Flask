from flask import Flask, render_template
app = Flask(__name__)

@app.route('/play/<times>')
def add_box(times):
    return render_template('index.html', times=int(times))

@app.route('/play/<times>/<color>')
def change_color(times,color):
    return render_template('index.html', times=int(times), color=color)

if __name__=="__main__":
    app.run(debug=True)
