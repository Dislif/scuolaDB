from app import app
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
    return render_template('registration.html')

@app.route('/signup', methods=['POST'])
def signup():
    u=request.form['username']
    p=request.form['password']
    e=request.form['email']
    return render_template('ris.html', u=u, p=p, e=e)