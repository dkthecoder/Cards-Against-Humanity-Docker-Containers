import requests_mock
import pytest
import unittest
from flask import url_for
from service2blackcards import app
from unittest.mock import patch
from flask_testing import TestCase

class TestBase(TestCase):
    def create_app(self):
        return app

    def test_length(self):
        response = self.client.get(url_for('get_bc_length'))
        self.assertEqual(int(response) == 89, True)
        self.assertEqual(response.status_code, 200)

    #def test_read_all(self):
        #response = self.client.get(url_for('read_all_bc'))
        #self.assertEqual(response.status_code, 200)

    #fix this test
    def test_retrieve_card(self):
        response = self.client.get(url_for('retrieve_bc', params = {"index":str(0)}))
        self.assertEqual(str(response) == "Coat hanger abortions", True)
        self.assertEqual(response.status_code, 200)

    #fix this test
    def test_delete_card(self):
        response = self.client.get(url_for('delete_bc', params = {"index":str(0)}))
        self.assertEqual(response.status_code, 200)
        response = self.client.get(url_for('retrieve_bc', params = {"index":str(0)}))
        self.assertEqual(str(response) == "Why can't I sleep at night ?", True)
        self.assertEqual(response.status_code, 200)

    #fix this test
    def test_add_card(self):
        response = self.client.get(url_for('add_bc', params = {"card":"Here's a new card to add"}))
        self.assertEqual(response.status_code, 200)
        response = self.client.get(url_for('retrieve_bc', params = {"index":str(89)}))
        self.assertEqual(str(response) == "Here's a new card to add", True)
        self.assertEqual(response.status_code, 200)