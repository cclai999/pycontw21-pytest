from typing import List
from datetime import datetime
import pytest
import lib


@pytest.fixture
def operation_data() -> List[lib.Operation]:
    # This op data simulates our unit_test data to avoid DB calls and dependencies.
    ops = [
        lib.Operation('A202107001', 'SL0001', '601', datetime(2021, 7, 13, 8, 00)),
        lib.Operation('A202107002', 'SL0002', '602', datetime(2021, 7, 13, 10, 00)),
        lib.Operation('A202107003', 'SL0003', '601', datetime(2021, 7, 13, 11, 00)),
        lib.Operation('A202107004', 'SL0004', '602', datetime(2021, 7, 13, 14, 00)),
        lib.Operation('A202107005', 'SL0005', '601', datetime(2021, 7, 13, 16, 00)),
    ]
    ops.sort(key=lambda op: op.op_time)
    return ops
