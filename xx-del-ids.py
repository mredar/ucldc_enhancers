# OUT: Python shell history and tab completion are enabled.
import urllib
import urllib2
urllib.urlopen('http://107.21.228.130:8080/solr/dc-collection/update?stream.body=%3Cdelete%3E%3Cquery%3Eentity_ss:[*%20TO%20*]%3C/query%3E%3C/delete%3E')
# OUT: <addinfourl at 50247512 whose fp = <socket._fileobject object at 0x2f7fad0>>
urllib.urlopen('http://107.21.228.130:8080/solr/dc-collection/update?stream.body=<delete><query>entity_ss:[* TO *]</query></delete>')
# OUT: Traceback (most recent call last):
# OUT:   File "<input>", line 1, in <module>
# OUT: NameError: name 'urllilb' is not defined
urllib.urlopen('http://107.21.228.130:8080/solr/dc-collection/update?stream.body=<delete><query>entity_ss:[* TO *]</query></delete>')
# OUT: <addinfourl at 50279344 whose fp = <socket._fileobject object at 0x2f82f50>>
url_base='http://107.21.228.130:8080/solr/dc-collection/update?stream.body=<delete><query>id:'
f=open('ids-to-delete')
for l in f.readlines():
    l = l.strip()
    url_delete = url_base+l+'</query></delete>'
    print "DLETE:", url_delete
    urllib.urlopen(url_delete)
