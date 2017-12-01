# Roann Yanes, Abby Gervase, and Grace Milton

import unittest
import requests
import json

class TestAuthors(unittest.TestCase):

    PORT_NUM = '51082'
    print("Testing Port number: ", PORT_NUM)
    SITE_URL = 'http://student04.cse.nd.edu:' + PORT_NUM
    YEARS_URL = SITE_URL + '/years/'
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

    def test_years_get(self):
        self.reset_data()
        year = 1900
        r = requests.get(self.YEARS_URL + str(year))
        self.assertTrue(self.is_json(r.content.decode()))
        resp = json.loads(r.content.decode())
        self.assertEqual(resp['books'], [236093, 126609, 5693, 12194, 827685, 143513])

if __name__ == "__main__":
    unittest.main()

