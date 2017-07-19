#Assignment: Great Number Game
'''
Create a site that when a user loads it creates a random number between 1-100 and
stores the number in session. Allow the user to guess at the number and tell them
when they are too high or too low. If they guess the correct number tell them and
offer to play again.
'''

from flask import Flask, session, render_template, redirect, request
import random

app = Flask(__name__)
app.secret_key = 'shhh'

def random_number():
    session['num'] = random.randrange(0,101)


@app.route('/')
def index():
    session['num'] = random.randrange(0,101)
    print session
    return render_template('index.html')

@app.route('/guess', methods=['POST'])
def guess():
    guessed_num = int(request.form['guess'])
    print guessed_num
    if guessed_num < session['num']:
        session['guessed_num'] = "low"
        print "too low"
    elif guessed_num > session['num']:
        session['guessed_num'] = "high"
        print "too high"
    else:
        session['guessed_num'] = "won"
        print "You Guessed Right"
    return render_template('index.html')

@app.route('/reset')
def reset():
    session['guessed_num'] = ""
    random_number()
    return redirect('/')

app.run(debug=True)
