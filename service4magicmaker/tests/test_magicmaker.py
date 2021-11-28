import requests_mock
import pytest
from flask import url_for
from service4magicmaker import app


def create_app():
    app.config.update(DEBUG=True)
    return app


def test_random_number_generator(self):
    response = self.client.get(url_for('random_number_generator', start = 1, end = 100, num = 10))
    self.assertEqual(response != "")
    self.assertEqual(response.status_code, 200)

def test_rand_numbers_from_word(self):
    response = self.client.get(url_for('rand_numbers_from_word', start = 1, end = 100, num = 10, word = "kittykat"))
    self.assertEqual(response.status_code, 200)
    self.assertEqual(response != "")
