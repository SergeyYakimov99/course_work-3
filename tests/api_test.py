from run import app


class TestApi:

    def test_app_all_posts(self):
        """ Проверяем получение правильного списка постов"""
        response = app.test_client().get('api/posts', follow_redirects=True)

        assert response.status_code == 200, "Статус-код запроса всех постов неверен"
        assert response.mimetype == "application/json", "Получен не json"

    def test_app_one_posts(self):
        """ Проверяем получение правильного списка для одного поста"""
        response = app.test_client().get('api/posts/1', follow_redirects=True)

        assert response.status_code == 200, "Статус-код запроса всех постов неверен"
        assert response.mimetype == "application/json", "Получен не json"
