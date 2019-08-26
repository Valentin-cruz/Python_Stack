from flask import Flask, render_template, request, redirect, flash, session
from mysqlconnection import connectToMySQL    # import the function that will return an instance of a connection
import re	# the regex module
from flask_bcrypt import Bcrypt
app = Flask(__name__)
bcrypt = Bcrypt(app)
app.secret_key = "super secret"

# create a regular expression object that we'll use later   
EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$') 
NAME_REGEX = re.compile(r'^[a-zA-Z]+$')

@app.route('/')
def index():
    if 'id' not in session:
        session['id'] = False
    return render_template('index.html')

@app.route('/register', methods=["POST"])
def register_val():
    error = False
    mysql = connectToMySQL('login_reg')
    query = "SELECT * FROM user WHERE email = %(email)s "
    data = {
        "email":request.form['email']
    }
    result = mysql.query_db(query,data)

    if len(request.form["first_name"]) == 0 or len(request.form["last_name"]) == 0 or len(request.form["email"]) == 0 or len(request.form["password"]) == 0 or len(request.form["c_password"]) == 0:
        flash("All input fileds are required")
        error=True

    else:
        if not NAME_REGEX.match(request.form['first_name']):
            flash("Name input format is Invalid")
            error = True
        
        if len(request.form['first_name'])<2:
            flash('Invalid name length')

        if not NAME_REGEX.match(request.form['last_name']):
            flash("Name input format is Invalid")
            error = True
        
        if len(request.form['last_name'])<2:
            flash('Invalid name length')

        if len(request.form["password"])< 6:
            flash("Password must be more than 6 characters")
            error=True

        if result:
            if result[0]['email'] == request.form['email']:
                flash("Email has already been registered")
                error=True

        if not EMAIL_REGEX.match(request.form["email"]):
            flash("Invalid Email format")
            error=True

        if request.form["password"] != request.form["c_password"]:
            flash("Passwords do not match")
            error=True

    if error == True:
        return redirect('/')
    elif error == False:

        pw_hash = bcrypt.generate_password_hash(request.form['password']) 
        mysql = connectToMySQL('wall')
        query = "INSERT INTO user (email, first_name, last_name, password, created_at, updated_at) VALUES (%(email)s, %(fname)s, %(lname)s, %(password)s, NOW(), NOW());"
        data = {
                'email':request.form['email'],
                'fname':request.form['first_name'],
                'lname':request.form['last_name'],
                'password':pw_hash
        }
        mysql.query_db(query,data)
        flash('login success')
        return redirect("/success")


    return redirect('/')


@app.route('/login', methods=["POST"])
def login_val():
    mysql = connectToMySQL('login_reg')
    query = "SELECT * FROM user WHERE email = %(email)s "
    data = {
        "email":request.form['email']
    }
    result = mysql.query_db(query,data)

    if len(result) == 0:
        flash('enter email')
        return redirect('/')

    if result[0]['email'] == request.form['email']:
        if bcrypt.check_password_hash(result[0]['password'], request.form['password']):
            session['id'] = result[0]['id']
            return redirect('/success')
        else:
            flash ('Invalid login denied')
            return redirect('/')
    else:
        flash ('Invalid login denied')
        return redirect('/')

@app.route("/success")
def result():
    print(session)
    if session['id']:
        return render_template('success.html')
    else:
        return redirect ('/')

@app.route('/logout')
def logout():
    print(session)
    session.clear()
    print(session)
    return redirect('/')


if __name__ == "__main__":
    app.run(debug=True)