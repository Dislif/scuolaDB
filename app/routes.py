from app import app
from app.forms import RegisterForm, LoginForm, ProvaForm
from flask import render_template, redirect, url_for, session

@app.route('/')
def index():
    return 'Hello, World!'

@app.route('/signin', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        return redirect(url_for('index'))
    return render_template('login.html', form=form)

@app.route('/prova', methods=['GET', 'POST'])
def prova():
    form = ProvaForm()
    if form.validate_on_submit():
        return redirect(url_for('index'))
    return render_template('provaform.html', form=form)
    
@app.route('/signup', methods=['GET', 'POST'])
def register():
    form = RegisterForm()
    if form.validate_on_submit():
        return redirect(url_for('index'))
    return render_template('registration.html', form=form)