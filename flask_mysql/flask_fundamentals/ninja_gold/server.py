from flask import Flask, render_template, redirect, request, session, flash
import re
from mysqlconnection import connectToMySQL
from flask_bcrypt import Bcrypt
from time import strftime, localtime

app = Flask(__name__)
bcrypt = Bcrypt(app)
app.secret_key = "super secret"
EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')
NAME_REGEX = re.compile(r'^[a-zA-Z]+$')

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/process_money', methods=['POST'])
def money():
    return redirect('/')


if __name__ == "__main__":
    app.run(debug=True)