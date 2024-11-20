"""
HallsRelief: Aidan Wong, Brian Liu, Victor Casado
SoftDev
K23 - Introduction to APIs
2024-10-20
time spent: 0.3
"""


from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def main():
    return render_template('main.html')

if __name__ == "__main__":
    app.debug = True
    app.run()