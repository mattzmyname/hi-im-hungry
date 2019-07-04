import base64
import time
from pprint import pprint
from yelpapi import YelpAPI
from .credentials import yelp

MY_API_KEY = base64.b64decode(yelp['API_Key']).decode('utf-8')
client = YelpAPI(MY_API_KEY, timeout_s= 2.0)


def get_search_parameters(lat, long):
	# See the Yelp API for more details
	params = {}
	params["term"] = "restaurant"
	params['latitude'] = str(lat)
	params['longitude'] = str(long)
	params["radius_filter"] = "2000"
	params["limit"] = "10",
	params['sort_by'] = 'rating'
	
	return params


def get_results(params):
	response = client.search_query(**params)
	
	return response


def main():
	locations = [(39.98, -82.98), (42.24, -83.61), (41.33, -89.13)]
	api_calls = []
	for lat, long in locations:
		params = get_search_parameters(lat, long)
		api_calls.append(get_results(params))
		# Be a good internet citizen and rate-limit yourself
		time.sleep(1.0)
	return api_calls[0]
	
	

	