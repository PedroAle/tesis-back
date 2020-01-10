from django.test import TestCase
""" import unittest
from sqlite3 import Error
from api.services.connection import create_connection
import sqlite3
import sys
import os
import json
from api.terms import views """

# Create your tests here.
""" class Tesis_TestCase(unittest.TestCase):

    def setUp(self):
        self.add_tesis()

    def add_tesis(self):
        conn = create_connection('db.sqlite3')
        cur = conn.cursor()
        cur.execute("INSERT INTO api_term(term) VALUES ('2221')")
        conn.commit()
    
    def test_addterm(self):
        json_result = views.get_terms
        # print(json_result)
        self.assertEqual(1, len(json_result))

    def tearDown(self):
        conn = create_connection('db.sqlite3')
        cur = conn.cursor()
        cur.execute("DELETE FROM api_term")
        conn.commit() """
        
