##curl -X POST -H "Accept: application/json" -H "Content-type: text/plain" \
##     --data "The Stanbol enhancer can detect famous cities such as \
##             Paris and people such as Bob Marley." http://54.197.229.87:8080/enhancer/chain/dbpedia-proper-noun
##
##curl -X POST -H "Accept: text/plain" -H "Content-type: text/plain" \
##     --data "The Stanbol enhancer can detect famous cities such as \
##             Paris and people such as Bob Marley." http://54.197.229.87:8080/enhancer/chain/dbpedia-proper-noun?omitMetadata=true
#
##curl -v -X POST -H "Accept: text/plain" \
##    -H "Content-type: text/html; charset=UTF-8" \
##    --data "<html><body><p>The Stanbol enhancer \
##           can detect famous cities such as Paris and people such \
##           as Bob Marley.</p></body></html>" \
##    "http://54.197.229.87:8080/enhancer/?omitMetadata=true"
##curl -v -X POST -H "Accept: text/plain" \
##    -H "Content-type: text/html; charset=UTF-8" \
##    --data "<html><body><p>The Stanbol enhancer \
##           can detect famous cities such as Paris and people such \
##           as Bob Marley.</p></body></html>" \
##    "http://54.197.229.87:8080/enhancer/chain/dbpedia-proper-noun?omitMetadata=true"
##curl -v -X POST -H "Accept: multipart/from-data" \
##    -H "Content-type: text/html; charset=UTF-8"  \
##    --data "<html><body><p>The Stanbol enhancer \
##           can detect famous cities such as Paris and people such \
##           as Bob Marley..</p></body></html>" \
##    "http://54.197.229.87:8080/enhancer/chain/dbpedia-proper-noun?outputContent=*/*&omitParsed=true&rdfFormat=application/rdf%2Bxml"
##

###------- dbpedia spotlight

##curl -i -X POST \
##    -H "Accept:application/json" \
##    -H "content-type:application/x-www-form-urlencoded" \
##    -d "disambiguator=Document&confidence=-1&support=-1&text=President%20Obama%20called%20Wednesday%20on%20Congress%20to%20extend%20a%20tax%20break%20for%20students%20included%20in%20last%20year%27s%20economic%20stimulus%20package" \
##       http://spotlight.dbpedia.org/rest/annotate/

curl -X POST -H "Accept: application/json" -H "Content-type: text/plain" \
     --data "Albert Einstein" \
             http://54.197.229.87:8080/enhancer/chain/dbpedia-proper-noun
