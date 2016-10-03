from database import initialize_db, disconnect_db, add_entry, get_current_list
from flask import Flask, request, redirect, url_for, render_template

app = Flask(__name__)
initialize_db()




@app.route('/')
@app.route('/home')
def home():
    """Renders the home page."""
    return render_template('home.html')

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
    hookups = get_current_list()
    return render_template('myrtle.html',
                           items=hookups
                           )

@app.route('/add_hk', methods=['POST'])
def add_myrtle():
    hooker = request.form['hooker']
    hookee = request.form['hookee']
    reason = request.form['reason']
    if hooker == '' or hookee == '' or reason == '':
        return redirect(url_for('myrtle'))
    add_entry(hooker, hookee, reason)
    hookups = get_current_list()
    return redirect(url_for('myrtle'))


@app.route('/shutdown')
def close_db():
    disconnect_db()

if __name__ == '__main__':
    app.debug = True
    app.run()
