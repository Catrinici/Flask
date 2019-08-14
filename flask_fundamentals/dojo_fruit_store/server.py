from flask import Flask, render_template, request, redirect
import time
app = Flask(__name__)  

@app.route('/')         
def index():
    return render_template("index.html")

@app.route('/checkout', methods=['POST'])         
def checkout():
    print(request.form)
    print(int(request.form["strawberry"]))
    sum = int(request.form["strawberry"]) + \
        int(request.form["raspberry"]) + int(request.form["apple"])
    timestamp = time.strftime('%A %B, %d %Y %H:%M')
    
    return render_template("checkout.html", sum=sum, timestamp=timestamp)

@app.route('/fruits')         
def fruits():
    return render_template("fruits.html")

if __name__=="__main__":   
    app.run(debug=True)    
