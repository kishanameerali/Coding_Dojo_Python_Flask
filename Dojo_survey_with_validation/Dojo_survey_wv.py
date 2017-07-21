#Dojo Survey With Validation
"""
Build a new Flask project. The goal is to help you get familiar with sending POST requests
through a form and displaying that information:

You should have two routes: '/' and '/result' both of which render a template

Take the Dojo Survey assignment that you completed previously and add validations!
The Name and Comment fields should be validated so that they are not blank. Also,
validate that the comment field is no longer than 120 characters.
"""


from flask import Flask,render_template,request,redirect,flash,session
app = Flask(__name__)
app.secret_key = "secret"

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/result', methods=['POST'])
def result():
    #Initial Validation Method
    '''
    print request.form
    if len(request.form['name']) and len(request.form['comment']) > 0 and len(request.form['comment']) < 121:
        return render_template('result.html', user = request.form)
    else:
        flash("Name or Comment field is blank or Comment field exceeds 120 characters")
        return redirect('/')
    '''
    #Second Validation Method using Lists to show all flash messages at once
    error_messages = []
    if (len(request.form['name']) < 2):
        print "name validation failed"
        error_messages.append("Name field cannot be blank")

    if (len(request.form['comment']) < 2):
        print "comment length validation failed"
        error_messages.append("Comment field cannot be blank")

    if (len(request.form['comment']) > 121):
        print "comment validation failed"
        error_messages.append("Comment field exceeds 120 characters")

    if (error_messages):
        for error in error_messages:
            flash(error)
        return redirect('/')

    return render_template('result.html', user = request.form)

app.run(debug=True)
