from flask import Flask, render_template, request, redirect, session, Markup
import random
app = Flask(__name__)
app.secret_key = "super secret"

@app.route("/")
def index():
    guess_number = random.randrange(0,101)
    if "guess" not in session:
        session["guess"] = guess_number
    return render_template("index.html")

@app.route("/check", methods=["POST"] )
def check_input_value():
    input_value = int(request.form["input_guess"])
    random_guess = session["guess"]
    box_color = ""
    box_text = ""
    reset_button = ""

    if input_value == random_guess:
        box_color = "green"
        box_text = "You've Guessed the number!"
        reset_button = Markup('<a href="/"><button type="submit" class="btn btn-primary subbut" value="Submit">Try Again</button><a>')
        session.clear()
        return render_template("index.html",box_color=box_color, box_text=box_text, reset_button=reset_button)

    if input_value > random_guess:
        box_color = "red"
        box_text = "your guess is to high"
        return render_template("index.html",box_color=box_color, box_text=box_text, reset_button=reset_button)

    if input_value < random_guess:
        box_color = "red"
        box_text = "your guess is to low"
        return render_template("index.html",box_color=box_color, box_text=box_text)

if __name__=="__main__":
    app.run(debug=True) 