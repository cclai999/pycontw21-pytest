from typing import List
from datetime import date
import pytest

import lib
import pytest_mock


# 需要使用到外部的 resource, get_operations_from_db()
def test_room601_exception():
    room = '601'
    operations = lib.all_operations(date(2021, 7, 13), room)
    assert all(op.room == room for op in operations)


def test_room601_operations_true(operation_data: List[lib.Operation],
                                 mocker: pytest_mock.MockFixture):
    mocker.patch('lib.get_operations_from_db',
                 autospec=True,
                 return_value=operation_data)
    room = '601'
    operations = lib.all_operations(date(2021, 7, 13), room)
    assert all(op.room == room for op in operations)
