from flask import Blueprint, render_template, request

posts_blueprint = Blueprint('posts_blueprint', __name__, template_folder='templates')

@posts_blueprint.route('/')
def posts_all():
    return 'Все посты здесь'


@posts_blueprint.route('/posts/<int:post_pk>/')
def posts_one(post_pk):
    return 'Страница одного поста'


@posts_blueprint.route('/search')
def posts_search():
    return 'Поиск по постам'


@posts_blueprint.route('/users/<username>/')
def posts_by_user(username):
    return 'Поиск по пользователю'