"""
Aidan Wong
Clueless
SoftDev
K09 - Flask Exploration
2024-09-23
time spent: 0.5
"""

from flask import Flask
app = Flask(__name__)            # create instance of class Flask

@app.route("/")                  # assign fxn to route
def hello_world():
    return "No hablo queso!"

app.run()

