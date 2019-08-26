from flask import Flask, render_template, request, redirect, flash, session
from mysqlconnection import connectToMySQL    # import the function that will return an instance of a connection
import re	# the regex module
app = Flask(__name__)
app.secret_key = "super secret"

# create a regular expression object that we'll use later   
EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$') 

@app.route('/')
def index():
        if 'email' not in session:
                session['id'] = False
        return render_template('index.html')


@app.route('/process', methods=['POST'])
def submit():
        error = False
        session['id']= request.form['email']
        mysql = connectToMySQL('email_val')
        query = "SELECT email FROM email WHERE email = %(email)s;"
        data = {
                'email':request.form['email']
        }
        compare = mysql.query_db(query,data)
        print(compare)

        if not EMAIL_REGEX.match(request.form['email']):
                flash("Email input format is Invalid")
                error = True

        if len(compare) > 0:
                flash("Email already stored")
                error = True
        
        if error == True:
                return redirect('/')

        elif error == False:
                mysql = connectToMySQL('email_val')
                query = "INSERT INTO email (email, created_at) VALUES (%(email)s, NOW());"
                data = {
                        'email':request.form['email']
                }
                mysql.query_db(query,data)
                return redirect("/success")

@app.route("/success")
def result():
        mysql = connectToMySQL("email_val")
        emails = mysql.query_db("SELECT * FROM email")
        valid_email = session['id']

        return render_template("success.html",emails = emails, valid_email=valid_email)

if __name__ == "__main__":
        app.run(debug=True)