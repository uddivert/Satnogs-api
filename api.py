import requests
import json
#def satApi():
"""
This is the format and order:
payload = {'key1': 'value1', 'key2': 'value2'}
r = requests.get('https://httpbin.org/get', params=payload)
https://httpbin.org/get?key2=value2&key1=value1
"""
#https://db-dev.satnogs.org/api/satellites/?format=json&in_orbit=true&norad_cat_id=25544
payload = {'format': 'json', 'in_orbit': 'true', 'norad_cat_id':'25544'}
r = requests.get('https://db-dev.satnogs.org/api/satellites/', params=payload)
print(r.url)
print(r.json())
#json.loads(r.json())
out_file = open("test.json", "w") 
json.dump(r.json(), out_file, indent = 6) 
out_file.close() 