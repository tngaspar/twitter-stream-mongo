from flask import Flask, request, render_template 
from elasticsearch import Elasticsearch

app = Flask(__name__)

esearch = Elasticsearch("http://localhost:9200/")

@app.route('/')
def index():
    return render_template('index.html')

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

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)