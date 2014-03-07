import pprint
import spotlight
from requests.exceptions import HTTPError as HTTPErrorRequests
####annotations=spotlight.annotate('http://spotlight.dbpedia.org/rest/annotate', 'Hugh Hefner')
####pprint.pprint(annotations)
####print '\n\n'
####annotations=spotlight.annotate('http://spotlight.dbpedia.org/rest/annotate', 'Albert Einstein')
####pprint.pprint(annotations)
####print '\n\n'
####annotations=spotlight.annotate('http://spotlight.dbpedia.org/rest/annotate', 'California')
####pprint.pprint(annotations)
from urllib2 import HTTPError
import os
import solr
from solr import SolrException

URL_SOLR = os.environ.get('URL_SOLR', 'http://107.21.228.130:8080/solr/dc-collection/')

solr_db = solr.Solr(URL_SOLR)
query = '-entity_ss:[* TO *]'
#query = 'collection_name:"Calisphere - Santa Clara University: Digital Objects"'
#query = 'collection_name:"Calisphere - The Ruth and Sherman Lee Institute of Japanese Art"'
fq='-entity_ss:[* TO *]'
#resp = solr_db.select(query, fq=fq)#, sort='id asc')
FIELD_TO_ENHANCE = 'creator'
FIELD_TO_ENHANCE = 'description'
#FIELD_TO_ENHANCE = 'title'
#FIELD_TO_ENHANCE = 'subject'

def get_entity_refs_from_annotations(annotations):
    '''Annotations are list of dicts. Use the "similarityScore" & URI for info
    '''
    uri_entities = []
    for ann in annotations:
        if ann['similarityScore'] >= .1:
            print "FOUND ENTITY", ann['URI']
            uri_entities.append(ann['URI'])
    return uri_entities

DOCS_RETRIEVED = DOCS_PREVIOUSLY_ENHANCED = 0
exception_resp = []
def main():
    entities_recognized = []
    resp = solr_db.select(query)
    DOCS_RETRIEVED = DOCS_PREVIOUSLY_ENHANCED = 0
    n_enhance_attempts = 0
    try:
        while (resp):
            for doc in resp.results:
                DOCS_RETRIEVED += 1
                if doc.has_key('entity_ss'):
                    DOCS_PREVIOUSLY_ENHANCED +=1
                    continue
                if doc.has_key(FIELD_TO_ENHANCE):
                    for fvalue in doc[FIELD_TO_ENHANCE]:
                        n_enhance_attempts += 1
                        if n_enhance_attempts % 100 == 0:
                            print "NDOCS:", str(DOCS_RETRIEVED), ' -> ', FIELD_TO_ENHANCE, fvalue.encode('utf-8')
                        #TODO: run each enhancer, get entity data then set the 
                        # the entity_ss using update syntax
                        try:
                            annotations = spotlight.annotate('http://spotlight.dbpedia.org/rest/annotate', fvalue)
                        except spotlight.SpotlightException, e:
                            exception_resp.append(e)
                            if not "No Resources found" in e.message:
                                print "NUM:", str(DOCS_RETRIEVED), " EEEE->", str(e)
                                print e.args, e.message
                                raise e
                        except HTTPError, e:
                            #TODO: logger
                            continue
                        except HTTPErrorRequests, e:
                            #TODO: logger
                            continue
                        if annotations:
                            entity_refs = get_entity_refs_from_annotations(annotations)
                            entities_recognized.extend(entity_refs)
                            for entity in entity_refs:
                                doc_up = {'id':doc['id'], 'entity_ss':{'add':entity.replace('http://dbpedia.org/resource/', 'http://wikipedia.org/wiki/')}}
                                try:
                                    print 'TRY UPDATE', str(doc_up)
                                    solr_db.add(doc_up)
                                except SolrException, e:
                                    if not e.httpcode == 400:
                                        raise e
            resp = solr_db.select(query, start=DOCS_RETRIEVED)
            #resp = resp.next_batch()
        solr_db.commit()
    except Exception, e:
        import traceback
        print "EXCEPTION TYPE:", type(e)
        print traceback.format_exc()
    
    #print "ENTITIES", entities_recognized
    print "NUMBER OF DOCS", str(DOCS_RETRIEVED)
    print "NUMBER OF DOCS ENHANCED", str(DOCS_RETRIEVED-DOCS_PREVIOUSLY_ENHANCED)
    print "NUMBER OF RECOGNIZED ENTITIES", str(len(entities_recognized))
    print "RESPONSE EXCEPTIONS:", str(len(exception_resp)) #, '  ----  ', str(exception_resp)
    
if __name__=="__main__":
    main()
