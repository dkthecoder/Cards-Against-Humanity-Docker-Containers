from app import app
from flask import url_for
from unittest.mock import patch
from flask_testing import TestCase
import pytest


class TestBase(TestCase):
    def create_app(self):
        return app

    def test_length(self):
        response = self.client.get(url_for('get_wc_length'))
        self.assertEqual(int(response) == 457, True)
        self.assertEqual(response.status_code, 200)

    # def test_read_all(self):
        #response = self.client.get(url_for('read_all_wc'))
        #self.assertEqual(response.status_code, 200)

    # fix this test
    def test_retrieve_card(self):
        response = self.client.get(
            url_for('retrieve_wc', params={"index": str(0)}))
        self.assertEqual(str(response) == "____ ? There's a app for that.", True)
        self.assertEqual(response.status_code, 200)

    # fix this test
    def test_delete_card(self):
        response = self.client.get(
            url_for('delete_wc', params={"index": str(0)}))
        self.assertEqual(response.status_code, 200)
        response = self.client.get(
            url_for('retrieve_wc', params={"index": str(0)}))
        self.assertEqual(str(response) == "Man meat", True)
        self.assertEqual(response.status_code, 200)

    # fix this test
    def test_add_card(self):
        response = self.client.get(
            url_for('add_wc', params={"card": "Here's a new card to add"}))
        self.assertEqual(response.status_code, 200)
        response = self.client.get(
            url_for('retrieve_wc', params={"index": str(457)}))
        self.assertEqual(str(response) == "Here's a new card to add", True)
        self.assertEqual(response.status_code, 200)
