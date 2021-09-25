from flask import Blueprint
from flask import jsonify, abort, request, make_response
from app import db
from app.models import Task

bp = Blueprint('api', __name__, url_prefix='/api')


@bp.errorhandler(404)
def not_found(err):
    return make_response(jsonify({'error': 'object not found!!!'}), 404)


@bp.errorhandler(400)
def bad_request(err):
    if err.description:
        return make_response(jsonify({'error': err.description}), 400)
    return make_response(jsonify({'error': 'bad request!!!'}), 400)


@bp.route('/create_db')
def index():
    db.create_all()
    return 'DB is created successfully!'


@bp.route('/tasks', methods=['GET'])
def get_tasks():
    tasks = Task.query.all()
    return jsonify({'tasks': [t.to_dict() for t in tasks]})


@bp.route('/tasks/<int:task_id>', methods=['GET'])
def get_task(task_id):
    task = Task.query.filter_by(id=task_id).first_or_404()
    return jsonify({'task': task.to_dict()})


@bp.route('/tasks', methods=['POST'])
def create_task():
    if request.json is None or 'title' not in request.json:
        abort(400)
    task = Task(
        title=request.json['title'],
        note=request.json.get('note', ''),
        done=False
    )
    db.session.add(task)
    db.session.commit()
    return jsonify({'task': task.to_dict()}), 201


@bp.route('/tasks/<int:task_id>', methods=['DELETE'])
def delete_task(task_id):
    task = Task.query.filter_by(id=task_id).first_or_404()
    db.session.delete(task)
    db.session.commit()
    return jsonify({'result': True})


@bp.route('/tasks/<int:task_id>', methods=['PUT'])
def update_task(task_id):
    task = Task.query.filter_by(id=task_id).first()
    if task is None:
        abort(404)
    if request.json is None:
        abort(400, "No JSON data!!!")
    if 'title' in request.json and type(request.json['title']) != str:
        abort(400, "title field is not a string!!!")
    if 'note' in request.json and type(request.json['note']) != str:
        abort(400, "note field is not a string!!!")
    if 'done' in request.json and type(request.json['done']) != bool:
        abort(400, "done field is not boolean!!!")

    task.title = request.json.get('title', task.title)
    task.note = request.json.get('note', task.note)
    task.done = request.json.get('done', task.done)
    db.session.commit()
    return jsonify({'task': task.to_dict()})
