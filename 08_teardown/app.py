"""
Aidan Wong
Elmos_Cheez-it
SoftDev
K08 -- Flask
2024-09-29
time spent:
"""

'''
DISCO:
<note any discoveries you made here... no matter how small!>

QCC:
0. 
1. 
2. 
3. 
4. 
5. 
 ...

INVESTIGATIVE APPROACH:
<Your concise summary of how
 you and your team set about
 "illuminating the cave of ignorance" here...>
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



