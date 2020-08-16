# Import Flask class from flask
from flask import Flask #Capital "F" indicates a class name

#Create an instance of the Flask class
app = Flask(__name__) #Convention is to name variables "app"

#Use the "route" decorator to tell Flask what URL should trigger the function that follows
@app.route("/")
#Define a function, named "index"
def index():
    return "Hello, World"