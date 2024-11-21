"""
HallsRelief: Aidan Wong, Brian Liu, Victor Casado
SoftDev
K23 - Introduction to APIs
2024-10-20
time spent: 0.6
"""

from flask import Flask, render_template
import os, json
import urllib.request

app = Flask(__name__)
app.secret_key = os.urandom(32)
# Get the key from the key_nasa.txt
with open("key_nasa.txt", "r") as key_file:
    api_key = key_file.read().strip()

@app.route('/')
def main():
    with urllib.request.urlopen("https://api.nasa.gov/planetary/apod?api_key=" + api_key) as response:
        html = response.read() # Read API response
        str = html.decode('utf-8') # Decode the bytes into string
        data = json.loads(str) # Converts JSON string to python library
        # print(data) # Prints the dictionary with the data
    return render_template("main.html", explanation=data["explanation"], url=data["hdurl"])

if __name__ == "__main__": # false if this file imported as module
    app.debug = True
    app.run(port=5001)