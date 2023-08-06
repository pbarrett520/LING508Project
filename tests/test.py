import pytest
from app.character import *
from app.dialect_enums import *
from app.pronunciation import *

def test_character():
    character = Chinese_character("大")
    bad_input = Chinese_character("big")
    assert isinstance(character.hanzi, str), "Type must be string"
    assert character.hanzi_error == None, "Must be a unicode Chinese character"
    assert bad_input.hanzi_error == bad_input.HANZI_ERROR

def test_pronunciation():
    pron = Pronunciation("da4", Dialect.STANDARD_MANDARIN)
    bad_pron = Pronunciation(33, "Mandarin")
    assert isinstance(pron.transcription, str), "Must be type str"
    assert isinstance(pron.dialect, Dialect), "Must be type dialect"
    assert bad_pron.hanzi == None, "Checking character input for wrong data type"
    assert bad_pron.dialect == None, "Checking dialect input for wrong data type"


