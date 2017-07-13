#Dojo Survey
"""
Build a new Flask project. The goal is to help you get familiar with sending POST requests
through a form and displaying that information:

You should have two routes: '/' and '/result' both of which render a template
"""


from flask import Flask,render_template,request,redirect
app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/result', methods=['POST'])
def result():
    print request.form
    #name = request.form['name']
    #location = request.form['location']
    #language = request.form['language']
    #comment = request.form['comment']
    return render_template('result.html', user = request.form)

app.run(debug=True)
