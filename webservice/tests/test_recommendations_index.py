import unittest
import requests
import json

class TestRecommendationsIndex(unittest.TestCase):

    PORT_NUM = '51082' #change port number to match your port number
    print("Testing Port number: ", PORT_NUM)
    SITE_URL = 'http://student04.cse.nd.edu:' + PORT_NUM
    RECOMMENDATIONS_URL = SITE_URL + '/recommendations/'
    RESET_URL = SITE_URL + '/reset/'

    def reset_data(self):
        m = {}
        r = requests.put(self.RESET_URL, json.dumps(m))

    def is_json(self, resp):
        try:
            json.loads(resp)
            return True
        except ValueError:
            return False

    def test_recommendations_index_delete(self):
        self.reset_data()

        m = {}
        r = requests.delete(self.RECOMMENDATIONS_URL, data = json.dumps(m))
        self.assertTrue(self.is_json(r.content.decode()))
        resp = json.loads(r.content.decode())
        self.assertEqual(resp['result'], 'success')

if __name__ == "__main__":
    unittest.main()

