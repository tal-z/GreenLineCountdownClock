import requests
import json
import pprint

sess = requests.session()
response = sess.get('https://api-v3.mbta.com/live_facilities/park-NB-0076')

print(response)

results = response.json()



print(json.dumps(results, indent='\t'))
