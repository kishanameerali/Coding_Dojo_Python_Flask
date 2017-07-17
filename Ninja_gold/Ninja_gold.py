#Ninja Gold
'''
You're going to create a mini-game that helps a ninja make some money! When you
start the game, your ninja should have 0 gold. The ninja can go to different places
(farm, cave, house, casino) and earn different amounts of gold. In the case of a
casino, your ninja can earn or LOSE up to 50 golds. Your job is to create a web app
that allows this ninja to earn gold and to display past activities of this ninja.
'''

from flask import Flask, session, redirect, render_template, request
import random
import datetime
from datetime import date

app = Flask(__name__)

app.secret_key = "secretsecret"

@app.route('/')
def index():
    if 'gold_total' and 'result' not in session:
        session['gold_total'] = 0
        session['result'] = []
    return render_template('index.html')

@app.route('/process_money',methods=['POST'])
def process_money():
    if request.form['building'] == 'farm':
        gold = random.randint(10,21)
        session['gold_total'] += gold
        session['result'].insert(0,"Earned " + str(gold) + " from the farm! (" + datetime.datetime.now().strftime('%Y/%m/%d %I:%M') + ")")
        print gold
        print session['gold_total']
    elif request.form['building'] == 'cave':
        gold = random.randint(5,11)
        session['gold_total'] += gold
        session['result'].insert(0,"Earned " + str(gold) + " from the cave! (" + datetime.datetime.now().strftime('%Y/%m/%d %I:%M') + ")")
        #session['gold_total'] += random.randint(5,11)
        print gold
        print session['gold_total']
    elif request.form['building'] == 'house':
        gold = random.randint(2,5)
        session['gold_total'] += gold
        session['result'].insert(0,"Earned " + str(gold) + " from the house! (" + datetime.datetime.now().strftime('%Y/%m/%d %I:%M') + ")")
        #session['gold_total'] += random.randint(2,5)
        print gold
        print session['gold_total']
    elif request.form['building'] == 'casino':
        gold = random.randint(-50,51)
        session['gold_total'] += gold
        if gold > 0:
            session['result'].insert(0,"Entered a casino and won " + str(gold) + "... YAYYY! (" + datetime.datetime.now().strftime('%Y/%m/%d %I:%M') + ")")
        else:
            session['result'].insert(0,"Entered a casino and lost " + str(gold*(-1)) + "... Ouch! (" + datetime.datetime.now().strftime('%Y/%m/%d %I:%M') + ")")
        #session['gold_total'] += random.randint(-50,51)
        print gold
        print session['gold_total']
    return redirect('/')

app.run(debug=True)
