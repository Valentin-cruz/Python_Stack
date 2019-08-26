from flask import Flask, render_template, request, redirect, flash # added request
from mysqlconnection import connectToMySQL    # import the function that will return an instance of a connection
app = Flask(__name__)
app.secret_key = "super secret"

@app.route('/')
def index():
    mysql = connectToMySQL('survey')	        # call the function, passing in the name of our db
    survey = mysql.query_db('SELECT * FROM survey;')  # call the query_db function, pass in the query as a string
    print(survey)
    return render_template("index.html", all_survey=survey)

@app.route('/results', methods=['POST'])
def create_user():
    is_valid = True
    if len(request.form['name']) < 1:
        is_valid = False
        flash("Please enter a first name")
    if len(request.form['location']) < 1:
        is_valid = False
        flash("Please enter a last name")
    if len(request.form['language']) < 2:
        is_valid = False
        flash("languages should be at least 2 characters")
    if len(request.form['comment']) < 2:
        is_valid = False
        flash("comments should be at least 2 characters")

    if is_valid:
        query = "INSERT INTO survey (name, location, language) VALUES (%(fn)s, %(ln)s, %(oc)s, NOW(), NOW());"
        data = {
            'name': request.form['name'],
            'location': request.form['location'],
            'language': request.form['language'],
            'comment': request.form['comment'],
        }
        db = connectToMySQL('survey')
        db.query_db(query, data)
    return redirect('/')

if __name__ == "__main__":
    app.run(debug=True)