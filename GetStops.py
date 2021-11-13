import requests
import pprint
import os


sess = requests.session()
API_KEY = os.getenv('MBTA_API_KEY')


routes_response = sess.get(f'https://api-v3.mbta.com/routes?filter[type]=0,1', headers={"x-api-key": API_KEY})
routes = routes_response.json()
route_ids = [route["id"] for route in routes['data']]
print(route_ids)

stops_response = sess.get(f'https://api-v3.mbta.com/stops?filter[route]={",".join(route_ids)}')
stops = stops_response.json()
pprint.pprint(stops)
