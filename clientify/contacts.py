class Contacts(object):
    def __init__(self, client):
        self.client = client

    def list_contacts(self):
        endpoint = '/contacts/'
        return self.client._get(self.client.BASE_URL + endpoint)

    def query_contacts(self, params: dict):
        endpoint = '/contacts/'
        return self.client._get(self.client.BASE_URL + endpoint, params=params)

    def create_contact(self, data: dict):
        endpoint = '/contacts/'
        return self.client._post(self.client.BASE_URL + endpoint, json=data)

    def contact_details(self, contact_id):
        endpoint = '/contacts/{}/'.format(contact_id)
        return self.client._get(self.client.BASE_URL + endpoint)

    def edit_contact_details(self, contact_id, data: dict):
        endpoint = '/contacts/{}/'.format(contact_id)
        return self.client._put(self.client.BASE_URL + endpoint, json=data)

    def delete_contact(self, contact_id):
        endpoint = '/contacts/{}/'.format(contact_id)
        return self.client._delete(self.client.BASE_URL + endpoint)
