from database import *
from flask import Flask, request, session, g, redirect, url_for, abort, render_template, flash

app = Flask(__name__)




@app.route('/')
@app.route('/home')
def home():
    """Renders the home page."""
    return render_template('home.html')
    return "Hello World\n"

@app.route('/history')
def her_story():
	return render_template('HERstory.html')

@app.route('/lawn')
def lawn():
	return render_template('lawn.html')

@app.route('/teh')
def teh():
	return render_template('teh.html')

@app.route('/rush')
def rush():
	return render_template('rush.html')

# @app.route('/myrtle')


if __name__ == '__main__':
	app.debug = True
	app.run()