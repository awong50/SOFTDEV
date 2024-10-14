"""
Elmos_Cheez-its: Amanda Tan, Ethan Sie, Aidan Wong
SoftDev
K16 - Flask Sessions
2024-10-09
time spent: 1.0
"""

from flask import Flask, render_template, request, session, redirect, url_for
import os

app = Flask(__name__)

app.secret_key = os.urandom(32)

users = {}

@app.route("/", methods=['GET', 'POST'])
def disp_loginpage():
    # print(users)
    form_type = request.form.get('form_type')
    if form_type == 'sign_in':
        name = request.form.get('name')
        password = request.form.get('password')

        #print(name)
        #print(password)

        if name in users and users[name] == password: 
            session['username'] = name 

            # print(session)
            return redirect(url_for('disp_loginpage')) 

        else:
            return render_template('login.html', errorL = "USERNAME OR PASSWORD IS INCORRECT")
    if 'username' in session: 
        return redirect(url_for('authenticate')) 
    
    elif form_type == 'sign_up':
        name = request.form.get('name')
        password = request.form.get('password')

        if not name in users:
            users[name] = password
            return redirect(url_for('disp_loginpage'))
        else:
            return render_template('login.html', errorS="USERNAME TAKEN")
    return render_template('login.html')


@app.route("/home", methods=['GET', 'POST'])
def authenticate():
    if 'username' in session: 
        returnName = session['username']
        return render_template('response.html', username=returnName) 
    return redirect(url_for('disp_loginpage')) 

@app.route("/logout", methods=['GET', 'POST'])
def disp_logoutpage():
    if 'username' in session:
        returnName = session['username'] 
        session.pop('username')  
        return render_template('logout.html', username=returnName) 
    return redirect(url_for('disp_loginpage')) 



if __name__ == "__main__":
    app.debug = True
    app.run()