import requests
import json
import pprint

sess = requests.session()
response = sess.get('https://api-v3.mbta.com/predictions/?filter[stop]=place-chill&filter[route]=Green-B&filter[direction_id]=1')

print(response)

results = response.json()
print(results['data'])


#print(json.dumps(results, indent='\t'))
