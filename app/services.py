from character import *
from dialect_enums import *
from pronunciation import *
from data.mysql_repo import *

class Services:

    def __init__(self):
        self.mysql = MysqlRepository()
    def get_all_pronunciations(self, param):
        character = Chinese_character(self.mysql.get_row(param)[1])
        gloss = character.english_gloss()
        pronunciations_string = ",".join(map(str, self.mysql.get_row(param)[2:]))
        pronunciations = Pronunciation(pronunciations_string)
        pronunciations_list =  pronunciations.transcription.split(",")
        output_template
        """
        record = (
            chinese_character,
            pronunciations.get('Mandarin', None),
            pronunciations.get('Cantonese', None),
            pronunciations.get('Hakka', None),
            pronunciations.get('Wu', None),
            pronunciations.get('Xiang', None),
            pronunciations.get('Min Nan', None),
            pronunciations.get('Jin', None),
            pronunciations.get('Gan', None)
        )
        """
