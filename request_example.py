import requests

auth_details = ('remco.ruijsenaars@hu.nl', 'MGOeJ1oY8vcGyVPPLvOiK6MrpVf3OncLFZksAl6Kx2Q2GlSXvcrImA')
api_url = 'http://webservices.ns.nl/ns-api-avt?station=ut'
response = requests.get(api_url, auth=auth_details)
print(response.text)