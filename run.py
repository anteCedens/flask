# Import Flask class from flask
from flask import Flask #Capital "F" indicates a class name

#Create an instance of the Flask class
#The first argument of the Flask class is the name of the applications module - our package
app = Flask(__name__) #Convention is to name variables "app"
# Since we're just using a single module, we can use"__name__" which is a built-in Python variable. Flask needs this so that it knows where to look for templates and static files

#Use the "route" decorator to tell Flask what URL should trigger the function that follows
@app.route("/")
#Define a function, named "index"
def index():
    return "Hello, World"