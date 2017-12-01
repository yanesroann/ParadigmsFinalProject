# Roann Yanes, Abby Gervase, and Grace Milton

import unittest
import requests
import json

class TestGenres(unittest.TestCase):

    PORT_NUM = '51082'
    print("Testing Port number: ", PORT_NUM)
    SITE_URL = 'http://student04.cse.nd.edu:' + PORT_NUM
    GENRES_URL = SITE_URL + '/genres/'
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

    def test_genres_get(self):
        self.reset_data()
        genre_id = 312
        r = requests.get(self.GENRES_URL + str(genre_id))
        self.assertTrue(self.is_json(r.content.decode()))
        resp = json.loads(r.content.decode())
        self.assertEqual(resp['books'], [824763])

if __name__ == "__main__":
    unittest.main()

