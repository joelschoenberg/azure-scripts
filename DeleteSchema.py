# This script retrieves the Schema of a custom Analytics Event

import requests

url = 'http://34.210.157.84:9080/events/schema/azureFunctions'
headers = {'X-Events-API-AccountName': 'customer1_b7686ddf-6680-43f3-bbeb-303c027344e2', 'X-Events-API-Key': '50c4c457-d91a-44b6-a6e1-437d1f35e50a', 'Accept': 'application/vnd.appd.events+json;v=1'}
appd = requests.delete(url, headers=headers)
print "Accessing AppDynamics..."
print "Return code:"
print appd.status_code
