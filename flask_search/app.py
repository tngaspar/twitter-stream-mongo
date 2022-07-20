from flask import Flask, request, render_template 
from elasticsearch import Elasticsearch

app = Flask(__name__)

esearch = Elasticsearch("http://elasticsearch:9200")

@app.route('/')
def index():
    response = esearch.cat.count(
        index="tweetdb",
        params={"format":"json"}
    )
    
    return render_template('index.html', response=response[0])

@app.route('/search', methods=['GET', 'POST'])
def search():
    form_term = request.form["search"]
    response = esearch.search(
        index="tweetdb",
        size=100, 
        body={
            "query": {
                "multi_match" : {
                    "query": form_term, 
                    "fields": [
                        "text"
                    ] 
                }
            }
        }
    )
    return render_template('search.html', response=response )

@app.route('/last')
def last():
    response = esearch.search(
        index="tweetdb",
        size=100, 
        body={
            "sort": [
                    {
                    "created_at": {
                        "order": "desc"
                    }
                    }
                ]
        }
    )
    response_count = esearch.cat.count(
    index="tweetdb",
    params={"format":"json"}
    )
    return render_template('last.html', response=response, response_count=response_count[0] )

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)