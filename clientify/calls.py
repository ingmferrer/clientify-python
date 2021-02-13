class Calls(object):
    def __init__(self, client):
        self.client = client

    def list_calls(self):
        endpoint = '/calls/'
        return self.client._get(self.client.BASE_URL + endpoint)

    def query_calls(self, params: dict):
        endpoint = '/calls/'
        return self.client._get(self.client.BASE_URL + endpoint, params=params)
