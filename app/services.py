# from data.mysql_repo import MysqlRepository
from .character import *
from .pronunciation import *
from data.mysql_repo import *


class Services:

    def __init__(self):
        self.mysql = MysqlRepository()

    def get_dialect(self, character: str, dialect: str) -> dict: # fufills use case. Takes a characcter and a dialect
        character = self.mysql.get_character(character)
        pronunciation = self.mysql.get_pronunciation(character.hanzi, dialect)
        output_template = {
            "character": character.hanzi,
            "gloss": character.english_gloss,
            "pronunciation": pronunciation.transcription
        }
        return output_template