import os
import sys
import pytest

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from app import create_app, db
from app.models import Task

tasks = [
    {
        'id': 1,
        'title': '交電話費',
        'note': '500元',
        'done': False
    },
    {
        'id': 2,
        'title': '錄教學影片',
        'note': 'rest api for todo app',
        'done': False
    }
]
# tasks = []


def add_init_tasks(test_db):
    for t in tasks:
        task = Task(
            title=t['title'],
            note=t['note'],
            done=False
        )
        test_db.session.add(task)
        test_db.session.commit()


@pytest.fixture
def client():
    os.environ['ENV'] = 'Test'
    app = create_app()
    app.config['SERVER_NAME'] = 'localhost'

    with app.test_client() as client:
        with app.app_context():
            db.create_all()
            add_init_tasks(db)
            yield client

            db.session.remove()
            db.drop_all()
