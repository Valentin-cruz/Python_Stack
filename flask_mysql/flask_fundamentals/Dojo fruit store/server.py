from flask import Flask, render_template, request, redirect
app = Flask(__name__)  

@app.route('/')         
def index():
    return render_template("index.html")

@app.route('/checkout', methods=['POST'])         
def checkout():
    first_name=request.form["first_name"]
    last_name=request.form["last_name"]
    student_id=request.form["student_id"]
    strawberries=request.form["strawberries"]
    raspberries=request.form["raspberries"]
    apples=request.form["apples"]
    count= int(strawberries)+int(raspberries)+int(apples)
    print(request.form)
    return render_template("checkout.html", strawberries=strawberries, raspberries=raspberries, apples=apples, count=count, first_name=first_name, last_name=last_name, student_id=student_id)

@app.route('/fruits')         
def fruits():
    return render_template("fruits.html")

if __name__=="__main__":   
    app.run(debug=True)   