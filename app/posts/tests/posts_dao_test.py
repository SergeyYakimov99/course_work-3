import pytest

from app.posts.dao.posts_dao import PostsDAO

class TestPostsDao:

    @pytest.fixture()
    def posts_dao(self):
        return PostsDAO("data/posts.json")

    def test_get_all_check_type(self, posts_dao):
        posts = posts_dao.get_all()
        assert type(posts) == list, "Вывод постов должен быть списком"
        assert type(posts[0]) == dict, "Каждый пост должен быть словарем"

