from flask import Flask  
app = Flask(__name__)    

@app.route('/')          
def hello_world():
    return 'Hello World!'

@app.route('/dojo')          
def dojo():
    return 'Dojo!'

@app.route('/say/<name>')          
def say(name):
    return f'hi {name}!'

@app.route('/repeat/<number>')          
def repeat(number):
    return int("35")* number


if __name__=="__main__":   
    app.run(debug=True)
