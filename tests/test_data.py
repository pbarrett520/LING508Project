import pytest
from data.mysql_repo import *
from app.character import *
from app.pronunciation import *
def test_data():
    # initialize values
    sql_test = MysqlRepository()
    entries = sql_test.get_all_entries()
    one_character = sql_test.get_character("上")
    print([one_character.hanzi, one_character.english_gloss])
    one_pronunciation = sql_test.get_pronunciation("上", "Mandarin")
    print(one_pronunciation.transcription)
    cjk_range_min = 0x4E00
    cjk_range_max = 0x9FFF
    sample_code_point = ord(entries[3][1])
    assert sql_test.get_all_entries() != None # make sure something is there
    assert isinstance(entries[3][0],int) # Make sure what's there is what's supposed to be there
    assert sample_code_point in range(cjk_range_min, cjk_range_max) # make sure the chinese character is actually a character according to unicode
    assert isinstance(one_character, Chinese_character) # make sure the correct datatype is returned when executing use case
    assert one_character.hanzi == "上" # make sure it's the right character
    assert isinstance(one_pronunciation, Pronunciation) # make sure the correct datatype is returned when executing use case
