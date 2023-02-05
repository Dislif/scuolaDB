from app import db 
from sqlalchemy.inspection import inspect

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
    #alunno = db.relationship('Alunno', backref='utente', uselist=False, lazy='dynamic')
    #profilo = db.relationship('Profilo', backref='utente', uselist=False, lazy='dynamic')
    #professore = db.relationship('Professore', backref='utente', uselist=False, lazy='dynamic')
    #genitore = db.relationship('Genitore', backref='utente', uselist=False, lazy='dynamic')

    def __repr__(self) -> str:
        return Rappresentable.__repr__(self)