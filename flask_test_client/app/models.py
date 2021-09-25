from datetime import datetime
from app import db


def is_done_str(done):
    return "done" if done else "todo"


class Task(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(64))
    note = db.Column(db.String(128))
    done = db.Column(db.Boolean, index=True)

    def to_dict(self):
        data = {
            'id': self.id,
            'title': self.title,
            'note': self.note,
            'done': is_done_str(self.done),
        }
        return data

    def __repr__(self):
        return f'<Task-{self.id}>, [{self.title}], status:{is_done_str(self.done)}'

