from typing import List, Optional
from datetime import datetime, date


class Operation:
    def __init__(self, op_id: str, patient_id: str,
                 room: int, op_time: datetime = None):
        self.op_id = op_id
        self.patient_id = patient_id
        self.room = room
        self.op_time = op_time


def all_operations(op_date: date, room: str) -> List[Operation]:

    ops = get_operations_from_db(op_date)
    log(f"Query for room-'{room}'")
    if room == 'all':
        return ops

    return [
        g
        for g in ops
        if g.room == room
    ]


def get_operations_from_db(op_date: date):
    raise Exception("NO DB!")
    pass


def log(msg: str):
    # raise Exception("NO LOG!")
    print(f"實務上應該會 log 到檔案，不會在這邊看到。 msg: {msg}.")
