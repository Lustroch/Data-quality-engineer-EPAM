# Для HTTP запросов с методом GET на URL - https://jsonplaceholder.typicode.com/users
# Создайте следующие тесты:
# 1) Проверка кода ответа: status code is 200 OK
# 2) Проверка заголовка ответа (response header):
# - the content-type header exists in the obtained response
# - the value of the content-type header is application/json; charset=utf-8
# 3) Проверка тела ответа (response body):
# - the content of the response body is the array of 10 users (JSON)
# - Tests should be done using the provided REST web-service.


import pytest
import requests
from unittest import TestCase


class APITesting(TestCase):
    def req(self):
        response = requests.get('https://jsonplaceholder.typicode.com/users')
        return response


    def test_code_answer(self):
        assert self.req().status_code == 200


    def test_response_header(self):
        assert self.req().headers['Content-Type']
        assert self.req().headers['Content-Type'] == 'application/json; charset=utf-8'


    def test_response_body(self):
        body_length = len(self.req().json())
        assert body_length == 10
        for i in range(body_length):
            assert self.req().json()[i]['id']
            assert self.req().json()[i]['username']
