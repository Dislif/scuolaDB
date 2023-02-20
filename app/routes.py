from app import app
import app.forms as fm
from flask import render_template, redirect, url_for, request

@app.route('/')
def index():
    return 'Hello, World!'

@app.route('/login')
def login():
    return render_template('login.html')

@app.route('/signin', methods=['POST'])
def signin():
    u=request.form['username']
    p=request.form['password']
    return render_template('ris.html', u=u, p=p)

@app.route('/prova', methods=['GET', 'POST'])
def prova():
    form = fm.ProvaForm()
    if form.validate_on_submit():
        return redirect(url_for('index'))
    return render_template('provaform.html', form=form)
    
@app.route('/register')
def register():
    form = fm.RegisterForm()
    return render_template('registration.html', form=form)

@app.route('/signup', methods=['POST'])
def signup():
    u=request.form['username']
    p=request.form['password']
    e=request.form['email']
    return render_template('ris.html', u=u, p=p, e=e)