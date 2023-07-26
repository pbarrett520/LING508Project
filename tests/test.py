import pytest
from app.character import *
from app.pronunciation import *
import re

def test_character():
    character = Chinese_character("大")
    bad_input = Chinese_character("big")
    assert isinstance(character.hanzi, str), "Type must be string"
    assert character.hanzi_error == None, "Must be a unicode Chinese character"
    assert bad_input.hanzi_error == bad_input.HANZI_ERROR

def test_pronunciation():
    pass