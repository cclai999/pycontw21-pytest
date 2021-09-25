import pytest

from triangle import is_valid_triangle, type_of_triangle


def test_is_valid_triangle():
    with pytest.raises(ValueError):
        result = is_valid_triangle("a", 1, 3)


def test_is_valid_triangle_with_valid_case():
    expected = True
    assert is_valid_triangle(2, 2, 3) == expected
    # assert is_valid_triangle(2, 2, 3) == True


def test_is_valid_triangle_with_invalid_case():
    expected = False
    assert is_valid_triangle(1, 2, 3) == expected
    # assert is_valid_triangle(1, 2, 3) == False


@pytest.mark.parametrize("a,b,c,expected", [
    (0, 1, 3, "不是三角形"),
    (1, 1, 1, "等邊三角形"),
    (2, 2, 3, "等腰三角形"),
    (3, 4, 5, "直角三角形"),
    (4, 5, 6, "一般三角形")
])
def test_type_of_triangle(a, b, c, expected):
    assert expected == type_of_triangle(a, b, c)
