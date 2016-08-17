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

@app.route('/myrtle', methods=['GET'])
def myrtle():
	open_connection()
	hookups = get_current_list()
	close_connection()
	return render_template('myrtle.html',
		items=hookups
		)

@app.route('/add_hk', methods=['POST'])
def add_myrtle():
	hooker = request.form['hooker']
	hookee = request.form['hookee']
	reason = request.form['reason']
	print hooker
	print hookee
	print reason
	if hooker == '' or hookee == '' or reason == '':
		return redirect(url_for('myrtle'))
	open_connection()
	add_entry(hooker, hookee, reason)
	hookups = get_current_list()
	close_connection()
	return redirect(url_for('myrtle'))

if __name__ == '__main__':
	app.debug = True
	app.run()
