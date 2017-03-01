#-----Flask HelloWorld -------#

# import flask class from flask package
from flask import Flask

#create the application object
app = Flask(__name__)

# error handling
app.config["DEBUG"] = True

# Use decorators to link the function to the url
@app.route("/")
@app.route("/hello")

# Define the view using a function, which returns a string.
def hello_world():
    return "Hello World!?!?!?!?!?"

# dynamic routes: route takes a query parameter.
@app.route("/test/<search_query>")
def search(search_query):
    return search_query

@app.route("/integer/<int:value>")
def int_type(value):
    print value + 1
    return "Correct!"

@app.route("/float/<float:value>")
def float_type(value):
    print value + 1
    return "Correct!"

@app.route("/path/<path:value>")
def path_type(value):
    return "Correct!"

# dynamic route with explicit status codes
@app.route("/name/<name>")
def index(name):
    if name.lower() == "michael" :
        return "Hello, {}".format(name), 200
    else:
        return "Not Found", 404

# start the development server using the run() method
if __name__ == "__main__":
    app.run()
