"""
Aidan Wong
Elmos_Cheez-it
SoftDev
K08 -- Flask
2024-09-29
time spent: 0.5
"""

'''
DISCO:
0. Returning strings in functions cause it to be sent to the HTML of the flask page. (base output language is HTML)
1. Flask can only be run on local machines
2. Flask behaves like an object in other langauges
3. app.route functions similarly to href in HTML

QCC:
0. What does "name" stand for?
1. Why does "print(__name__)" print "__main__"
2. How was "__name__" defined?
3. Can Flask be made to run on other computers?
4. Does "app.route" route all functions under it or just the one directly under it?
5. How does flask create these developmental servers?
 ...

INVESTIGATIVE APPROACH:
We looked at the code, ran it on our local machines, and observed the impacts of what happens. We also used the internet for identifying things we didn't understand.
'''


from flask import Flask

app = Flask(__name__)                    # Q0: Where have you seen similar syntax in other langs? 
                                         # A0: This line looks similar to creating an instance of an object in Java (myClass varName = new myClass(args)). Based on this, it looks like app is being created as a Flask object with __name__ as the argument being passed through it

@app.route("/")                          # Q1: What points of reference do you have for meaning of '/'?
                                         # A1: '/' in linux is the root of a directory. Based on the fact that Flask allows you to host a web page locally and that the syntax is "app.route()", '/' is likely a reference to the index of the page. In terms of HTML, '/' would be the index, which is the starting page of a web page.
def hello_world():
    print(__name__)                      # Q2: Where will this print to? Q3: What will it print?
                                         # A2: This will print to the terminal, as the print function in python prints to the terminal. A3: It will print the value of "__name__", which is __main__ (as seen when running "app.py")
    return "No hablo queso!"             # Q4: Will this appear anywhere? How u know?
                                         # A4: This will appear in the browser when you run app.py and open the development server. When you visit the development server after running "app.py", these words show on the screen. With this knowledge, it can be guessed that the run function below causes defined functions within the program to be executed. Since the words "No habblo queso!" appeared in the index HTML page, returning strings under an app.route() most likely adds the strings to the body of the HTML

app.run()                                # Q5: Where have you seen similar constructs in other languages?
                                         # A5: This syntax is similiar to Object Oriented Programming languages, where an object can have several functions associated with it. In this case, the flask object is being called to do the run function that is defined within the object.



