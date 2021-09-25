import math


def test_sqrt():
    num = 25
    assert math.sqrt(num) == 5


def test_square():
    num = 7
    # assert 7 * 7 == 40      # 49
    assert 7 * 7 == 49      # 49


def test_equality():
    # assert 10 == 11         # 10
    assert 10 != 11         # 10
