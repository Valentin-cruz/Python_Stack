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
    mysql = connectToMySQL('wall')
    query = "SELECT * FROM user WHERE email = %(email)s "
    data = {
        "email":request.form['email']
    }
    result = mysql.query_db(query,data)

    if len(request.form["first_name"]) == 0 or len(request.form["last_name"]) == 0 or len(request.form["email"]) == 0 or len(request.form["password"]) == 0 or len(request.form["c_password"]) == 0:
        error=True
        flash("All input fileds are required")

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

        if len(request.form["password"])< 8:
            flash("Password must be more than 8 characters")
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
        flash('login wall')
        return redirect("/wall")

    return redirect('/')

@app.route('/login', methods=["POST"])
def login_val():
    mysql = connectToMySQL('wall')
    query = "SELECT * FROM user WHERE email = %(email)s"
    data = {
        'email':request.form['email']
    }
    result = mysql.query_db(query,data)

    if len(result) == 0:
        flash(' email')
        return redirect('/')

    if result[0]['email'] == request.form['email']:
        print(result[0]['password'])
        if bcrypt.check_password_hash(result[0]['password'], request.form['password']):
            session['id'] = result[0]['id']
            return redirect('/wall')
        else:
            flash ('Invalid login denied')
            return redirect('/')
    else:
        flash ('Invalid login denied')
        return redirect('/')

@app.route("/wall")
def result():
    if session['id']:
        mysql = connectToMySQL('wall')
        query = "SELECT messages.id, messages.user_id, messages.sent_id, messages.message, messages.created_at, messages.updated_at, user.first_name, user.last_name FROM messages join user on user.id = messages.user_id  WHERE messages.sent_id = %(user_id)s ORDER BY messages.created_at desc;"
        data = {
            'user_id':session['id']
        }
        messages = mysql.query_db(query,data)

        mysql2 = connectToMySQL('wall')
        send_query = "SELECT * FROM user WHERE NOT id = %(user_id)s;"
        send_data ={
            'user_id':session['id']
        }
        sends = mysql2.query_db(send_query,send_data)
        return render_template('wall.html', messages = messages, sends = sends)
    else:
        return redirect ('/')

@app.route('/logout')
def logout():
    session.clear()
    return redirect('/')

@app.route('/delete')
def delete(message_id):
    mysql = connectToMySQL('wall')
    query = 'SELECT * FROM messages WHERE id = %(message_id)s;'
    data = {
        'message_id':message_id
    }
    result = mysql.query_db(query,data)
    if result[0]['sent_id'] != session['id']:
        return redirect('/danger')
    elif result[0]['sent_id'] == session['id']:
        mysql = connectToMySQL('wall')
        query = "DELETE FROM messages WHERE id = %(message)s"
        data = {
            'message':message_id
        }
        mysql.query_db(query,data)
        return redirect('/wall')

@app.route('/send', methods = ['POST'])
def send():
    mysql = connectToMySQL('wall')
    query = "SELECT * FROM user WHERE id = %(id)s "
    data = {
        "id":request.form['button']
    }
    mysql.query_db(query,data) 

    if len(request.form['message']) == 0:
        flash("No input")
        return redirect('/wall')
    else:
        mysql = connectToMySQL('wall')
        query = "INSERT INTO messages (user_id, sent_id, message, created_at, updated_at) VALUES (%(user_id)s, %(sent_id)s, %(message)s, NOW(), NOW());"
        data = {
            'user_id': request.form['user_id'],
            "sent_id":request.form['sent_id'],
            "message":request.form['message']
        }
        mysql.query_db(query,data)
    return redirect ('/wall')

@app.route('/danger', methods=['GET'])
def danger():
    session['id'] = False
    return render_template('danger.html')


if __name__ == "__main__":
    app.run(debug=True)