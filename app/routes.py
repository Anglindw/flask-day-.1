from app import app
from flask import render_template

@app.route('/')
@app.route('/home')
def home():
    
    return render_template('index.html')

@app.route('/fav_five')
def fav_five():
    chiefs = ['Patrick Mahomes','Trent Mcduffie', 'Travis Kelce', 'Willie Gay', 'George Karlaftis']
    return render_template('fav_five.html', names=chiefs)