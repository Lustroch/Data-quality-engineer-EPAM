# Для HTTP запросов с методом GET на URL - https://jsonplaceholder.typicode.com/users
# Создайте следующие тесты:
# 1) Проверка кода ответа: status code is 200 OK
# 2) Проверка заголовка ответа (response header):
# - the content-type header exists in the obtained response
# - the value of the content-type header is application/json; charset=utf-8
# 3) Проверка тела ответа (response body):
# - the content of the response body is the array of 10 users (JSON)
# - Tests should be done using the provided REST web-service.


import requests

response = requests.get('https://jsonplaceholder.typicode.com/users')


class TestAPI:

    @staticmethod
    def test_code_answer():
        assert response.status_code == 200

    @staticmethod
    def test_response_header():
        assert response.headers['Content-Type'] == 'application/json; charset=utf-8'

    @staticmethod
    def test_response_body():
        assert len(response.json()) == 10
