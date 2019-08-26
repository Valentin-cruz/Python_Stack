from flask import Flask, render_template
app = Flask(__name__)
@app.route('/')
def index():
    print("hello")
    return render_template("playground.html")

@app.route('/play')          
def play():
    return render_template("playground.html")

@app.route('/play/<x>')          
def repeat(x):
    repeat = int(x)
    return render_template('playground2.html', repeat=repeat)

@app.route('/play/<x>/<color>')          
def repeat2(x,color):
    repeat = int(x)
    colorchange = color
    return render_template('playground3.html', repeat=repeat, colorchange = colorchange)

if __name__=="__main__": 
    app.run(debug=True) 