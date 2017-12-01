# Abby Gervase, Grace Milton, and Roann Yanes

import unittest
import requests
import json
import sys

class TestBooksIndex(unittest.TestCase):

    PORT_NUM = '51082'
    print("Testing port number: ",PORT_NUM)
    SITE_URL = 'http://student04.cse.nd.edu:' + PORT_NUM
    BOOKS_URL = SITE_URL + '/books/'
    RESET_URL = SITE_URL + '/reset/'

    def reset_data(self):
        b = {}
        r = requests.put(self.RESET_URL, json.dumps(b))

    def is_json(self, resp):
        try:
            json.loads(resp)
            return True
        except ValueError:
            return False

    def test_books_index_get(self):
        self.reset_data()
        r = requests.get(self.BOOKS_URL)
        self.assertTrue(self.is_json(r.content.decode()))
        resp = json.loads(r.content.decode())

        books = resp['books']
        for book in books:
            if book['id'] == 150037:
                testbook = book

        self.assertEqual(testbook['authors'], ['Lemony Snicket', ' Brett Helquist'])
        self.assertEqual(testbook['title'], 'The Vile Village (A Series of Unfortunate Events, #7)')
        self.assertEqual(testbook['year'], 2001)

    def test_books_index_post(self):
        self.reset_data()

        b = {}
        b['authors'] = ['Roann Yanes']
        b['title'] = 'My Life as Morty'
        b['year'] = 2017
        r = requests.post(self.BOOKS_URL, data = json.dumps(b))
        self.assertTrue(self.is_json(r.content.decode()))
        resp = json.loads(r.content.decode())
        self.assertEqual(resp['result'], 'success')
        self.assertEqual(resp['id'], 10001)

        r = requests.get(self.BOOKS_URL + str(resp['id']))
        self.assertTrue(self.is_json(r.content.decode()))
        resp = json.loads(r.content.decode())
        self.assertEqual(resp['authors'], b['authors'])
        self.assertEqual(resp['title'], b['title'])
        self.assertEqual(resp['year'], b['year'])

    def test_books_index_delete(self):
        self.reset_data()

        b = {}
        r = requests.delete(self.BOOKS_URL, data = json.dumps(b))
        self.assertTrue(self.is_json(r.content.decode()))
        resp = json.loads(r.content.decode())
        self.assertEqual(resp['result'], 'success')

        r = requests.get(self.BOOKS_URL)
        self.assertTrue(self.is_json(r.content.decode()))
        resp = json.loads(r.content.decode())
        books = resp['books']
        self.assertFalse(books)

if __name__ == "__main__":
    unittest.main()

