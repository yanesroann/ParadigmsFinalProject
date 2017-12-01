# Grace Milton, Abby Gervase, and Roann Yanes
import unittest
import requests
import json

class TestBooks(unittest.TestCase):

    PORT_NUM = '51082'
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

    def test_books_get(self):
        self.reset_data()
        book_id = 4407
        r = requests.get(self.BOOKS_URL + str(book_id))
        self.assertTrue(self.is_json(r.content.decode('utf-8')))
        resp = json.loads(r.content.decode('utf-8'))
        self.assertEqual(resp['title'], 'American Gods (American Gods, #1)')
        self.assertEqual(resp['year'], 2001)
        self.assertEqual(resp['authors'], ["Neil Gaiman"])
        self.assertEqual(resp['img'], 'https://images.gr-assets.com/books/1258417001m/4407.jpg')

    def test_books_put(self):
        self.reset_data()
        book_id = 17231

        r = requests.get(self.BOOKS_URL + str(book_id))
        self.assertTrue(self.is_json(r.content.decode('utf-8')))
        resp = json.loads(r.content.decode('utf-8'))
        self.assertEqual(resp['authors'], ["Jeff Lindsay"])
        self.assertEqual(resp['title'], 'Darkly Dreaming Dexter (Dexter, #1)')
        self.assertEqual(resp['year'], 2004)

        b = {}
        b['authors'] = ['Roann Yanes']
        b['title'] = 'My Life as Morty'
        b['year'] = 2017
        r = requests.put(self.BOOKS_URL + str(book_id), data = json.dumps(b))
        self.assertTrue(self.is_json(r.content.decode('utf-8')))
        resp = json.loads(r.content.decode('utf-8'))
        self.assertEqual(resp['result'], 'success')

        r = requests.get(self.BOOKS_URL + str(book_id))
        self.assertTrue(self.is_json(r.content.decode('utf-8')))
        resp = json.loads(r.content.decode('utf-8'))
        self.assertEqual(resp['authors'], b['authors'])
        self.assertEqual(resp['title'], b['title'])
        self.assertEqual(resp['year'], b['year'])

    def test_books_delete(self):
        self.reset_data()
        book_id = 17231

        b = {}
        r = requests.delete(self.BOOKS_URL + str(book_id), data = json.dumps(b))
        self.assertTrue(self.is_json(r.content.decode('utf-8')))
        resp = json.loads(r.content.decode('utf-8'))
        self.assertEqual(resp['result'], 'success')

        r = requests.get(self.BOOKS_URL + str(book_id))
        self.assertTrue(self.is_json(r.content.decode('utf-8')))
        resp = json.loads(r.content.decode('utf-8'))
        self.assertEqual(resp['result'], 'error')

if __name__ == "__main__":
    unittest.main()

