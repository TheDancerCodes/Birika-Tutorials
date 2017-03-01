#-----Flask HelloWorld -------#

# import flask class from flask package
from flask import Flask

#create the application object
app = Flask(__name__)

# Use decorators to link the function to the url
@app.route("/")
@app.route("/hello")

# Define the view using a function, which returns a string.
def hello_world():
    return "Hello World!"

# start the development server using the run() method
if __name__ == "__main__":
    app.run()
