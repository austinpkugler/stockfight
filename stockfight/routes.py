from flask import render_template

from stockfight import app


@app.route('/')
def home():
    return render_template('home.html')


@app.route('/account/')
def account():
    return render_template('account.html')


@app.route('/dashboard/')
def dashboard():
    return render_template('dashboard.html')


@app.route('/leaderboard/')
def leaderboard():
    return render_template('leaderboard.html')
