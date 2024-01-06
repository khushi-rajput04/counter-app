from flask import Flask, render_template 
from replit import db

app = Flask(__name__)

if 'number' not in db:
    db['number'] = 0
    
# root --> '/'
# increment --> '/increment'
# db --> {'number': 0}

@app.route('/')
def home():
    return render_template('index.html', number = db['number'])

@app.route('/increment')
def increment():
    #increments a number
    db['number'] += 1
    return render_template('index.html', number=db['number'])

@app.route('/decrement')
def decrement():
    #decrements a number
    db['number'] -= 1
    return render_template('index.html', number=db['number'])
    
app.run(host='0.0.0.0', port=81)