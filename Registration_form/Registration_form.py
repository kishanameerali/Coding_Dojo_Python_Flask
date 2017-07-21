#Registration Form
'''
Create a simple registration page with the following fields:

-email
-first_name
-last_name
-password
-confirm_password

Here are the validations you must include:

-All fields are required and must not be blank
-First and Last Name cannot contain any numbers
-Password should be more than 8 characters
-Email should be a valid email
-Password and Password Confirmation should match

When the form is submitted, make sure the user submits appropriate information.
If the user did not submit appropriate information, return the error(s) above the
form that asks the user to correct the information.
'''

from flask import Flask,render_template,redirect,session,flash,request
import re

EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9\.\+_-]+@[a-zA-Z0-9\._-]+\.[a-zA-Z]*$')
app = Flask(__name__)
app.secret_key = 'secret'

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/user', methods=['POST'])
def register():
    #Initial Validation Method
    '''
    if len(request.form['first_name']) < 1 or len(request.form['last_name']) < 1 or len(request.form['email']) < 1 or len(request.form['password']) < 1:
        flash("Please fill in all fields")
    elif len(request.form['password']) < 9:
        flash("Password must be more than 8 characters")
    elif (request.form['first_name']).isalpha() == False or (request.form['first_name']).isalpha() == False:
        flash("First and Last names cannot contain any numbers")
    elif not EMAIL_REGEX.match(request.form['email']):
        flash("Invalid email address")
    elif request.form['password'] != request.form['confirm_password']:
        flash("Password and confirmation don't match")
    else:
        flash("User is registered")
    return redirect('/')
    '''
    #Second Validation Method using Lists to show all flash messages at once
    error_messages = []

    if len(request.form['first_name']) < 1 or len(request.form['last_name']) < 1 or len(request.form['email']) < 1 or len(request.form['password']) < 1:
        error_messages.append("Please fill in all fields")

    if len(request.form['password']) < 9:
        error_messages.append("Password must be more than 8 characters")

    if (request.form['first_name']).isalpha() == False or (request.form['first_name']).isalpha() == False:
        error_messages.append("First and Last names cannot contain any numbers")

    if not EMAIL_REGEX.match(request.form['email']):
        error_messages.append("Invalid email address")

    if request.form['password'] != request.form['confirm_password']:
        error_messages.append("Password and confirmation don't match")

    if(error_messages):
        for error in error_messages:
            flash(error)
        return redirect('/')
    else:
        flash("User is registered")
    return redirect('/')

app.run(debug=True)
