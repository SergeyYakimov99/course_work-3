import pytest

from app.posts.dao.comments_dao import CommentsDAO

class TestCommentsDao:

    @pytest.fixture()
    def comments_dao(self):
        return CommentsDAO("app/posts/tests/mock/comments.json")


    @pytest.fixture()
    def keys_expected(self):
        return {"post_pk", "commenter_name", "comment", "pk"}

# тест на получение всех комментариев к посту

    def test_get_by_post_pk_check_type(self, comments_dao):
        comments = comments_dao.get_by_post_pk(1)
        assert type(comments) == list, "Вывод комментариев должен быть списком"
        assert type(comments[0]) == dict, "Каждый комментарий должен быть словарем"


    def test_get_by_post_pk_check_keys(self, comments_dao, keys_expected):
        comment = comments_dao.get_by_post_pk(1)[0]
        comment_keys = set(comment.keys())
        assert comment_keys == keys_expected, "Список ключей не соответствует"

    parameters_for_posts_and_comments = [
        (1,{1,2}),
        (2,{7}),
        (0,set())
    ]

    @pytest.mark.parametrize("post_pk, correct_comments_pks", parameters_for_posts_and_comments)
    def test_get_by_post_pk_check_math(self, comments_dao, post_pk, correct_comments_pks):
        comments = comments_dao.get_by_post_pk(post_pk)
        comments_pks = set([comment["pk"] for comment in comments])
        assert comments_pks == correct_comments_pks, f"не совпадают pk комментариев для поста {post_pk}"


