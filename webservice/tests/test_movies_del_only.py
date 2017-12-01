import unittest
import requests
import json
import sys

class TestMoviesDelOnly(unittest.TestCase):

    PORT_NUM = '51082' #change port number to match your port number
    print("Testing Port number: ", PORT_NUM)
    SITE_URL = 'http://student04.cse.nd.edu:' + PORT_NUM
    MOVIES_URL = SITE_URL + '/movies/'
    RESET_URL = SITE_URL + '/reset/'

    def reset_data(self):
        m = {}
        r = requests.put(self.RESET_URL, data = json.dumps(m))

    def is_json(self, resp):
        try:
            json.loads(resp)
            return True
        except ValueError:
            return False

    def test_movies_delete(self):
        self.reset_data()
        movie_id = 95

        m = {}
        r = requests.delete(self.MOVIES_URL + str(movie_id), data = json.dumps(m))
        self.assertTrue(self.is_json(r.content))
        resp = json.loads(r.content)
        self.assertEquals(resp['result'], 'success')

        r = requests.get(self.MOVIES_URL + str(movie_id))
        self.assertTrue(self.is_json(r.content))
        resp = json.loads(r.content)
        self.assertEquals(resp['result'], 'error')

if __name__ == "__main__":
    unittest.main()

