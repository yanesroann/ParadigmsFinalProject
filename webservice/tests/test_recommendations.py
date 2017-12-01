# Grace Milton, Abby Gervase, and Roann Yanes

import unittest
import requests
import json

class TestRecommendations(unittest.TestCase):

    PORT_NUM = '51082'
    print("Testing Port number: ", PORT_NUM)
    SITE_URL = 'http://student04.cse.nd.edu:' + PORT_NUM
    RECOMMENDATIONS_URL = SITE_URL + '/recommendations/'
    RATINGS_URL = SITE_URL + '/ratings/'
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

    def test_recommendations_get(self):
        self.reset_data()
        book_num = 3
        r = requests.get(self.RECOMMENDATIONS_URL + str(book_num))
        self.assertTrue(self.is_json(r.content.decode()))
        resp = json.loads(r.content.decode())
        self.assertEqual(resp['book_id'], [24812, 8, 17332218])

    def test_recommendations_post(self):
        self.reset_data()
        book_id = 2800905
        rating = 4

        b = {}
        b['id'] = book_id
        b['rating'] = rating
        r = requests.post(self.RECOMMENDATIONS_URL, data = json.dumps(b))
        self.assertTrue(self.is_json(r.content.decode()))
        resp = json.loads(r.content.decode())
        self.assertEqual(resp['result'], 'success')

        r = requests.get(self.RATINGS_URL + str(book_id))
        self.assertTrue(self.is_json(r.content.decode()))
        resp = json.loads(r.content.decode())
        self.assertEqual(resp['rating'], 4.029481192402417)

if __name__ == "__main__":
    unittest.main()

