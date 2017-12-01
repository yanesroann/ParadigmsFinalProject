# Roann Yanes. Abby Gervase, and Grace Milton

import unittest
import requests
import json

class TestGenresIndex(unittest.TestCase):

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

    def test_genres_index_get(self):
        self.reset_data()
        r = requests.get(self.GENRES_URL)
        self.assertTrue(self.is_json(r.content.decode()))
        resp = json.loads(r.content.decode())

        testgenre = {}

        genres = resp['genres']
        for genre in genres:
            if genre['genre'] == 303:
                testgenre = genre

        self.assertEqual(testgenre['books'], [56728])


if __name__ == "__main__":
    unittest.main()

