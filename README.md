# Clientify

A python wrapper for clientify

## Requirements
- Requests

## Installation
`pip install git+https://github.com/ingmferrer/clientify-python.git`

## Usage
### Authentication

There are two ways to authenticate to Clientify
1. Get the API Token from dashboard
```python
from clientify.client import ClientifyClient
client = ClientifyClient(token='<API_TOKEN>')
```

2. Log-in with username and password
```python
from clientify.client import ClientifyClient
client = ClientifyClient()
response = client.authenticate(username='<EMAIL>', password='<PASSWORD>')
assert response == True
```

### Contacts
#### List contacts
```python
response = client.contacts.list_contacts()
```

#### Create a contact
```python
data = {
        'first_name': 'Jasper',
        'last_name': 'Barry',
        'email': 'tbefaqoja@mailinator.net',
        'phone': '+1 (618) 353-6458',
        'status': 'Voluptates facilis u',
        'title': 'Mrs.',
        'company': 'Henderson Gomez LLC',
        'contact_type': '',
        'contact_source': '',
        'addresses': [
            {
                'street': 'camino de la coquina, 23',
                'city': 'Lugo',
                'state': 'Galicia',
                'country': 'Spain',
                'postal_code': '34',
                'type': 1
            }
        ],
        'custom_fields': [],
        'description': 'Sunt vitae consequun',
        'remarks': 'Consequatur aliquid',
        'summary': 'Voluptas dolorem com',
        'message': 'Nobis aliquip quia c',
        're_property_name': 'Hakeem Hicks',
        'last_contact': None
    }
response = client.contacts.create_contact(data)
```

#### Contact Details
```python
response = client.contacts.contact_details('<CONTACT_ID>')
```

#### Edit Contact Details
```python
data = {
    'first_name': 'Paco',
    'last_name': 'Mario'
}
response = client.contacts.edit_contact_details('<CONTACT_ID>', data)
```

#### Delete Contact
```python
response = client.contacts.delete_contact('<CONTACT_ID>')
```

### Deals
#### List deal pipelines
```python
response = client.deals.list_deal_pipelines()
```

#### Get deal pipeline details
```python
response = client.deals.get_deal_pipeline_details('<PIPELINE_ID>')
```

#### List deal pipeline stages
```python
response = client.deals.list_deal_pipeline_stages()
```

#### Get deal pipeline stage details
```python
response = client.deals.get_deal_pipeline_stage_details('<STAGE_ID>')
```

#### List deals
```python
response = client.deals.list_deals()
```

#### Create deal
```python
data = {
    "name":"Nuevo deal con pipeline desc y pipeline stage, fecha y custom fields",
    "amount":"11.33",
    "contact":"https://api.clientify.net/v1/contacts/integer/",
    "company":"https://api.clientify.net/v1/companies/integer/",
    "pipeline_desc": "nuevo",
    "pipeline_stage_desc": "ultima",
    "expected_closed_date": "2019-11-30",
    "custom_fields": [{"field": "quaderno_id","value": "cdn_1133"}]
}
response = client.deals.create_deal(data)
```

#### Update deal details
```python
data = {
	"pipeline_stage": "https://api.clientify.net/v1/deals/pipelines/stages/integer/"
}
response = client.deals.update_deal_details(data)
```

#### Delete deal
```python
response = client.deals.delete_deal('<DEAL_ID>')
```
