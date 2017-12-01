import unittest
import requests
import json
import sys

class TestBooksDelOnly(unittest.TestCase):

    PORT_NUM = '51082' #change port number to match your port number
    print("Testing Port number: ", PORT_NUM)
    SITE_URL = 'http://student04.cse.nd.edu:' + PORT_NUM
    BOOKS_URL = SITE_URL + '/books/'
    RESET_URL = SITE_URL + '/reset/'

    def reset_data(self):
        b = {}
        r = requests.put(self.RESET_URL, data = json.dumps(b))

    def is_json(self, resp):
        try:
            json.loads(resp)
            return True
        except ValueError:
            return False

    def test_movies_delete(self):
        self.reset_data()
        book_id = 6479259

        b = {}
        r = requests.delete(self.BOOKS_URL + str(book_id), data = json.dumps(b))
        self.assertTrue(self.is_json(r.content))
        resp = json.loads(r.content)
        self.assertEqual(resp['result'], 'success')

        r = requests.get(self.BOOKS_URL + str(book_id))
        self.assertTrue(self.is_json(r.content))
        resp = json.loads(r.content)
        self.assertEqual(resp['result'], 'error')

if __name__ == "__main__":
    unittest.main()

