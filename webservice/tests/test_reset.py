import unittest
import requests
import json

class TestReset(unittest.TestCase):

    PORT_NUM = '51082' #change port number to match your port number
    print("Testing Port number: ", PORT_NUM)
    SITE_URL = 'http://student04.cse.nd.edu:' + PORT_NUM
    RESET_URL = SITE_URL + '/reset/'

    def test_reset_data(self):
        m = {}
        r = requests.put(self.RESET_URL)

if __name__ == "__main__":
    unittest.main()

