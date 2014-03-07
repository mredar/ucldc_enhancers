# OUT: Python shell history and tab completion are enabled.
import requests
headers = { 'accept':'application/json',
'content-type':'text/plain' }
url_stanbol_enhancer = 'http://54.197.229.87:8080/enhancer/chain/dbpedia-proper-noun'
data='Michael Jordan'
resp = requests.post(url_stanbol_enhancer, data=data, headers=headers)
resp
# OUT: <Response [200]>
dir(resp)
# OUT: ['__attrs__', '__bool__', '__class__', '__delattr__', '__dict__', '__doc__', '__format__', '__getattribute__', '__getstate__', '__hash__', '__init__', '__iter__', '__module__', '__new__', '__nonzero__', '__reduce__', '__reduce_ex__', '__repr__', '__setattr__', '__setstate__', '__sizeof__', '__str__', '__subclasshook__', '__weakref__', '_content', '_content_consumed', 'apparent_encoding', 'close', 'connection', 'content', 'cookies', 'elapsed', 'encoding', 'headers', 'history', 'iter_content', 'iter_lines', 'json', 'links', 'ok', 'raise_for_status', 'raw', 'reason', 'request', 'status_code', 'text', 'url']
resp.json
# OUT: <bound method Response.json of <Response [200]>>
resp.json()
# OUT: {u'@context': {u'enhancer': u'http://fise.iks-project.eu/ontology/', u'enhancer:confidence': {u'@type': u'xsd:double'}, u'dc:creator': {u'@type': u'xsd:string'}, u'dc:type': {u'@type': u'@id'}, u'dbp-ont': u'http://dbpedia.org/ontology/', u'enhancer:start': {u'@type': u'xsd:int'}, u'dc': u'http://purl.org/dc/terms/', u'entityhub': u'http://stanbol.apache.org/ontology/entityhub/entityhub#', u'dc:relation': {u'@type': u'@id'}, u'dc:created': {u'@type': u'xsd:dateTime'}, u'enhancer:entity-type': {u'@type': u'@id'}, u'foaf': u'http://xmlns.com/foaf/0.1/', u'xsd': u'http://www.w3.org/2001/XMLSchema#', u'enhancer:extracted-from': {u'@type': u'@id'}, u'foaf:depiction': {u'@type': u'@id'}, u'rdfs': u'http://www.w3.org/2000/01/rdf-schema#', u'owl': u'http://www.w3.org/2002/07/owl#', u'enhancer:end': {u'@type': u'xsd:int'}, u'enhancer:entity-reference': {u'@type': u'@id'}, u'schema': u'http://schema.org/'}, u'@graph': [{u'foaf:depiction': [u'http://upload.wikimedia.org/wikipedia/commons/b/b3/Jordan_Lipofsky.jpg', u'http://upload.wikimedia.org/wikipedia/commons/thumb/b/b3/Jordan_Lipofsky.jpg/200px-Jordan_Lipofsky.jpg'], u'rdfs:comment': {u'@value': u'Michael Jeffrey Jordan (born February 17, 1963) is a retired American professional basketball player, active entrepreneur, and majority owner of the Charlotte Bobcats. His biography on the National Basketball Association (NBA) website states, "By acclamation, Michael Jordan is the greatest basketball player of all time. " Jordan was one of the most effectively marketed athletes of his generation and was considered instrumental in popularizing the NBA around the world in the 1980s and 1990s.', u'@language': u'en'}, u'@id': u'http://dbpedia.org/resource/Michael_Jordan', u'@type': [u'dbp-ont:Agent', u'dbp-ont:Athlete', u'dbp-ont:BasketballPlayer', u'dbp-ont:Person', u'foaf:Person', u'owl:Thing', u'schema:Person'], u'rdfs:label': [{u'@value': u'Michael Jordan', u'@language': u'de'}, {u'@value': u'Michael Jordan', u'@language': u'en'}, {u'@value': u'Michael Jordan', u'@language': u'es'}, {u'@value': u'Michael Jordan', u'@language': u'fr'}, {u'@value': u'Michael Jordan', u'@language': u'it'}, {u'@value': u'Michael Jordan', u'@language': u'pt'}, {u'@value': u'Michael Jordan', u'@language': u'tr'}, {u'@value': u'\u0414\u0436\u043e\u0440\u0434\u0430\u043d, \u041c\u0430\u0439\u043a\u043b', u'@language': u'ru'}, {u'@value': u"\u05de\u05d9\u05d9\u05e7\u05dc \u05d2'\u05d5\u05e8\u05d3\u05df", u'@language': u'he'}, {u'@value': u'\u0645\u0627\u064a\u0643\u0644 \u062c\u0640\u0648\u0631\u062f\u0646', u'@language': u'ar'}, {u'@value': u'\u8fc8\u514b\u5c14\xb7\u4e54\u4e39', u'@language': u'zh'}]}, {u'enhancer:extracted-from': u'urn:content-item-sha1-45b6ea86a835e2b74c1f2cdde54a0002cf0e012d', u'enhancer:confidence': 0.14285763, u'dc:language': u'de', u'dc:creator': u'org.apache.stanbol.enhancer.engines.langdetect.LanguageDetectionEnhancementEngine', u'dc:type': u'dc:LinguisticSystem', u'dc:created': u'2014-01-09T18:19:26.166Z', u'@id': u'urn:enhancement-705a31cf-26f1-230c-b2cb-35e53ec73e68', u'@type': [u'enhancer:Enhancement', u'enhancer:TextAnnotation']}, {u'enhancer:extracted-from': u'urn:content-item-sha1-45b6ea86a835e2b74c1f2cdde54a0002cf0e012d', u'enhancer:confidence': 1.0, u'dc:creator': u'org.apache.stanbol.enhancer.engines.entitylinking.engine.EntityLinkingEngine', u'enhancer:entity-label': {u'@value': u'Michael Jordan', u'@language': u'en'}, u'entityhub:site': u'dbpedia', u'dc:relation': u'urn:enhancement-cd919618-5590-20f1-98b2-ad836bd2baf5', u'dc:created': u'2014-01-09T18:19:26.271Z', u'enhancer:entity-type': [u'dbp-ont:Agent', u'dbp-ont:Athlete', u'dbp-ont:BasketballPlayer', u'dbp-ont:Person', u'schema:Person', u'owl:Thing', u'foaf:Person'], u'@id': u'urn:enhancement-7d2c4b77-c9a6-72aa-ab5b-ab57e81d6493', u'@type': [u'enhancer:Enhancement', u'enhancer:EntityAnnotation'], u'enhancer:entity-reference': u'http://dbpedia.org/resource/Michael_Jordan'}, {u'enhancer:extracted-from': u'urn:content-item-sha1-45b6ea86a835e2b74c1f2cdde54a0002cf0e012d', u'enhancer:confidence': 0.28571513, u'dc:language': u'nl', u'dc:creator': u'org.apache.stanbol.enhancer.engines.langdetect.LanguageDetectionEnhancementEngine', u'dc:type': u'dc:LinguisticSystem', u'dc:created': u'2014-01-09T18:19:26.166Z', u'@id': u'urn:enhancement-89fd037c-8975-a25b-20e4-604cd72e0c75', u'@type': [u'enhancer:Enhancement', u'enhancer:TextAnnotation']}, {u'enhancer:extracted-from': u'urn:content-item-sha1-45b6ea86a835e2b74c1f2cdde54a0002cf0e012d', u'enhancer:confidence': 0.5714272, u'dc:language': u'en', u'dc:creator': u'org.apache.stanbol.enhancer.engines.langdetect.LanguageDetectionEnhancementEngine', u'dc:type': u'dc:LinguisticSystem', u'dc:created': u'2014-01-09T18:19:26.166Z', u'@id': u'urn:enhancement-a858a580-e2e4-7c7a-2735-a7d3e4b0bde9', u'@type': [u'enhancer:Enhancement', u'enhancer:TextAnnotation']}, {u'enhancer:extracted-from': u'urn:content-item-sha1-45b6ea86a835e2b74c1f2cdde54a0002cf0e012d', u'enhancer:confidence': 1.0, u'dc:creator': u'org.apache.stanbol.enhancer.engines.entitylinking.engine.EntityLinkingEngine', u'dc:type': u'dbp-ont:Person', u'enhancer:start': 0, u'enhancer:end': 14, u'enhancer:selected-text': {u'@value': u'Michael Jordan', u'@language': u'en'}, u'dc:created': u'2014-01-09T18:19:26.271Z', u'enhancer:selection-context': {u'@value': u'Michael Jordan', u'@language': u'en'}, u'@id': u'urn:enhancement-cd919618-5590-20f1-98b2-ad836bd2baf5', u'@type': [u'enhancer:Enhancement', u'enhancer:TextAnnotation']}]}
j = resp.json()
type(j)
# OUT: <type 'dict'>
j
# OUT: {u'@context': {u'enhancer': u'http://fise.iks-project.eu/ontology/', u'enhancer:confidence': {u'@type': u'xsd:double'}, u'dc:creator': {u'@type': u'xsd:string'}, u'dc:type': {u'@type': u'@id'}, u'dbp-ont': u'http://dbpedia.org/ontology/', u'enhancer:start': {u'@type': u'xsd:int'}, u'dc': u'http://purl.org/dc/terms/', u'entityhub': u'http://stanbol.apache.org/ontology/entityhub/entityhub#', u'dc:relation': {u'@type': u'@id'}, u'dc:created': {u'@type': u'xsd:dateTime'}, u'enhancer:entity-type': {u'@type': u'@id'}, u'foaf': u'http://xmlns.com/foaf/0.1/', u'xsd': u'http://www.w3.org/2001/XMLSchema#', u'enhancer:extracted-from': {u'@type': u'@id'}, u'foaf:depiction': {u'@type': u'@id'}, u'rdfs': u'http://www.w3.org/2000/01/rdf-schema#', u'owl': u'http://www.w3.org/2002/07/owl#', u'enhancer:end': {u'@type': u'xsd:int'}, u'enhancer:entity-reference': {u'@type': u'@id'}, u'schema': u'http://schema.org/'}, u'@graph': [{u'foaf:depiction': [u'http://upload.wikimedia.org/wikipedia/commons/b/b3/Jordan_Lipofsky.jpg', u'http://upload.wikimedia.org/wikipedia/commons/thumb/b/b3/Jordan_Lipofsky.jpg/200px-Jordan_Lipofsky.jpg'], u'rdfs:comment': {u'@value': u'Michael Jeffrey Jordan (born February 17, 1963) is a retired American professional basketball player, active entrepreneur, and majority owner of the Charlotte Bobcats. His biography on the National Basketball Association (NBA) website states, "By acclamation, Michael Jordan is the greatest basketball player of all time. " Jordan was one of the most effectively marketed athletes of his generation and was considered instrumental in popularizing the NBA around the world in the 1980s and 1990s.', u'@language': u'en'}, u'@id': u'http://dbpedia.org/resource/Michael_Jordan', u'@type': [u'dbp-ont:Agent', u'dbp-ont:Athlete', u'dbp-ont:BasketballPlayer', u'dbp-ont:Person', u'foaf:Person', u'owl:Thing', u'schema:Person'], u'rdfs:label': [{u'@value': u'Michael Jordan', u'@language': u'de'}, {u'@value': u'Michael Jordan', u'@language': u'en'}, {u'@value': u'Michael Jordan', u'@language': u'es'}, {u'@value': u'Michael Jordan', u'@language': u'fr'}, {u'@value': u'Michael Jordan', u'@language': u'it'}, {u'@value': u'Michael Jordan', u'@language': u'pt'}, {u'@value': u'Michael Jordan', u'@language': u'tr'}, {u'@value': u'\u0414\u0436\u043e\u0440\u0434\u0430\u043d, \u041c\u0430\u0439\u043a\u043b', u'@language': u'ru'}, {u'@value': u"\u05de\u05d9\u05d9\u05e7\u05dc \u05d2'\u05d5\u05e8\u05d3\u05df", u'@language': u'he'}, {u'@value': u'\u0645\u0627\u064a\u0643\u0644 \u062c\u0640\u0648\u0631\u062f\u0646', u'@language': u'ar'}, {u'@value': u'\u8fc8\u514b\u5c14\xb7\u4e54\u4e39', u'@language': u'zh'}]}, {u'enhancer:extracted-from': u'urn:content-item-sha1-45b6ea86a835e2b74c1f2cdde54a0002cf0e012d', u'enhancer:confidence': 0.14285763, u'dc:language': u'de', u'dc:creator': u'org.apache.stanbol.enhancer.engines.langdetect.LanguageDetectionEnhancementEngine', u'dc:type': u'dc:LinguisticSystem', u'dc:created': u'2014-01-09T18:19:26.166Z', u'@id': u'urn:enhancement-705a31cf-26f1-230c-b2cb-35e53ec73e68', u'@type': [u'enhancer:Enhancement', u'enhancer:TextAnnotation']}, {u'enhancer:extracted-from': u'urn:content-item-sha1-45b6ea86a835e2b74c1f2cdde54a0002cf0e012d', u'enhancer:confidence': 1.0, u'dc:creator': u'org.apache.stanbol.enhancer.engines.entitylinking.engine.EntityLinkingEngine', u'enhancer:entity-label': {u'@value': u'Michael Jordan', u'@language': u'en'}, u'entityhub:site': u'dbpedia', u'dc:relation': u'urn:enhancement-cd919618-5590-20f1-98b2-ad836bd2baf5', u'dc:created': u'2014-01-09T18:19:26.271Z', u'enhancer:entity-type': [u'dbp-ont:Agent', u'dbp-ont:Athlete', u'dbp-ont:BasketballPlayer', u'dbp-ont:Person', u'schema:Person', u'owl:Thing', u'foaf:Person'], u'@id': u'urn:enhancement-7d2c4b77-c9a6-72aa-ab5b-ab57e81d6493', u'@type': [u'enhancer:Enhancement', u'enhancer:EntityAnnotation'], u'enhancer:entity-reference': u'http://dbpedia.org/resource/Michael_Jordan'}, {u'enhancer:extracted-from': u'urn:content-item-sha1-45b6ea86a835e2b74c1f2cdde54a0002cf0e012d', u'enhancer:confidence': 0.28571513, u'dc:language': u'nl', u'dc:creator': u'org.apache.stanbol.enhancer.engines.langdetect.LanguageDetectionEnhancementEngine', u'dc:type': u'dc:LinguisticSystem', u'dc:created': u'2014-01-09T18:19:26.166Z', u'@id': u'urn:enhancement-89fd037c-8975-a25b-20e4-604cd72e0c75', u'@type': [u'enhancer:Enhancement', u'enhancer:TextAnnotation']}, {u'enhancer:extracted-from': u'urn:content-item-sha1-45b6ea86a835e2b74c1f2cdde54a0002cf0e012d', u'enhancer:confidence': 0.5714272, u'dc:language': u'en', u'dc:creator': u'org.apache.stanbol.enhancer.engines.langdetect.LanguageDetectionEnhancementEngine', u'dc:type': u'dc:LinguisticSystem', u'dc:created': u'2014-01-09T18:19:26.166Z', u'@id': u'urn:enhancement-a858a580-e2e4-7c7a-2735-a7d3e4b0bde9', u'@type': [u'enhancer:Enhancement', u'enhancer:TextAnnotation']}, {u'enhancer:extracted-from': u'urn:content-item-sha1-45b6ea86a835e2b74c1f2cdde54a0002cf0e012d', u'enhancer:confidence': 1.0, u'dc:creator': u'org.apache.stanbol.enhancer.engines.entitylinking.engine.EntityLinkingEngine', u'dc:type': u'dbp-ont:Person', u'enhancer:start': 0, u'enhancer:end': 14, u'enhancer:selected-text': {u'@value': u'Michael Jordan', u'@language': u'en'}, u'dc:created': u'2014-01-09T18:19:26.271Z', u'enhancer:selection-context': {u'@value': u'Michael Jordan', u'@language': u'en'}, u'@id': u'urn:enhancement-cd919618-5590-20f1-98b2-ad836bd2baf5', u'@type': [u'enhancer:Enhancement', u'enhancer:TextAnnotation']}]}
import pprint
pprint.pprint(j)
# OUT: {u'@context': {u'dbp-ont': u'http://dbpedia.org/ontology/',
# OUT:                u'dc': u'http://purl.org/dc/terms/',
# OUT:                u'dc:created': {u'@type': u'xsd:dateTime'},
# OUT:                u'dc:creator': {u'@type': u'xsd:string'},
# OUT:                u'dc:relation': {u'@type': u'@id'},
# OUT:                u'dc:type': {u'@type': u'@id'},
# OUT:                u'enhancer': u'http://fise.iks-project.eu/ontology/',
# OUT:                u'enhancer:confidence': {u'@type': u'xsd:double'},
# OUT:                u'enhancer:end': {u'@type': u'xsd:int'},
# OUT:                u'enhancer:entity-reference': {u'@type': u'@id'},
# OUT:                u'enhancer:entity-type': {u'@type': u'@id'},
# OUT:                u'enhancer:extracted-from': {u'@type': u'@id'},
# OUT:                u'enhancer:start': {u'@type': u'xsd:int'},
# OUT:                u'entityhub': u'http://stanbol.apache.org/ontology/entityhub/entityhub#',
# OUT:                u'foaf': u'http://xmlns.com/foaf/0.1/',
# OUT:                u'foaf:depiction': {u'@type': u'@id'},
# OUT:                u'owl': u'http://www.w3.org/2002/07/owl#',
# OUT:                u'rdfs': u'http://www.w3.org/2000/01/rdf-schema#',
# OUT:                u'schema': u'http://schema.org/',
# OUT:                u'xsd': u'http://www.w3.org/2001/XMLSchema#'},
# OUT:  u'@graph': [{u'@id': u'http://dbpedia.org/resource/Michael_Jordan',
# OUT:               u'@type': [u'dbp-ont:Agent',
# OUT:                          u'dbp-ont:Athlete',
# OUT:                          u'dbp-ont:BasketballPlayer',
# OUT:                          u'dbp-ont:Person',
# OUT:                          u'foaf:Person',
# OUT:                          u'owl:Thing',
# OUT:                          u'schema:Person'],
# OUT:               u'foaf:depiction': [u'http://upload.wikimedia.org/wikipedia/commons/b/b3/Jordan_Lipofsky.jpg',
# OUT:                                   u'http://upload.wikimedia.org/wikipedia/commons/thumb/b/b3/Jordan_Lipofsky.jpg/200px-Jordan_Lipofsky.jpg'],
# OUT:               u'rdfs:comment': {u'@language': u'en',
# OUT:                                 u'@value': u'Michael Jeffrey Jordan (born February 17, 1963) is a retired American professional basketball player, active entrepreneur, and majority owner of the Charlotte Bobcats. His biography on the National Basketball Association (NBA) website states, "By acclamation, Michael Jordan is the greatest basketball player of all time. " Jordan was one of the most effectively marketed athletes of his generation and was considered instrumental in popularizing the NBA around the world in the 1980s and 1990s.'},
# OUT:               u'rdfs:label': [{u'@language': u'de',
# OUT:                                u'@value': u'Michael Jordan'},
# OUT:                               {u'@language': u'en',
# OUT:                                u'@value': u'Michael Jordan'},
# OUT:                               {u'@language': u'es',
# OUT:                                u'@value': u'Michael Jordan'},
# OUT:                               {u'@language': u'fr',
# OUT:                                u'@value': u'Michael Jordan'},
# OUT:                               {u'@language': u'it',
# OUT:                                u'@value': u'Michael Jordan'},
# OUT:                               {u'@language': u'pt',
# OUT:                                u'@value': u'Michael Jordan'},
# OUT:                               {u'@language': u'tr',
# OUT:                                u'@value': u'Michael Jordan'},
# OUT:                               {u'@language': u'ru',
# OUT:                                u'@value': u'\u0414\u0436\u043e\u0440\u0434\u0430\u043d, \u041c\u0430\u0439\u043a\u043b'},
# OUT:                               {u'@language': u'he',
# OUT:                                u'@value': u"\u05de\u05d9\u05d9\u05e7\u05dc \u05d2'\u05d5\u05e8\u05d3\u05df"},
# OUT:                               {u'@language': u'ar',
# OUT:                                u'@value': u'\u0645\u0627\u064a\u0643\u0644 \u062c\u0640\u0648\u0631\u062f\u0646'},
# OUT:                               {u'@language': u'zh',
# OUT:                                u'@value': u'\u8fc8\u514b\u5c14\xb7\u4e54\u4e39'}]},
# OUT:              {u'@id': u'urn:enhancement-705a31cf-26f1-230c-b2cb-35e53ec73e68',
# OUT:               u'@type': [u'enhancer:Enhancement',
# OUT:                          u'enhancer:TextAnnotation'],
# OUT:               u'dc:created': u'2014-01-09T18:19:26.166Z',
# OUT:               u'dc:creator': u'org.apache.stanbol.enhancer.engines.langdetect.LanguageDetectionEnhancementEngine',
# OUT:               u'dc:language': u'de',
# OUT:               u'dc:type': u'dc:LinguisticSystem',
# OUT:               u'enhancer:confidence': 0.14285763,
# OUT:               u'enhancer:extracted-from': u'urn:content-item-sha1-45b6ea86a835e2b74c1f2cdde54a0002cf0e012d'},
# OUT:              {u'@id': u'urn:enhancement-7d2c4b77-c9a6-72aa-ab5b-ab57e81d6493',
# OUT:               u'@type': [u'enhancer:Enhancement',
# OUT:                          u'enhancer:EntityAnnotation'],
# OUT:               u'dc:created': u'2014-01-09T18:19:26.271Z',
# OUT:               u'dc:creator': u'org.apache.stanbol.enhancer.engines.entitylinking.engine.EntityLinkingEngine',
# OUT:               u'dc:relation': u'urn:enhancement-cd919618-5590-20f1-98b2-ad836bd2baf5',
# OUT:               u'enhancer:confidence': 1.0,
# OUT:               u'enhancer:entity-label': {u'@language': u'en',
# OUT:                                          u'@value': u'Michael Jordan'},
# OUT:               u'enhancer:entity-reference': u'http://dbpedia.org/resource/Michael_Jordan',
# OUT:               u'enhancer:entity-type': [u'dbp-ont:Agent',
# OUT:                                         u'dbp-ont:Athlete',
# OUT:                                         u'dbp-ont:BasketballPlayer',
# OUT:                                         u'dbp-ont:Person',
# OUT:                                         u'schema:Person',
# OUT:                                         u'owl:Thing',
# OUT:                                         u'foaf:Person'],
# OUT:               u'enhancer:extracted-from': u'urn:content-item-sha1-45b6ea86a835e2b74c1f2cdde54a0002cf0e012d',
# OUT:               u'entityhub:site': u'dbpedia'},
# OUT:              {u'@id': u'urn:enhancement-89fd037c-8975-a25b-20e4-604cd72e0c75',
# OUT:               u'@type': [u'enhancer:Enhancement',
# OUT:                          u'enhancer:TextAnnotation'],
# OUT:               u'dc:created': u'2014-01-09T18:19:26.166Z',
# OUT:               u'dc:creator': u'org.apache.stanbol.enhancer.engines.langdetect.LanguageDetectionEnhancementEngine',
# OUT:               u'dc:language': u'nl',
# OUT:               u'dc:type': u'dc:LinguisticSystem',
# OUT:               u'enhancer:confidence': 0.28571513,
# OUT:               u'enhancer:extracted-from': u'urn:content-item-sha1-45b6ea86a835e2b74c1f2cdde54a0002cf0e012d'},
# OUT:              {u'@id': u'urn:enhancement-a858a580-e2e4-7c7a-2735-a7d3e4b0bde9',
# OUT:               u'@type': [u'enhancer:Enhancement',
# OUT:                          u'enhancer:TextAnnotation'],
# OUT:               u'dc:created': u'2014-01-09T18:19:26.166Z',
# OUT:               u'dc:creator': u'org.apache.stanbol.enhancer.engines.langdetect.LanguageDetectionEnhancementEngine',
# OUT:               u'dc:language': u'en',
# OUT:               u'dc:type': u'dc:LinguisticSystem',
# OUT:               u'enhancer:confidence': 0.5714272,
# OUT:               u'enhancer:extracted-from': u'urn:content-item-sha1-45b6ea86a835e2b74c1f2cdde54a0002cf0e012d'},
# OUT:              {u'@id': u'urn:enhancement-cd919618-5590-20f1-98b2-ad836bd2baf5',
# OUT:               u'@type': [u'enhancer:Enhancement',
# OUT:                          u'enhancer:TextAnnotation'],
# OUT:               u'dc:created': u'2014-01-09T18:19:26.271Z',
# OUT:               u'dc:creator': u'org.apache.stanbol.enhancer.engines.entitylinking.engine.EntityLinkingEngine',
# OUT:               u'dc:type': u'dbp-ont:Person',
# OUT:               u'enhancer:confidence': 1.0,
# OUT:               u'enhancer:end': 14,
# OUT:               u'enhancer:extracted-from': u'urn:content-item-sha1-45b6ea86a835e2b74c1f2cdde54a0002cf0e012d',
# OUT:               u'enhancer:selected-text': {u'@language': u'en',
# OUT:                                           u'@value': u'Michael Jordan'},
# OUT:               u'enhancer:selection-context': {u'@language': u'en',
# OUT:                                               u'@value': u'Michael Jordan'},
# OUT:               u'enhancer:start': 0}]}



