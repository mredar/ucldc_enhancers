# OUT: Python shell history and tab completion are enabled.
import solr
sdb = solr.Solr('http://107.21.228.130:8080/solr/dc-collection/')
r = sdb.select('*:*')
sdoc=r.results[0]
sdoc
ID=sdoc['id']
print sdoc
#sdb.add(id=ID, entity_ss={'set':"Bob Marley"})
sdb.add({'id':ID, 'entity_ss':{'set':"Bob Marley"}})
sdb.commit()
