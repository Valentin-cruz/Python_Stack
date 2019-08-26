from flask import Flask, render_template, request, redirect, session
app = Flask(__name__)
app.secret_key = "super secret"

@app.route('/')
def index():
    if "count" not in session:
        session["count"] = 1
    else:    
        session["count"] += 1
    
    return render_template("index.html") 

@app.route("/count", methods=["POST"])
def count():
    if request.form["change"]=="add":
        session["count"] += 1
    elif request.form["change"]=="reset":
        session["count"] == 0

    return redirect("/")

@app.route("/clear")
def clear():
    session.clear()
    return redirect("/")

if __name__=="__main__":
    app.run(debug=True) 