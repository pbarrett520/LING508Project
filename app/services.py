#from data.mysql_repo import MysqlRepository
from .character import *
from .pronunciation import *
from data.mysql_repo import *

class Services:

    def __init__(self):
        self.mysql = MysqlRepository()

    def get_dialect(self,character, dialect):
        character = Chinese_character(character)
        pronunciation_string = self.mysql.get_pronunciation(character.hanzi, dialect)
        pronunciation = Pronunciation(pronunciation_string)
        output_template = f"\n{character.hanzi}: {character.english_gloss}\nDialect: {dialect}\nPronunciation: {pronunciation.transcription}"
        return output_template

if __name__ == '__main__': #Doesn't work this way either
    def test_services():
        services_test = Services()
        get_mandarin_shang = services_test.get_dialect("上","Mandarin")
        print(get_mandarin_shang)