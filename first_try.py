# OUT: Python shell history and tab completion are enabled.
import requests
headers = { 'Accept': 'application/json',
           'Content-type': 'text/plain' }
data = "Albert Einstein"
url_stanbol = 'http://54.197.229.87:8080/enhancer/chain/dbpedia-proper-noun?omitMetadata=true'
resp = requests.post(url_stanbol, headers=headers, data=data)
resp
# OUT: <Response [415]>
dir(resp)
# OUT: ['__attrs__', '__bool__', '__class__', '__delattr__', '__dict__', '__doc__', '__format__', '__getattribute__', '__getstate__', '__hash__', '__init__', '__iter__', '__module__', '__new__', '__nonzero__', '__reduce__', '__reduce_ex__', '__repr__', '__setattr__', '__setstate__', '__sizeof__', '__str__', '__subclasshook__', '__weakref__', '_content', '_content_consumed', 'apparent_encoding', 'close', 'connection', 'content', 'cookies', 'elapsed', 'encoding', 'headers', 'history', 'iter_content', 'iter_lines', 'json', 'links', 'ok', 'raise_for_status', 'raw', 'reason', 'request', 'status_code', 'text', 'url']
resp.status_code
# OUT: 415
headers = { 'accept': 'application/json',
'content-type':'text/plain'}
resp = requests.post(url_stanbol, headers=headers, data=data)
resp
# OUT: <Response [415]>
resp = requests.post(url_stanbol, headers=headers, data=data)
