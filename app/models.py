from app import db 
from sqlalchemy.inspection import inspect

class Rappresentable:

    def __repr__(self) -> str:
        attrs = [getattr(self, attr) for attr in inspect(self.__class__).c.keys()]
        repr = '<{}:' + ''.join(['\n  {},' for attr in attrs][:-1]) + '\n>'
        return repr.format(self.__class__.__name__, *attrs)
