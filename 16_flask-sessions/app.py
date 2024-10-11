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

app.secret_key = os.urandom(32) # Secret key has to be generated in order to use sessions

# Hardcodes the valid usernames and their corresponding passwords
users = {
    'Aidan': 'bill',
    'Amanda': 'law',
    'Ethan': 'order'
}

@app.route("/", methods=['GET', 'POST'])
def disp_loginpage():
    if request.method == 'POST':
        # Takes the username and password from the form to compare with the array
        name = request.form.get('name')
        password = request.form.get('password')

        #print(name)
        #print(password)

        if name in users and users[name] == password: # Checks to see if user info exists
            session['username'] = name # Store username in session for access (Not storing the password for security)

            # print(session) # Debug statement to look inside the session object
            return redirect(url_for('disp_loginpage')) # Logs the user in once it is verified that they have an account and a session has been created

        return redirect(url_for('disp_loginpage')) # Used to remove the confirm form resubmission pop up when page is refreshed after entering incorrect data
    if 'username' in session: # Checks to see if a session exists (indicated by it being filled with a username key)
        return redirect(url_for('authenticate')) # Use of redirect to swap page (login screen can't be accessed when logged in); Use of 'url_for' for more dynamic code (in case route changes)
    return render_template('login.html') # Display base login screen


@app.route("/home", methods=['GET', 'POST'])
def authenticate():
    if 'username' in session: # Check to see if valid session
        returnName = session['username'] # Set value in username key to variable
        return render_template('response.html', username=returnName) # Render template only used when it is verified that there is a valid session
    return redirect(url_for('disp_loginpage')) # Sends user back to login page if not logged in

@app.route("/logout", methods=['GET', 'POST'])
def disp_logoutpage():
    if 'username' in session: # Check to see if valid session
        returnName = session['username'] # Sets variable before popping to grab the value from session
        session.pop('username')  # Removes the username key from session, which basically closes the session with this code's logic
        return render_template('logout.html', username=returnName) # Username variable set with Jinja to show user's name on page load
    return redirect(url_for('disp_loginpage')) # Sends user back to login page if not logged in



if __name__ == "__main__":
    app.debug = True
    app.run()