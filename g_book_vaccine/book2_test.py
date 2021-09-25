from datetime import datetime
import pytest
import pytest_mock
import book2


def test_book_b4_begin_time(mocker):
    fake_time = begin_date_time = datetime(2021, 6, 14, 7, 59)
    mocker.patch('book2._get_now', return_value=fake_time)
    result = book2.book_vaccine()
    assert result == "2021-06-14 08：00 才能預約"


def test_book_after_begin_time(mocker):
    fake_time = begin_date_time = datetime(2021, 6, 14, 8, 10)
    mocker.patch('book2._get_now', return_value=fake_time)
    result = book2.book_vaccine()
    assert result == "開始預約"