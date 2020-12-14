class Deals(object):
    def __init__(self, client):
        self.client = client

    def list_deal_pipelines(self):
        endpoint = '/deals/pipelines/'
        return self.client._get(self.client.BASE_URL + endpoint)

    def get_deal_pipeline_details(self, pipeline_id):
        endpoint = '/deals/pipelines/{}/'.format(pipeline_id)
        return self.client._get(self.client.BASE_URL + endpoint)

    def list_deal_pipeline_stages(self):
        endpoint = '/deals/pipelines/stages/'
        return self.client._get(self.client.BASE_URL + endpoint)

    def get_deal_pipeline_stage_details(self, stage_id):
        endpoint = '/deals/pipelines/stages/{}/'.format(stage_id)
        return self.client._get(self.client.BASE_URL + endpoint)

    def list_deals(self):
        endpoint = '/deals/'
        return self.client._get(self.client.BASE_URL + endpoint)

    def get_deal_details(self, deal_id):
        endpoint = '/deals/{}/'.format(deal_id)
        return self.client._get(self.client.BASE_URL + endpoint)

    def query_deals(self, params: dict):
        endpoint = '/deals/'
        return self.client._get(self.client.BASE_URL + endpoint, params=params)

    def create_deal(self, data: dict):
        endpoint = '/deals/'
        return self.client._post(self.client.BASE_URL + endpoint, json=data)

    def update_deal_details(self, deal_id, data: dict):
        endpoint = '/deals/{}/'.format(deal_id)
        return self.client._put(self.client.BASE_URL + endpoint, json=data)

    def delete_deal(self, deal_id):
        endpoint = '/deals/{}/'.format(deal_id)
        return self.client._delete(self.client.BASE_URL + endpoint)

    def close_deal(self, deal_id, data: dict):
        endpoint = '/deals/{}/close/'.format(deal_id)
        return self.client._post(self.client.BASE_URL + endpoint, json=data)
