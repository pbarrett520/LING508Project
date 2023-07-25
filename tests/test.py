import pytest
from app.character import *
from app.pronunciation import *
import re

def test_character():
    character = Chinese_character("大")
    bad_input = Chinese_character("big")
    assert isinstance(character.hanzi, str), "Type must be string"
    assert re.search("[\u4e00-\u9FFF]", character.hanzi), "Must be a unicode Chinese character"
    assert len(character.hanzi().split()) == 1, "Must be a single character"
    assert bad_input.__init__() == bad_input.hanzi_error, "Something else is wrong with the input"

def test_pronunciation():
    pass