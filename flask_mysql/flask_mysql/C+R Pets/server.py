from flask import Flask, render_template, request, redirect
from mysqlconnection import connectToMySQL    # import the function that will return an instance of a connection
app = Flask(__name__)
@app.route("/")
def index():
    mysql = connectToMySQL('c_r_pets')	        # call the function, passing in the name of our db
    friends = mysql.query_db('SELECT * FROM pets;')  # call the query_db function, pass in the query as a string
    print(friends)
    return render_template("index.html", all_friends=friends)

@app.route("/create_friend", methods=["POST"])
def add_friend_to_db():
    query = "INSERT INTO pets (name, type, created_at, updated_at) VALUES (%(name)s, %(type)s, NOW(), NOW());"
    data = {
        'name': request.form['name'],
        'type': request.form['type'],
    }
    db = connectToMySQL('c_r_pets')
    result=db.query_db(query, data)
    return redirect('/')

if __name__ == "__main__":
    app.run(debug=True)