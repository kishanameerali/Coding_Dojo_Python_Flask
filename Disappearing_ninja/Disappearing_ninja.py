#Disappearing Ninjas
'''
These are the routes that you need to set up:

1. On the default page ('localhost:5000'), it should display a view that says "No ninjas here"
2. When user visits /ninja, it should display all four Ninja Turtles (Leonardo, Michelangelo,
Raphael, and Donatello)
3. /ninja/[ninja_color], should display the corresponding Ninja Turtle (grab the color parameter
out of the requested URL)
  1. If user visits /ninja/blue, it should only display the Ninja Turtle Leonardo.
  2. /ninja/orange - Ninja Turtle Michelangelo.
  3. /ninja/red - Ninja Turtle Raphael
  4. /ninja/purple - Ninja Turtle Donatello
  5. If a user tries to hack into your web app by specifying a color or string combination other
  than the colors (Blue, Orange, Red, and Purple), example: /ninja/black or /ninja/123, then
  display Megan Fox who was April O'Neil in the most recent ninja turtles movie.
4. You'll need to remember how to use static files for this assignment. Take a minute to refresh
your memory back to the static files section if you need to :)
'''

from flask import Flask,render_template,redirect,request
app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/ninja')
def ninja():
    return render_template('ninja.html')

@app.route('/ninja/<color>')
def show_turtle(color):
    print color
    if color == 'blue':
        color = 'leonardo.jpg'
        #<img src="{{url_for('static', filename='leonardo.jpg')}}">
    elif color == 'orange':
        color = 'michelangelo.jpg'
        #<img src="{{url_for('static', filename='michelangelo.jpg')}}">
    elif color == 'red':
        color = 'raphael.jpg'
        #<img src="{{url_for('static', filename='raphael.jpg')}}">
    elif color == 'purple':
        color = 'donatello.jpg'
        #<img src="{{url_for('static', filename='donatello.jpg')}}">
    else:
        color = 'notapril.jpg'
        #<img src="{{url_for('static', filename='notapril.jpg')}}">

    return render_template("ninja.html", color=color)



app.run(debug=True)
