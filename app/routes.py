from app import app
import app.forms as fm
from flask import render_template, request

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

    
@app.route('/register')
def register():
    form = fm.RegisterForm()
    return render_template('registration.html', form=form, type=type)

@app.route('/signup', methods=['POST'])
def signup():
    u=request.form['username']
    p=request.form['password']
    e=request.form['email']
    return render_template('ris.html', u=u, p=p, e=e)