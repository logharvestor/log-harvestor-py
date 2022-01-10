import unittest

from logger import API_URL, Logger

valid_token = "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCIsImtpZCI6ImZvcndhcmRlciJ9.eyJfaWQiOiI2MTI4OTIwYjNjMzQyNTAwMjFkZGQyMTciLCJpYXQiOjE2MzAwNDg3ODN9.sb8lfpp01CC-y0T9Z5XiIEdy-JBeDHSBD8Gd05bZYaQ"
valid_token_local = "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCIsImtpZCI6ImZvcndhcmRlciJ9.eyJfaWQiOiI2MDk5Mzg5Mjg4MWQ0MzAwMjkxNzY2MGUiLCJpYXQiOjE2Mjc3MzAzOTZ9.uEY-6s8hK8HX6qy-5Su8Esb-iRXewc9hXYhRLIlALCo"
invalid_token = "123ABC"
valid_api_url = API_URL
valid_api_url_local = "http://localhost:3001/api/log"
invalid_api_url = "tcp://localhost:3001"


class TestInit(unittest.TestCase):
  def test_valid(self):
    lh = Logger(token=valid_token, api_url=valid_api_url)
    res = lh.log('test', msg={"a": 123})
    self.assertEqual(res, True)

if __name__ == '__main__':
    unittest.main()