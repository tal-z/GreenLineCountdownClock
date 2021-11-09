import requests
import json
import pprint

sess = requests.session()
response = sess.get('https://api-v3.mbta.com/stops?fields[stop]=name,description')

print(response)

results = response.json()
pprint.pprint(results['data'])


#print(json.dumps(results, indent='\t'))
