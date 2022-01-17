from uuid import uuid4
import requests

from logharvestor import API_URL


class Forwarder:
    """
    Primary collector and coordinator with LogHarvestor (LH) Platform

    :param token: JWT generated for the forwarder
    :type token: string 

    :param api_url: The destination for logs (you should not need to update this)
    :type api_url: string

    :param verbose: Show transactional information
    :type verbose: bool 

    """

    def __init__(self, token, api_url=API_URL, verbose=False):
        self.id = uuid4()
        self.token = token
        self.api_url = api_url
        self.verbose = verbose
        self.total_logs_sent = 0
        self.headers = ({'authorization': f'Bearer {self.token}',
                         'content-type': 'application/json'})

    def test_conn(self):
        """
        Test connection with LH Platform

        :returns: Boolean indicating if the connection was successful and the response from the server

        >>> token = 'your_token_here'
        >>> lh = Forwarder(token=token)

        >>> success, res = lh.test_conn()
        """

        check_api_url = self.api_url+'/check'
        self.verboseLog(f'\nTestConn: {check_api_url}')

        res = requests.post(url=check_api_url, headers=self.headers)

        if res.status_code == 200:
            self.verboseLog(f'TestConn: Success; ServerResponse: {res}')
            return (True, res)
        else:
            self.verboseLog(f'TestConn: Failed; ServerResponse: {res}')
            return (False, res)

    def log(self, type, msg):
        """
        Sends a Log object to LH Platform

        :param type: How the log is classified
        :type type: str


        :param msg: The content of the log
        :type msg: any 

        :returns: Boolean indicating if the request was successful and the response from the server

        >>> token = 'your_token_here'
        >>> lh = Forwarder(token=token)

        >>> success, res = lh.log('info', {"hello": "world"})
        """
        data = {"type": type, "msg": msg}
        self.verboseLog(f'\nLog: [{data}]')

        res = requests.post(url=self.api_url, headers=self.headers, json=data)

        if res.status_code == 200:
            self.total_logs_sent += 1
            self.verboseLog(
                f'Log: Success; TotalLogsSent: {self.total_logs_sent}')
            return (True, res)
        else:
            self.verboseLog(f'Log: Failed; ServerResponse: {res}')
            return (False, res)

    def verboseLog(self, msg):
        """Utility method"""
        if self.verbose:
            print(msg)
