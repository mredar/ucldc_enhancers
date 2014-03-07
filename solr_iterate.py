import os
import solr
from solr import SolrException

URL_SOLR = os.environ.get('URL_SOLR', 'http://107.21.228.130:8080/solr/dc-collection/')

solr_db = solr.Solr(URL_SOLR)
query = '*:*'
#query = 'collection_name:"Calisphere - Santa Clara University: Digital Objects"'
#query = 'collection_name:"Calisphere - The Ruth and Sherman Lee Institute of Japanese Art"'
#fq='url_thumbnail:[* TO *]'
#resp = solr_db.select(query, fq=fq)#, sort='id asc')
FIELD_TO_ENHANCE = 'creator'
FIELD_TO_ENHANCE = 'description'
#FIELD_TO_ENHANCE = 'title'
#FIELD_TO_ENHANCE = 'subject'

NUMBER_OF_DOCS = 0
def main():
    entities_recognized = []
    resp = solr_db.select(query)
    NUMBER_OF_DOCS = 0
    n_enhance_attempts = 0
    try:
        while (resp):
            for doc in resp.results:
                NUMBER_OF_DOCS += 1
                print doc
####                if doc.has_key(FIELD_TO_ENHANCE):
####                    for fvalue in doc[FIELD_TO_ENHANCE]:
####                        n_enhance_attempts += 1
####                        if n_enhance_attempts % 100 == 0:
####                            print FIELD_TO_ENHANCE, fvalue.encode('utf-8')
####                        #TODO: run each enhancer, get entity data then set the 
####                        # the entity_ss using update syntax
####                        for enhancer in enhancers:
####                            entities = enhancer.enhance(value)
####                        graph = get_stanbol_graph_json(fvalue)
####                        if graph:
####                            entity_refs = get_entity_refs_from_graph(graph)
####                            entities_recognized.extend(entity_refs)
####                            for entity in entity_refs:
####                                doc_up = {'id':doc['id'], 'entity_ss':{'set':entity}}
####                                try:
####                                    solr_db.add(doc_up)
####                                except SolrException, e:
####                                    print "SOLR EXCEPTION", dir(e)
####                                    if not e.httpcode == 400:
####                                        raise e
            resp = resp.next_batch() ##NOTE: doesn't work with updating doc set
        
        #solr_db.commit()
    except Exception, e:
        print "EXCEPTION", str(e), type(e), dir(e)
        print "NUMVBER", str(NUMBER_OF_DOCS)
    
    #print "ENTITIES", entities_recognized
    print "NUMBER OF DOCS", str(NUMBER_OF_DOCS)
    print "NUMBER OF RECOGNIZED ENTITIES", str(len(entities_recognized))
    print "RESPONSE EXCEPTIONS:", str(len(exception_resp)) #, '  ----  ', str(exception_resp)
    
if __name__=="__main__":
    main()
