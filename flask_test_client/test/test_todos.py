# from flask import url_for
# from app.models import Task
# from app import routes


def test_add_task_should_return_task3(client):
    new_item = {'title': '買牛奶', 'note': '2瓶'}
    resp = client.post("/api/tasks", json=new_item)
    assert resp.status_code == 201
    json_data = resp.get_json()
    assert json_data['task']['id'] == 3
    assert json_data['task']['title'] == '買牛奶'
    assert json_data['task']['note'] == '2瓶'


# def test_add_task_wo_title_should_return_error(client):
#     new_item = {'note': '2瓶'}
#     resp = client.post("/api/tasks", json=new_item)
#     assert resp.status_code == 400


def test_query_tasks_with_2_rows_should_return_2_tasks(client):
    resp = client.get("/api/tasks")
    assert resp.status_code == 200
    json_data = resp.get_json()
    assert len(json_data['tasks']) == 2


def test_query_task3_with_2_rows_should_return_error(client):
    resp = client.get("/api/tasks/3")
    assert resp.status_code == 404
    json_data = resp.get_json()
    assert json_data['error'] == 'object not found!!!'

