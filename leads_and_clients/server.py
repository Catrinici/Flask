from flask import Flask, render_template, redirect, request
from mysqlconnection import connectToMySQL
import plotly.graph_objects as go

app = Flask(__name__)

mysql = connectToMySQL('mydb')


@app.route('/')
def index():
    
    # all_clients = mysql.query_db("SELECT clients.first_name, clients.last_name FROM clients")

    mysql = connectToMySQL('lead_gen_business')
    all_clients = mysql.query_db("SELECT clients.first_name, clients.last_name, COUNT(leads.leads_id) AS leads FROM clients JOIN sites ON clients.client_id=sites.client_id JOIN leads ON sites.site_id=leads.site_id GROUP BY clients.first_name, clients.last_name")
    
    colors = ['gold', 'mediumturquoise', 'darkorange', 'lightgreen']
    fig = go.Figure(data=[go.Pie(labels=['clients.first_name'], values=['leads'])])
    fig.update_traces(hoverinfo='label+percent', textinfo='value', textfont_size=20,
                      marker=dict(colors=colors, line=dict(color='#000000', width=2)))
    fig.show()

    return render_template('index.html', clients = all_clients)




if __name__ == "__main__":
    app.run(debug=True)
