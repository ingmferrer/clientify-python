class Users(object):
    def __init__(self, client):
        self.client = client

    def list_users(self):
        endpoint = '/users/'
        return self.client._get(self.client.BASE_URL + endpoint)

    def query_users(self, params: dict):
        endpoint = '/users/'
        return self.client._get(self.client.BASE_URL + endpoint, params=params)
