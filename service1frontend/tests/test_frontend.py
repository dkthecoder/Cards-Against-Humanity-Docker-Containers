from app import app
from flask import url_for
from flask_testing import TestCase
import pytest


class TestBase(TestCase):
    def create_app(self):
        return app

    def test_home_repsonce(self):
        response = self.client.get(url_for('index'))
        self.assertEqual(response.status_code, 200)

    def test_play_repsonce(self):
        response = self.client.get(url_for('play'))
        self.assertEqual(response.status_code, 200)

    def test_home_repsonce(self):
        response = self.client.get(url_for('rules'))
        self.assertEqual(response.status_code, 200)

    def test_home_repsonce(self):
        response = self.client.get(url_for('black_cards'))
        self.assertEqual(response.status_code, 200)

    def test_home_repsonce(self):
        response = self.client.get(url_for('white_cards'))
        self.assertEqual(response.status_code, 200)
