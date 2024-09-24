"""
Aidan Wong
Clueless
SoftDev
K09 - Flask Exploration
2024-09-23
time spent: 0.5
"""

from flask import Flask
app = Flask(__name__)          # Creates an instance of flask

@app.route("/")                # Defines a route for the root URL "/", Functions below will be run when the user accesses this page
def hello_world():
    print(__name__)            # Prints the name of the current module (which is __main__)
    return "No hablo queso!"   # Returns a string that will be sent to the browser as HTML when accessing "/"

app.run()                      # Runs the flask application, which starts the web server
                
