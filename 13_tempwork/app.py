from flask import Flask, render_template
import random
app = Flask(__name__)

@app.route("/")
def index():
    return render_template('index.html')

@app.route("/wdywtbwygp")
def test_tmplt():
    with open("data/occupations.csv") as file:
        data = file.read().strip().split("\n")
    occupation = {}
    weights = []
    for i in range(1, len(data)-1):
        splitted = data[i].rsplit(",", 2)
        splitted[0] = splitted[0].replace('"', "")
        occupation[splitted[0]] = {'weight': float(splitted[1]), 'resource': splitted[2]}
        weights.append(float(splitted[1])) 

    randO = random.choices(list(occupation), weights, k=1)[0]
    resource = occupation[randO]['resource']

    return render_template( 'tablified.html', random_occupation=randO, occupations_dict=occupation, resource=resource)


if __name__ == "__main__":
    app.debug = True
    app.run()
