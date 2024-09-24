"""
Aidan Wong
Clueless
SoftDev
K09 - Flask Exploration
2024-09-23
time spent: 0.5
"""

from flask import Flask
app = Flask(__name__)           #create instance of class Flask

@app.route("/")                 #assign fxn to route
def hello_world():
    print("the __name__ of this module is... ")
    print(__name__)
    return "No hablo queso!"

if __name__ == "__main__":      # true if this file NOT imported; Identifies whether or not it is the main program
    app.debug = True            # enable auto-reload upon code change; Works like extension Live Server for HTMl files
    app.run()
