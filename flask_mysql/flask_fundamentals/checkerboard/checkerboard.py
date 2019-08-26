from flask import Flask, render_template
app = Flask(__name__)

@app.route('/')
def check():
    return render_template("check.html")

@app.route('/4')
def check2():
    return render_template("check2.html")

@app.route('/<x>/<y>')
def check3(x,y):
    r = float(x)
    c = float(y)
    return render_template("check3.html", c=c, r=r)


if __name__=="__main__": 
    app.run(debug=True) 