from flask import Flask, render_template, request, redirect, session, flash
app = Flask(__name__)
app.secret_key = 'KeepItSecretKeepItSafe'

@app.route('/')
def index():
    return render_template("index.html")


@app.route("/process", methods=['POST'])
def submit():
    if len(request.form['name']) < 1:
        flash("Name cannot be blank!", 'name')
    elif len(request.form['name']) <= 2:
        flash("Name must be 3+ characters", 'name')

    if len(request.form['comment']) < 1:
        flash("Comment cannot be blank!", 'comment')
    elif len(request.form['comment']) > 80:
        flash("Comment must be less than 80 characters", 'comment')

    if '_flashes' in session.keys():
        return redirect("/")
    else:
        return render_template('result.html')

@app.route('/return', methods=['POST'])
def gohome():
    return render_template('index.html')



if __name__=="__main__":
    app.run(debug=True)
