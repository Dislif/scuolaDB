from flask_wtf import FlaskForm
from wtforms import EmailField, PasswordField, BooleanField, SubmitField, StringField, DateField, IntegerField, TelField, RadioField
from wtforms.validators import InputRequired, Email, NumberRange, Length, Optional, Regexp

class LoginForm(FlaskForm):
    email = EmailField('Email', validators=[InputRequired(), Email()])
    password = PasswordField('Password', validators=[InputRequired()])
    remember_me = BooleanField('Remember Me')
    submit = SubmitField('Sign In')

class RegisterForm(FlaskForm):
    nome = StringField('Nome', validators=[InputRequired()])
    cognome = StringField('Cognome', validators=[InputRequired()])
    data_nascita = DateField('Nascita', validators=[InputRequired()])
    sesso = RadioField('Sesso', choices=['Maschio', 'Femmina', 'Non-binario', 'Borsa frigo'], validators=[InputRequired()])
    via = StringField('Via', validators=[InputRequired()])
    civico = IntegerField('Civico', validators=[InputRequired(), NumberRange(min=1)])
    urbe = StringField('Città', validators=[InputRequired()])
    telefono = TelField('Telefono', validators=[InputRequired(), Length(min=10, max=10), Regexp(regex=r'^(\d{3} ?){2}\d{4}$')])
    email = EmailField('Email', validators=[InputRequired(), Email()])
    password = PasswordField('Password', validators=[InputRequired()])
    conf_pass = PasswordField('Conferma password', validators=[InputRequired()])
    submit = SubmitField('Sign up')

class VotoForm(FlaskForm):
    valutazione = IntegerField('Valutazione', validators=[InputRequired(), NumberRange(min=1, max=10)])
    annotazione = StringField('Annotazione', validators=[Optional()])

class ClassiForm(FlaskForm):
    anno_corso = IntegerField('Anno corso', validators=[NumberRange(min=1, max=5)])
    sezione = StringField('Sezione', validators=[Length(min=1, max=1)])
    ordine = StringField('Ordine')
    indirizzo = StringField('Indirizzo')