from flask import Flask, request, redirect, render_template
import cgi
import os


app = Flask(__name__)
app.config['DEBUG'] = True

@app.route("/")
def index():
    return render_template('signup.html', title="Signup Form")

@app.route("/hello", methods=['POST'])
def hello():
    first_name = request.form['first_name']
    return '<h1>Hello, ' + first_name + '</h1>'

app.run()