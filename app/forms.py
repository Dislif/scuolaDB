from flask_wtf import FlaskForm
from wtforms import EmailField, PasswordField, SubmitField, StringField, DateField, IntegerField, TelField, RadioField
from wtforms.validators import InputRequired, Email, NumberRange, Length, Optional, Regexp, EqualTo, ValidationError
from app.assets.validation_regex import nome_reg, cognome_reg, indirizzo_reg, urbe_reg, telefono_reg, password_reg
from app.assets.error_message import input_required_error, tel_error, str_error, indirizzo_error, password_error, confirm_pass_error, email_error
from app.models import Utente


class LoginForm(FlaskForm):
    email = EmailField('Email', validators=[
        InputRequired(message=input_required_error), 
        Email(message=email_error)
    ])
    password = PasswordField('Password', validators=[
        InputRequired(message=input_required_error), 
        Regexp(regex=password_reg, message=password_error)
    ])
    #remember_me = BooleanField('Remember Me')
    submit = SubmitField('Sign In')

    def validate_email(self, email):
        user = Utente.query.filter_by(email=email.data).first()
        if user is None:
            raise ValidationError('Utente non registrato')

class RegisterForm(FlaskForm):
    nome = StringField('Nome', validators=[
        InputRequired(message=input_required_error), 
        Regexp(regex=nome_reg, message=str_error)
    ])
    cognome = StringField('Cognome', validators=[
        InputRequired(message=input_required_error), 
        Regexp(regex=cognome_reg, message=str_error) 
    ])
    data_nascita = DateField('Nascita', validators=[
        InputRequired(message=input_required_error)
    ])
    sesso = RadioField('Sesso', choices=['Maschio', 'Femmina', 'Non-binario', 'Borsa frigo'], validators=[
        InputRequired(message=input_required_error)
    ])
    indirizzo = StringField('Indirizzo', validators=[
        InputRequired(message=input_required_error), 
        Regexp(regex=indirizzo_reg, message=indirizzo_error)
    ])
    urbe = StringField('Città', validators=[
        InputRequired(message=input_required_error), 
        Regexp(regex=urbe_reg, message=str_error)
    ])
    telefono = TelField('Telefono', validators=[
        InputRequired(message=input_required_error), 
        Length(min=10, max=12),
        Regexp(regex=telefono_reg, message=tel_error)
    ])
    email = EmailField('Email', validators=[
        InputRequired(message=input_required_error), 
        Email(message=email_error)
    ])
    password = PasswordField('Password', validators=[
        InputRequired(message=input_required_error), 
        Regexp(regex=password_reg, message=password_error)
    ])
    conf_pass = PasswordField('Conferma password', validators=[
        InputRequired(message=input_required_error), 
        EqualTo('password', message=confirm_pass_error)
    ])
    submit = SubmitField('Sign up')

    def validate_email(self, email):
        user = Utente.query.filter_by(email=email.data).first()
        if user is not None:
            raise ValidationError('Email già in uso, inserisci un altra email!')

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