from flask import Flask, render_template, request, redirect
from mysqlconnection import connectToMySQL    # import the function that will return an instance of a connection
app = Flask(__name__)

@app.route("/")
def index():
    
    return redirect("/users")


@app.route("/users")
def show_all():
    mysql = connectToMySQL('user')	        # call the function, passing in the name of our db
    query = mysql.query_db('SELECT * FROM user;')  # call the query_db function, pass in the query as a string
    print(query)
    return render_template("index.html", all_users = query)

@app.route("/users/create", methods=["POST"])
def create_user():
    query = "INSERT INTO user (fname, lname, email, created_at, updated_at) VALUES (%(fname)s, %(lname)s, %(email)s, NOW(), NOW());"
    data = {
        'fname': request.form['fname'],
        'lname': request.form['lname'],
        'email': request.form['email'],
    }
    mysql = connectToMySQL('user')
    new_friend_id = mysql.query_db(query,data)
    return redirect('/users/'+str(new_friend_id))

@app.route("/users/new")
def new_user():
    return render_template("new_user.html")

@app.route("/users/<num>/edit")
def edit_user(num):
    mysql = connectToMySQL("user")
    query = mysql.query_db("SELECT * FROM user WHERE id="+str(num)+";")
    print(query)
    return render_template("edit_user.html", one_user = query)

@app.route("/update", methods=['POST'])
def update():
    mysql = connectToMySQL("user")
    query = mysql.query_db("UPDATE user SET first_name =\'"+request.form['fname']+"\',last_name =\'"+request.form['lname']+"\',email =\'"+request.form['email']+"\',updated_at = now()  WHERE id="+request.form['id']+";")
    return redirect("/")

@app.route("/users/<num>")
def show_user(num):
    mysql = connectToMySQL("user")
    query = mysql.query_db("SELECT * FROM user WHERE id="+str(num)+";")
    print(query)
    return render_template("show_user.html", one_user = query)

@app.route("/users/<num>/delete")
def delete(num):
    mysql = connectToMySQL("user")
    query = mysql.query_db("DELETE FROM user WHERE id=\'"+num+"\';")
    return redirect("/")

if __name__ == "__main__":
    app.run(debug=True)