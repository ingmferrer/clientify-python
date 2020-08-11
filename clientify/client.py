import json

import requests

from .contacts import Contacts
from .deals import Deals
from .orders import Orders


class ClientifyClient(object):
    BASE_URL = "https://api.clientify.net/v1"

    def __init__(self, token=None):
        self.token = token

        self.contacts = Contacts(self)
        self.orders = Orders(self)
        self.deals = Deals(self)

    def authenticate(self, username, password):
        payload = {
            'username': username,
            'password': password,
        }
        url = '/api-auth/obtain_token/'
        response = self._post(self.BASE_URL + url, json=payload)
        self.token = response['token']
        return True

    def _get(self, url, *args, **kwargs):
        return self._request('GET', url, *args, **kwargs)

    def _post(self, url, *args, **kwargs):
        return self._request('POST', url, *args, **kwargs)

    def _put(self, url, *args, **kwargs):
        return self._request('PUT', url, *args, **kwargs)

    def _delete(self, url, *args, **kwargs):
        return self._request('DELETE', url, *args, **kwargs)

    def _request(self, method, url, *args, **kwargs):
        headers = {}
        if self.token:
            headers['Authorization'] = 'Token {}'.format(self.token)

        response = requests.request(method, url, headers=headers, **kwargs)

        if response.ok:
            try:
                return response.json()
            except json.decoder.JSONDecodeError:
                return None

        return response.content
