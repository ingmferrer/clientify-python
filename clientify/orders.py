class Orders(object):
    def __init__(self, client):
        self.client = client

    def list_orders(self):
        endpoint = '/orders/'
        return self.client._get(self.client.BASE_URL + endpoint)

    def create_orders(self, data: dict):
        endpoint = '/orders/'
        return self.client._post(self.client.BASE_URL + endpoint, json=data)
