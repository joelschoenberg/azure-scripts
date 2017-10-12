#
# Script to extract data from an Azure Serverless Function
# and add it to an AppDynamics Controller as a custom
# Analytics Event. Uses the API documented here:
# https://docs.appdynamics.com/display/PRO42/Analytics+Events+API
#
# This script is broken into three parts:
# 1. Extract the schema from Azure Serverless Functions
#    - assumes you have configured Application Insights for your function
# 2. Use the returned JSON object to create the AppDynamics Schema
# 3. Extract the data from Azure Serverless Functions
# 4. Insert the payload from that extraction into AppDynamics
#    - assumes you have a controller with an Event cluster (see docs)
import requests
import json
# ---------------------------------------------------------------------------
# PART 1: EXTRACT THE SCHEMA FROM AZURE SERVERLESS FUNCTIONS
# My application ID: 06e7e052-76e6-467a-9e1d-44bdfcdb71ad
# My API Key: 2ld7ms8jngjh76qpim0n7uiri0dxfl6feeghqcsq
#
# This query gets the schema my Azure Serverless Function
#
applicationid = '06e7e052-76e6-467a-9e1d-44bdfcdb71ad'
url = 'https://api.applicationinsights.io/beta/apps/06e7e052-76e6-467a-9e1d-44bdfcdb71ad/query/schema'
headers = {'x-api-key': '2ld7ms8jngjh76qpim0n7uiri0dxfl6feeghqcsq', 'Prefer': 'response-v1=true'}
# Execute and print the GET with header in URL
azschema = requests.get(url, headers=headers)
print "Accessing Azure..."
print "The Azure schema payload in JSON format:"
print azschema.content
print "Return code:"
print azschema.status_code
print

# ---------------------------------------------------------------------------
# PART 2: CREATE THE APPDYNAMICS SCHEMA
#
# TODO: figure out how to insert the JSON as an object
#
url = 'http://34.210.157.84:9080/events/schema/azureFunctions'
headers = {'X-Events-API-AccountName': 'customer1_b7686ddf-6680-43f3-bbeb-303c027344e2', 'X-Events-API-Key': '50c4c457-d91a-44b6-a6e1-437d1f35e50a', 'Content-type': 'application/vnd.appd.events+json;v=1'}
data = '{"schema": { "id": "string", "metricName": "string", "mycount": "integer" }}'
appdschema = requests.post(url, headers=headers, data=data)
print "Accessing AppDynamics..."
print "Creating schema..."
print "Return code:"
print appdschema.status_code
print

# ---------------------------------------------------------------------------
# PART 3: EXTRACT THE TRACES FROM AZURE SERVERLESS FUNCTIONS
#
# THIS QUERY EXTRACTS THE TRACES FOR THE LAST 1 HOUR
#
applicationid = '06e7e052-76e6-467a-9e1d-44bdfcdb71ad'
url = 'https://api.applicationinsights.io/beta/apps/06e7e052-76e6-467a-9e1d-44bdfcdb71ad/events/traces'
headers = {'x-api-key': '2ld7ms8jngjh76qpim0n7uiri0dxfl6feeghqcsq', 'Prefer': 'response-v1=true'}
payload = {'timespan': 'PT1H'}
aztraces = requests.get(url, payload=payload, headers=headers)
print "Accessing Azure..."
print "The Azure traces payload in JSON format:"
print aztraces.content
print "Return code:"
print aztraces.status_code
print


# ---------------------------------------------------------------------------
# PART 4: INSERT THE JSON PAYLOAD INTO APPDYNAMICS
#
# TODO: insert the trace data as a json object

url = 'http://34.210.157.84:9080/events/schema/azureFunctions'
headers = {'X-Events-API-AccountName': 'customer1_b7686ddf-6680-43f3-bbeb-303c027344e2', 'X-Events-API-Key': '50c4c457-d91a-44b6-a6e1-437d1f35e50a', 'Content-type': 'application/vnd.appd.events+json;v=1'}
data = {"id": "06e7e052-76e6-467a-9e1d-44bdfcdb71ad", "metricName": "requests", "mycount": "131"}
appdtraces = requests.post(url, headers=headers, data=data)
print "Accessing AppDynamics..."
print "Adding data..."
print appddata.content
print "Return code:"
print appddata.status_code
print
