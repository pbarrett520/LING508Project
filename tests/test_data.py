import pytest
from data.mysql_repo import *
from app.character import *
from app.pronunciation import *
def test_data():

    sql_test = MysqlRepository()
    entries = sql_test.get_all_entries()
    one_character = sql_test.get_character("上")
    print([one_character.hanzi, one_character.english_gloss])
    one_pronunciation = sql_test.get_pronunciation("上", "Mandarin")
    print(one_pronunciation.transcription)
    cjk_range_min = 0x4E00
    cjk_range_max = 0x9FFF
    sample_code_point = ord(entries[3][1])
    assert sql_test.get_all_entries() != None
    assert isinstance(entries[3][0],int)
    assert sample_code_point in range(cjk_range_min, cjk_range_max)
    assert isinstance(one_character, Chinese_character)
    assert one_character.hanzi == "上"
    assert isinstance(one_pronunciation, Pronunciation)
# I recognize this should be a bit more complex, but I spent way too long debugging the web scraper script and playing with the sql to do more than this.
# Also my life has been consumed by packing as I prepare to move to the US next month