import pytest
from data.mysql_repo import *
def test_data():

    sql_test = MysqlRepository()
    entries = sql_test.get_entries()
    cjk_range_min = 0x4E00
    cjk_range_max = 0x9FFF
    sample_code_point = ord(entries[3][1])
    assert sql_test.get_entries() != None
    assert isinstance(entries[3][0],int)
    assert sample_code_point in range(cjk_range_min, cjk_range_max)