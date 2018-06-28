import json
import os

from flask import Flask, render_template, session, request, flash, redirect, url_for

# configuration
DEBUG = True
SECRET_KEY = 'abc123'
USERNAME = 'admin'
PASSWORD = 'abc123'

# create our little application :)
app = Flask(__name__)
app.config.from_object(__name__)


@app.route('/')
def index():
    if not session.get('logged_in'):
        return render_template('login.html')
    return render_template('monitor.html')


@app.route('/login', methods=['GET', 'POST'])
def login():
    error = None
    if request.method == 'POST':
        if request.form['username'] != app.config['USERNAME']:
            error = 'Invalid username'
        elif request.form['password'] != app.config['PASSWORD']:
            error = 'Invalid password'
        else:
            session['logged_in'] = True
            flash('You were logged in')
            return render_template('monitor.html', error=error)
    return render_template('login.html', error=error)


@app.route('/logout')
def logout():
    session.pop('logged_in', None)
    flash('已退出')
    return redirect(url_for('login'))


@app.route("/cmd")
def cmd():
    os.system('/home/user/shell/restart.sh test')
    return "success"


@app.route("/test",methods=['GET', 'POST'])
def test():
    data = json.loads(request.get_data())
    node = data['node']
    if (node == 'pro'):
        os.system('/home/user/shell/test.sh')
    return "success"


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')
