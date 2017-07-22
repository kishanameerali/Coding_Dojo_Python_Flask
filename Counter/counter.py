#Counter Assignment
'''
Count the number of times someone visits the page during a session

Extra Challenges
-add a +2 button underneath the counter that increments the counter by 2 and reloads the page.
-add a reset button that will reset the counter to 1
'''

from flask import Flask,session,render_template,redirect
app = Flask(__name__)
app.secret_key = 'secretsecret'

@app.route("/")
def index():
    if 'counter' not in session:
        session['counter'] = 0
    session['counter'] += 1
    return render_template('index.html')

@app.route("/plustwo")
def plustwo():
    session['counter'] += 1
    return redirect('/')

@app.route("/reset")
def reset():
    session.clear()
    return redirect('/')

app.run(debug=True)
