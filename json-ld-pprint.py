# OUT: Python shell history and tab completion are enabled.
import requests
headers = { 'accept':'application/json',
'content-type':'text/plain' }
url_stanbol_enhancer = 'http://54.197.229.87:8080/enhancer/chain/dbpedia-proper-noun'
data='Michael Jordan'
resp = requests.post(url_stanbol_enhancer, data=data, headers=headers)
import pprint
f=open('jordan-stanbol-rdf.json', 'w')
pprint.pprint(resp.json(), f)
