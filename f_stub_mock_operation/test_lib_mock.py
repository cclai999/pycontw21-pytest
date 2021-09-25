from typing import List
from datetime import date

import lib
import pytest_mock


def test_room602_operations_log(operation_data: List[lib.Operation],
                                mocker: pytest_mock.MockFixture):
    mocker.patch('lib.get_operations_from_db',
                 autospec=True,
                 return_value=operation_data)
    mock_log = mocker.patch('lib.log', autospec=True)

    room = '602'
    operations = lib.all_operations(date(2021, 7, 13), room)
    assert len(operations) == 2
    mock_log.assert_called_once_with(f"Query for room-'602'")


def test_room602_operations_log_with_spy(operation_data: List[lib.Operation],
                                mocker: pytest_mock.MockFixture):
    mocker.patch('lib.get_operations_from_db',
                 autospec=True,
                 return_value=operation_data)
    mock_log = mocker.spy(lib, 'log')
    room = '602'
    operations = lib.all_operations(date(2021, 7, 13), room)
    assert len(operations) == 2
    mock_log.assert_called_once_with(f"Query for room-'602'")


