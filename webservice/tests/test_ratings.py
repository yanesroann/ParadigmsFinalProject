# Abby Gervase, Grace Milton, and Roann Yanes

import unittest
import requests
import json

class TestRatings(unittest.TestCase):

    PORT_NUM = '51082' #change port number to match your port number
    print("Testing Port number: ", PORT_NUM)
    SITE_URL = 'http://student04.cse.nd.edu:' + PORT_NUM
    RATINGS_URL = SITE_URL + '/ratings/'
    RESET_URL = SITE_URL + '/reset/'

    def reset_data(self):
        b = {}
        r = requests.put(self.RESET_URL)

    def is_json(self, resp):
        try:
            json.loads(resp)
            return True
        except ValueError:
            return False

    def test_ratings_get(self):
        self.reset_data()
        book_id = 1914973

        r = requests.get(self.RATINGS_URL + str(book_id))
        self.assertTrue(self.is_json(r.content.decode()))
        resp = json.loads(r.content.decode())
        self.assertEqual(resp['rating'], 4.048714529616291)
        self.assertEqual(resp['book_id'], book_id)

if __name__ == "__main__":
    unittest.main()

