# Roann Yanes, Abby Gervase, and Grace Milton

import unittest
import requests
import json

class TestAuthors(unittest.TestCase):

    PORT_NUM = '51082'
    print("Testing Port number: ", PORT_NUM)
    SITE_URL = 'http://student04.cse.nd.edu:' + PORT_NUM
    AUTHORS_URL = SITE_URL + '/authors/'
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

    def test_authors_get(self):
        self.reset_data()
        author_id = 300
        r = requests.get(self.AUTHORS_URL + str(author_id))
        self.assertTrue(self.is_json(r.content.decode()))
        resp = json.loads(r.content.decode())
        self.assertEqual(resp['books'], [8579016, 52529, 13237327])

if __name__ == "__main__":
    unittest.main()

