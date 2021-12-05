import requests_mock
import pytest
from flask import url_for
from flask_testing import TestCase

from service4magicmaker import app

class TestBase(TestCase):
    def create_app(self):
        return app

    def create_app():
        app.config.update(DEBUG=True)
        return app

    def test_random_number_generator(self):
        response = self.client.get(url_for('ran_num_gen', params = {"star":str(1), "end":str(100)}))
        self.assertEqual(int(response) <= 100 and int(response) >= 1, True)
        self.assertEqual(response.status_code, 200)

    def test_rand_numbers_from_word(self):
        response = self.client.get(url_for('ran_num_word', start=1, end=100, num=10, word="kittykat"))
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response != "")
