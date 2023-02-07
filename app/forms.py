from flask_wtf import FlaskForm
import wtforms as wtf 
import wtforms.validators as wtfv

class LoginForm(FlaskForm):
    email = wtf.EmailField('Email', validators=[wtfv.InputRequired(), wtfv.Email()])
    password = wtf.PasswordField('Password', validators=[wtfv.InputRequired()])
    remember_me = wtf.BooleanField('Remember Me')
    submit = wtf.SubmitField('Sign In')

class RegisterForm(FlaskForm):
    nome = wtf.StringField('Nome', validators=[wtfv.InputRequired()])
    cognome = wtf.StringField('Cognome', validators=[wtfv.InputRequired()])
    data_nascita = wtf.DateField('Nascita', validators=[wtfv.InputRequired()])
    sesso = wtf.RadioField('Sesso', choices=['Maschio', 'Femmina', 'Non-binario', 'Borsa frigo'], validators=[wtfv.InputRequired()])
    via = wtf.StringField('Via', validators=[wtfv.InputRequired()])
    civico = wtf.IntegerField('Civico', validators=[wtfv.InputRequired(), wtfv.NumberRange(min=1)])
    urbe = wtf.StringField('Città', validators=[wtfv.InputRequired()])
    telefono = wtf.TelField('Telefono', validators=[wtfv.InputRequired(), wtfv.Length(min=10, max=10), wtfv.Regexp(regex=r'^(\d{3} ?){2}\d{4}$')])
    email = wtf.EmailField('Email', validators=[wtfv.InputRequired(), wtfv.Email()])
    password = wtf.PasswordField('Password', validators=[wtfv.InputRequired()])
    conf_pass = wtf.PasswordField('Conferma password', validators=[wtfv.InputRequired()])
    submit = wtf.SubmitField('Sign up')

class VotoForm(FlaskForm):
    valutazione = wtf.IntegerField('Valutazione', validators=[wtfv.InputRequired(), wtfv.NumberRange(min=1, max=10)])
    annotazione = wtf.StringField('Annotazione', validators=[wtfv.Optional()])

class ClassiForm(FlaskForm):
    anno_corso = wtf.IntegerField('Anno corso', validators=[wtfv.NumberRange(min=1, max=5)])
    sezione = wtf.StringField('Sezione', validators=[wtfv.Length(min=1, max=1)])
    ordine = wtf.StringField('Ordine')
    indirizzo = wtf.StringField('Indirizzo')