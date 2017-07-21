#Counter Assignment
#Count the number of times someone visits the page during a session

from flask import Flask,session,render_template,redirect
app = Flask(__name__)
app.secret_key = 'secretsecret'

@app.route("/")
def index():
    if 'counter' not in session:
        session['counter'] = 0
    session['counter'] += 1
    return render_template('index.html')

@app.route("/button", methods=['POST'])
def plustwo():
    session['counter'] += 2
    redirect('/')

app.run(debug=True)
