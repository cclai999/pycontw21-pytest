from datetime import datetime
import pytest
import pytest_mock

from book import datetime, book_vaccine


def test_book_b4_begin_time(mocker):
    fake_time = datetime(2021, 6, 14, 7, 59)
    mocker.patch('datetime.now', return_value=fake_time)
    result = book_vaccine()
    assert result == "2021-06-14 08：00 才能預約"


def test_book_after_begin_time(mocker):
    fake_time = datetime(2021, 6, 14, 8, 00)
    mocker.patch('datetime.now', return_value=fake_time)
    result = book_vaccine()
    assert result == "開始預約"

