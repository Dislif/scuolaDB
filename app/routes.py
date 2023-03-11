from app import app, db
from app.forms import RegisterForm, LoginForm, ProvaForm
from flask import render_template, redirect, url_for, session
from app.models import Utente, Anagrafica

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
        user = Utente(email=form.email.data)
        user.set_password(form.password.data)
        params = form.data
        #list(map(lambda p : params.pop(p), ['submit','csrf_token','conf_pass']))
        for field in ['submit','csrf_token','conf_pass','password','email']:
            params.pop(field)
        anagraphics = Anagrafica(**params, utente=user)
        for entry in [user, anagraphics]:
            db.session.add(entry)
        db.session.commit()
        return redirect(url_for('index'))
    return render_template('registration.html', form=form)