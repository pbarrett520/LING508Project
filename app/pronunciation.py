from .dialect_enums import *
from .character import *

class Pronunciation:
        def __init__(self,
                     hanzi: Chinese_character,
                     dialect:Dialect):


                if isinstance(hanzi,Chinese_character)== False:
                     self.hanzi = None
                else:
                     self.hanzi = hanzi

                if isinstance(dialect, Dialect) == False:
                        self.dialect = None
                else:
                        self.dialect = dialect
