import requests_mock
import pytest
from flask import url_for
from service2blackcards import app
from unittest.mock import patch


def create_app():
    app.config.update(DEBUG=True)
    return app


def test_length(self):
    response = self.client.get(url_for('get_bc_length'))
    self.assertEqual(response.status_code, 200)

def test_read_all(self):
    response = self.client.get(url_for('read_all_bc'))
    self.assertEqual(response.status_code, 200)

#fix this test
def test_retrieve_card(self):
    response = self.client.get(url_for('retrieve_bc'))
    self.assertEqual(response.status_code, 200)

#fix this test
def test_delete_card(self):
    response = self.client.get(url_for('delete_bc'))
    self.assertEqual(response.status_code, 200)

#fix this test
def test_add_card(self):
    response = self.client.get(url_for('add_bc'))
    self.assertEqual(response.status_code, 200)