import requests
import datetime
import pandas as pd


params = {
  'access_key': '0ad4d902bc5b53d11ccdde7b5e98b26d',
  "dep_iata" : "EWR",
  "airline_iata": "UA"
  }

api_result = requests.get('https://api.aviationstack.com/v1/flights', params)
api_response = api_result.json()
df = pd.json_normalize(api_response["data"])

