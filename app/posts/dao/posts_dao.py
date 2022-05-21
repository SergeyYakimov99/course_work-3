import json


class PostsDAO:

    """ Работа со всеми постами"""

    def __init__(self, path):
        self.path = path


    def _load(self):
        with open(f"{self.path}", "r", encoding="utf-8") as file:
            data = json.load(file)
        return data


    def get_all(self):
        """ Выводит все посты"""
        return self._load()


    def get_by_pk(self, pk):
        """ Выводит пост по номеру"""
        posts = self.get_all()

        for post in posts:
            if post["pk"] == pk:
                return post


    def get_by_user(self, user_name):
        """ Выводит пост пользователя по имени"""

        posts = self.get_all()
        posts_by_user = []

        for post in posts:
            if post['poster_name'] == user_name:
                posts_by_user.append(post)

        return posts_by_user


    def search(self, query):
        """ Возвращает список словарей по вхождению query"""

        posts = self.get_all()
        matching_posts = []

        for post in posts:
            if query.lower() in post["content"].lower():
                matching_posts.append(post)
        return matching_posts
