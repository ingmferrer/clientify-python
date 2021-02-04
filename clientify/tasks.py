class Tasks(object):
    def __init__(self, client):
        self.client = client

    def list_tasks(self):
        endpoint = '/tasks/'
        return self.client._get(self.client.BASE_URL + endpoint)

    def query_tasks(self, params: dict):
        endpoint = '/tasks/'
        return self.client._get(self.client.BASE_URL + endpoint, params=params)
