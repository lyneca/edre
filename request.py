import requests
import json

token = ''
base_url = ''

class NetworkException(Exception):
    def __str__(self):
        return "Error {}: {}".format(self.args[0], self.args[1])

class Requester:
    """
    Class used to perform authenticated requests to Ed.
    """
    def __init__(self):
        self.access_token = token
        self.user_agent = 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/57.0.2987.133 Safari/537.36'
        self.base_url = base_url

    def update_token(self):
        """Updates the access token to the global variable."""
        self.access_token = token

    def _error(self, request):
        raise NetworkException(request.status_code, request.reason)

    def _generate_headers(self):
        return {
            'content-type': 'application/json;charset=UTF-8',
            'user-agent': self.user_agent,
            'X-Token': self.access_token
        }

    def post(self, endpoint, data={}):
        """
        Sends an authenticated HTTP POST request to Ed.

        :param endpoint: The API endpoint. Will be concatenated to https://edstem.com.au/api[/endpoint]; i.e., include the / at the start.
        :param data: The POST data to send.
        """
        headers = self._generate_headers()
        r = requests.post(self.base_url + endpoint, data=data, headers=headers)
        if r.status_code >= 400:
            return self._error(r)
        if r.content:
            return r.json()
        else: return 0

    def get(self, endpoint, params={}):
        """
        Sends an authenticated HTTP GET request to Ed.

        :param endpoint: The API endpoint. Will be concatenated to https://edstem.com.au/api[/endpoint]; i.e., include the / at the start.
        :param data: The GET URL parameters to send.
        """
        headers = self._generate_headers()
        r = requests.get(self.base_url + endpoint, params=params, headers=headers)
        if r.status_code >= 400:
            return self._error(r)
        if r.content:
            return r.json()
        else: return 0
