from flask_wtf import FlaskForm
from wtforms import EmailField, PasswordField, BooleanField, SubmitField, StringField, DateField, IntegerField, TelField, RadioField
from wtforms.validators import InputRequired, Email, NumberRange, Length, Optional, Regexp, EqualTo

telefono_reg = r'^(\d{3} ?){2}\d{4} *$'
nome_reg = r'^([A-Z][a-zàéèòùì]+ )*([A-Z][a-zàéèòùì]+) *$'
cognome_reg = r'^([A-Z](\'[A-Z])?[a-zàéèòùì]+(-| ))*([A-Z](\'[A-Z])?[a-zàéèòùì]+) *$'
urbe_reg = r'^[A-Z][a-zàéèòùì]*(( |\')[A-Z]?[a-zàéèòùì]+)* *$'
via_reg = r'^(Viale|Via|Corso|Piazza|Piazzale) [A-Z]?[a-zàéèòùì]+(( |\')[A-Z]?[a-zàéèòùì]+)* *$'
password_reg = r'^(?=.*?[A-Z])(?=.*?[a-z])(?=.*?[0-9])(?=.*?[#?!@$ %^&*-]).{8,}$'


class LoginForm(FlaskForm):
    email = EmailField('Email', validators=[InputRequired(), Email()])
    password = PasswordField('Password', validators=[InputRequired()])
    remember_me = BooleanField('Remember Me')
    submit = SubmitField('Sign In')

class RegisterForm(FlaskForm):
    nome = StringField('Nome', validators=[InputRequired(), Regexp(regex=nome_reg)])
    cognome = StringField('Cognome', validators=[InputRequired(), Regexp(regex=cognome_reg) ])
    data_nascita = DateField('Nascita', validators=[InputRequired()])
    sesso = RadioField('Sesso', choices=['Maschio', 'Femmina', 'Non-binario', 'Borsa frigo'], validators=[InputRequired()])
    via = StringField('Via', validators=[InputRequired(), Regexp(regex=via_reg)])
    civico = IntegerField('Civico', validators=[InputRequired(), NumberRange(min=1)])
    urbe = StringField('Città', validators=[InputRequired(), Regexp(regex=urbe_reg)])
    telefono = TelField('Telefono', validators=[InputRequired(), Length(min=10, max=12), Regexp(regex=telefono_reg)])
    email = EmailField('Email', validators=[InputRequired(), Email()])
    password = PasswordField('Password', validators=[InputRequired(), Regexp(regex=password_reg)])
    conf_pass = PasswordField('Conferma password', validators=[InputRequired(), EqualTo(password), Regexp(regex=password_reg)])
    submit = SubmitField('Sign up')

class VotoForm(FlaskForm):
    valutazione = IntegerField('Valutazione', validators=[InputRequired(), NumberRange(min=1, max=10)])
    annotazione = StringField('Annotazione', validators=[Optional()])

class ClassiForm(FlaskForm):
    anno_corso = IntegerField('Anno corso', validators=[NumberRange(min=1, max=5)])
    sezione = StringField('Sezione', validators=[Length(min=1, max=1)])
    ordine = StringField('Ordine')
    indirizzo = StringField('Indirizzo')

class ProvaForm(FlaskForm):
    nome = StringField('Nome', validators=[InputRequired(), Regexp(regex=password_reg)])
    submit = SubmitField('Sign up')