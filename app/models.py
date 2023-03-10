from app import db 
from sqlalchemy.inspection import inspect
from werkzeug.security import generate_password_hash, check_password_hash

class Rappresentable:

    def __repr__(self) -> str:
        attrs = [getattr(self, attr) for attr in inspect(self.__class__).c.keys()]
        repr = '<{}:' + ''.join(['\n  {},' for attr in attrs][:-1]) + '\n>'
        return repr.format(self.__class__.__name__, *attrs)

class Utente(db.Model, Rappresentable):
    __tablename__ = 'utenti'
    id = db.Column(db.Integer, primary_key=True)
    #username = db.Column(db.String(64), index=True, unique=True)
    email = db.Column(db.String(120), index=True, unique=True)
    hash_password = db.Column(db.String(255))

    alunno = db.relationship('Alunno', backref='utente', uselist=False)
    dati_anagrafici = db.relationship('Anagrafica', backref='utente', uselist=False)
    professore = db.relationship('Professore', backref='utente', uselist=False)
    genitore = db.relationship('Genitore', backref='utente', uselist=False)

    def set_password(self, password):
        self.hash_password = generate_password_hash(password)
    
    def check_password(self, password):
        return check_password_hash(self.hash_password, password)

    def __repr__(self) -> str:
        return Rappresentable.__repr__(self)

class Classe(db.Model, Rappresentable):
    __tablename__ = 'classi'
    id = db.Column(db.Integer, primary_key=True)
    anno_corso = db.Column(db.SmallInteger)
    sezione = db.Column(db.String(1))
    anno_scolastico = db.Column(db.Integer) #db.String(7)    es: 2017/18
    ordine = db.Column(db.String(255))
    indirizzo = db.Column(db.String(255))

    alunni = db.relationship('Alunno', backref='classe', lazy='dynamic')
    #materie = db.relationship('Materia', secondary='cattedre', back_populates='classi', lazy='dynamic')
    #professori = db.relationship('Professore', secondary='cattedre', back_populates='classi', lazy='dynamic')

    def __repr__(self) -> str:
        return Rappresentable.__repr__(self)

class Materia(db.Model, Rappresentable):
    __tablename__ = 'materie'
    id = db.Column(db.Integer, primary_key=True)
    nome = db.Column(db.String(255))
    classe_concorso = db.Column(db.String(5))
    
    voti = db.relationship('Voto', backref='materia', lazy='dynamic')
    #classi = db.relationship('Classe', secondary='cattedre', back_populates='materie', lazy='dynamic')
    #professori = db.relationship('Professore', secondary='cattedre', back_populates='materie', lazy='dynamic')
    
    def __repr__(self) -> str:
        return Rappresentable.__repr__(self)

class Anagrafica(db.Model, Rappresentable):
    __tablename__ = 'anagrafiche'
    id = db.Column(db.Integer, primary_key=True)
    #cf = db.Column(db.String(20), unique=True)
    nome = db.Column(db.String(64))
    cognome = db.Column(db.String(64))
    data_nascita = db.Column(db.Date)
    sesso = db.Column(db.String(255))
    indirizzo = db.Column(db.String(255))
    urbe = db.Column(db.String(255))
    telefono = db.Column(db.String(10), unique=True)
    utente_id = db.Column(db.Integer, db.ForeignKey('utenti.id'))

    def __repr__(self) -> str:
        return Rappresentable.__repr__(self)

class Alunno(db.Model, Rappresentable):
    __tablename__ = 'alunni'
    id = db.Column(db.Integer, primary_key=True)
    classe_id = db.Column(db.Integer, db.ForeignKey('classi.id'))
    utente_id = db.Column(db.Integer, db.ForeignKey('utenti.id'))

    genitori = db.relationship('Genitore', secondary='parentele', back_populates='figli', lazy='dynamic')
    voti = db.relationship('Voto', backref='alunno', lazy='dynamic')

    def __repr__(self) -> str:
        return Rappresentable.__repr__(self)
        
class Professore(db.Model, Rappresentable):
    __tablename__ = 'professori'
    id = db.Column(db.Integer, primary_key=True)
    classe_concorso = db.Column(db.String(5))
    utente_id = db.Column(db.Integer, db.ForeignKey('utenti.id'))

    #classi = db.relationship('Classe', secondary='cattedre', backref='professore', lazy='dynamic')
    #materie = db.relationship('Materia', secondary='cattedre', backref='professore', lazy='dynamic')

    def __repr__(self) -> str:
        return Rappresentable.__repr__(self)

class Genitore(db.Model, Rappresentable):
    __tablename__ = 'genitori'
    id = db.Column(db.Integer, primary_key=True)
    utente_id = db.Column(db.Integer, db.ForeignKey('utenti.id'))
    
    figli = db.relationship('Alunno', secondary='parentele', back_populates='genitori', lazy='dynamic')

    def __repr__(self) -> str:
        return Rappresentable.__repr__(self)

class Voto(db.Model, Rappresentable):
    __tablename__ = 'voti'
    id = db.Column(db.Integer, primary_key=True)
    valutazione = db.Column(db.Integer)
    annotazione = db.Column(db.String(255), nullable=True)
    data_valutazione = db.Column(db.Date)
    alunno_id = db.Column(db.Integer, db.ForeignKey('alunni.id'))
    materia_id = db.Column(db.Integer, db.ForeignKey('materie.id'))
    
    def __repr__(self) -> str:
        return Rappresentable.__repr__(self)
        
class Cattedra(db.Model, Rappresentable):
    __tablename__ = 'cattedre'
    id = db.Column(db.Integer, primary_key=True)
    materia_id = db.Column(db.Integer, db.ForeignKey('materie.id'))
    classe_id = db.Column(db.Integer, db.ForeignKey('classi.id'))
    professore_id = db.Column(db.Integer, db.ForeignKey('professori.id'))

    def __repr__(self) -> str:
        return Rappresentable.__repr__(self)

class Parentela(db.Model, Rappresentable):
    __tablename__ = 'parentele'
    id = db.Column(db.Integer, primary_key=True)
    alunno_id = db.Column(db.Integer, db.ForeignKey('alunni.id'))
    genitore_id = db.Column(db.Integer, db.ForeignKey('genitori.id'))

    def __repr__(self) -> str:
        return Rappresentable.__repr__(self)
