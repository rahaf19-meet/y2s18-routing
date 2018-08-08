from databases import *
from flask import Flask, render_template, url_for
app = Flask(__name__)

@app.route('/')
def home():
    return render_template("home.html")

@app.route('/hi/<string:name>/<int:num>')
def hello(name,num):
    return render_template("student.html",student_na=name, student_id=num)
app.run(debug=True)
