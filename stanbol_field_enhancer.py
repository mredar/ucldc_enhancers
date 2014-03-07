import os
import urllib2
import json
#import requests ##Can't use requests due to the socket 'too many files open'
#bug
import solr
from solr import SolrException

URL_SOLR = os.environ.get('URL_SOLR', 'http://107.21.228.130:8080/solr/dc-collection/')
#this is the list of acceptable input to solr index, needed because the 
#doc returned by solrpy has additional fields that err out on update.
INPUT_DOC_KEYS = ('id', 'collection_name', 'campus', 'repository',
                  'identifier', 'title', 'contributor', 'coverage',
                  'creator', 'date', 'description', 'format', 'identifier',
                  'language', 'publisher', 'relation', 'rights', 'source',
                  'subject', 'type', 
                  )
EXCLUDE_DOC_KEYS = ('score',)

URL_STANBOL_ENHANCER = 'http://54.197.229.87:8080/enhancer/chain/dbpedia-proper-noun'

HEADERS_STANBOL = { 'accept':'application/json',
'content-type':'text/plain' }

FIELD_TO_ENHANCE = 'creator'
FIELD_TO_ENHANCE = 'description'
#FIELD_TO_ENHANCE = 'title'
#FIELD_TO_ENHANCE = 'subject'


exception_resp = []
def get_stanbol_graph_json(data):
    request = urllib2.Request(URL_STANBOL_ENHANCER, data=data.encode('utf-8'), headers=HEADERS_STANBOL)
    try:
        f = urllib2.urlopen(request)
    except urllib2.HTTPError, e:
        if e.code != 500:
            print str(e), e.code, 'DATA:', data
            raise e
        else:
            return None
    try:
        json_dict = json.load(f)
    except ValueError, e:
        exception_resp.append((e, resp, data))
        return None
    return json_dict['@graph'] if json_dict.has_key('@graph') else None

def get_entity_refs_from_graph(graph, confidence_threshold=.7):
    entity_ref_conf={}
    entity_refs = []
    for i in graph:
        if 'enhancer:entity-reference' in i.keys():
            entity_ref_conf[i['enhancer:entity-reference']]=i['enhancer:confidence']
    for i in graph:
        if i['@id'] in entity_ref_conf:
            if entity_ref_conf[i['@id']] > .5:
                entity_refs.append(i['@id'])
#                for j in i['rdfs:label']:
#                    if j['@language'] == 'en':
#                        label = j['@value']
#                print "GOOD REF", i['@id'], label
    return entity_refs
    
solr_db = solr.Solr(URL_SOLR)
query = '*:*'
#query = 'collection_name:"Calisphere - Santa Clara University: Digital Objects"'
#query = 'collection_name:"Calisphere - The Ruth and Sherman Lee Institute of Japanese Art"'
#fq='url_thumbnail:[* TO *]'
#resp = solr_db.select(query, fq=fq)#, sort='id asc')
entities_recognized = []
resp = solr_db.select(query)
NUMBER_OF_DOCS = 0
n_enhance_attempts = 0
try:
    while (resp):
        for doc in resp.results:
            NUMBER_OF_DOCS += 1
            if doc.has_key(FIELD_TO_ENHANCE):
                for fvalue in doc[FIELD_TO_ENHANCE]:
                    n_enhance_attempts += 1
                    if n_enhance_attempts % 100 == 0:
                        print FIELD_TO_ENHANCE, fvalue.encode('utf-8')
                    graph = get_stanbol_graph_json(fvalue)
                    if graph:
                        entity_refs = get_entity_refs_from_graph(graph)
                        entities_recognized.extend(entity_refs)
                        for entity in entity_refs:
                            doc_up = {'id':doc['id'], 'entity_ss':{'set':entity}}
                            try:
                                solr_db.add(doc_up)
                            except SolrException, e:
                                print "SOLR EXCEPTION", dir(e)
                                if not e.httpcode == 400:
                                    raise e
        resp = resp.next_batch() ##NOTE: doesn't work with updating doc set
    
    solr_db.commit()
except Exception, e:
    print "EXCEPTION", str(e), type(e), dir(e)

#print "ENTITIES", entities_recognized
print "NUMBER OF DOCS", str(NUMBER_OF_DOCS)
print "NUMBER OF RECOGNIZED ENTITIES", str(len(entities_recognized))
print "RESPONSE EXCEPTIONS:", str(len(exception_resp)) #, '  ----  ', str(exception_resp)


#g0.keys()
# OUT: [u'foaf:depiction', u'rdfs:comment', u'@id', u'@type', u'rdfs:label']
#g1=graph[1]
#g1.keys()
# OUT: [u'enhancer:extracted-from', u'enhancer:confidence', u'dc:language', u'dc:creator', u'dc:type', u'dc:created', u'@id', u'@type']
##g2=graph[2]
##g2.keys()
### OUT: [u'enhancer:extracted-from', u'enhancer:confidence', u'dc:creator', u'dc:type', u'enhancer:start', u'enhancer:end', u'enhancer:selected-text', u'dc:created', u'enhancer:selection-context', u'@id', u'@type']
##g3=graph[3]
##g3.keys()
### OUT: [u'enhancer:extracted-from', u'enhancer:confidence', u'dc:language', u'dc:creator', u'dc:type', u'dc:created', u'@id', u'@type']
##g4=graph[4]
##g4.keys()
### OUT: [u'enhancer:extracted-from', u'enhancer:confidence', u'dc:creator', u'enhancer:entity-label', u'entityhub:site', u'dc:relation', u'dc:created', u'enhancer:entity-type', u'@id', u'@type', u'enhancer:entity-reference']
##g4['enhancer:entity-reference']
### OUT: u'http://dbpedia.org/resource/Michael_Jordan'
##g0['@type']
### OUT: [u'dbp-ont:Agent', u'dbp-ont:Athlete', u'dbp-ont:BasketballPlayer', u'dbp-ont:Person', u'foaf:Person', u'owl:Thing', u'schema:Person']
