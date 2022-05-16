from flask import Blueprint, jsonify

api_blueprint = Blueprint('api_blueprint', __name__)


@api_blueprint.route('/api/posts/')
def posts_all():
    return jsonify({"content": "Все посты здесь"})


@api_blueprint.route('/api/posts/<int:post_pk>/')
def posts_one(post_pk):
    return jsonify({"content": "Страница одного поста"})


