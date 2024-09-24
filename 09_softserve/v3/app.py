"""
Aidan Wong
Clueless
SoftDev
K09 - Flask Exploration
2024-09-23
time spent: 0.5
"""

from flask import Flask
app = Flask(__name__)                 #create instance of class Flask

@app.route("/")                       #assign fxn to route
def hello_world():
    print("about to print __name__...")
    print(__name__)                   #where will this go?: This is printed to the terminal that was used to start the Flask development server
    return "No hablo queso!"

app.debug = True # Enables a debugger that appears in terminal with a PIN and a message that says "Restarting with stat"; This portion of the code is run before the hello world function above
app.run()
