from flask import render_template, redirect, url_for, flash
from flask_login import current_user

from stockfight import app, bcrypt, db, models
from stockfight.forms import SignUpForm, SignInForm


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


@app.route('/sign-up', methods=['GET', 'POST'])
def sign_up():
    if current_user.is_authenticated:
        return redirect(url_for('home'))

    form = SignUpForm()

    if form.validate_on_submit():
        pass_hash = bcrypt.generate_password_hash(form.password.data).decode('utf-8')
        user = models.User(username=form.username.data, email=form.email.data.lower(), password=pass_hash)
        user.roles = [models.Role.query.filter_by(title='Employee').first()]
        db.session.add(user)
        db.session.commit()
        flash(f'Your account was created. You may now sign in.', 'success')
        return redirect(url_for('sign_in'))

    return render_template('forms/sign-up.html', title='Sign Up', form=form)


@app.route('/sign-in')
def sign_in():
    return render_template('forms/sign-in.html')
