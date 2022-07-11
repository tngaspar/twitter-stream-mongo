<h1 align="center">Twitter Stream</h1>

<p align="center">
<img src="https://img.shields.io/badge/-Python-2d2d2d?style=flat-square&logo=python"/>
<img src="https://img.shields.io/badge/-Docker-black?style=flat-square&logo=docker"/> 
<img src="https://img.shields.io/badge/-MongoDB-black?style=flat-square&logo=mongoDB"/>
<img src="https://img.shields.io/badge/-ElasticSearch-black?style=flat-square&logo=elasticsearch"/>
<img src="https://img.shields.io/badge/-Kibana-black?style=flat-square&logo=kibana"/> 
</p>
   
## Table of Contents
   1. [Features](#features) 
   2. [Project Components](#project-components)
   3. [Requirements](#requirements)
   4. [Installation](#installation)
   5. [Kibana](#kibana)
      1. [Kibana Dashboard](#kibana-dashboard)
      2. [Kibana Search](#kibana-search) 

## Features

* Dockerized realtime tweet streaming to <a href="https://www.mongodb.com/">MongoDB</a> based on search rules. <a href="https://github.com/tweepy/tweepy">Tweepy</a> used to connect to twitter API;
* MongoDB collection is continuously synced with an <a href="https://www.elastic.co/elasticsearch/">Elasticsearch</a> index using <a href="https://github.com/rwynn/monstache">Monstache</a>;
* MongoDB queried with <a href="https://github.com/rwynn/monstache">Mongo Express</a>, a web-based MongoDB admin interface;
* <a href="https://www.elastic.co/kibana/">Kibana</a> used to visualize and search tweets.


## Project Components
All components of the project are dockerized. The Streaming Client is initiated by `twitter_stream/Dockerfile`. All remaining containers are created from DockerHub images.

&nbsp;
<p align="center">
<img src="doc/architecture.png" width=90% />
</p>

## Requirements

* <a href="https://docs.docker.com/get-docker/">Docker</a>
* <a href="https://docs.docker.com/compose/install/">Docker Compose</a>

## Installation
1. Clone the repo:

```bash
$ git clone https://github.com/tngaspar/twitter-stream-mongo.git
```

2. Create `.env` file in project root folder with the following parameters:

```
API_KEY=[Twitter API key]
API_SECRET_KEY=[Twitter API secrect key]
BEARER_TOKEN=[Twitter API bearer token]
MDB_HOST_NAME=mongodb://root:[Password]@mongo:27017/
MDB_DATABASE_NAME=tweetdb
MDB_COLLECTION_NAME=tweets
SEARCH_RULE=[Twitter Filtered Stream rule]
MONGODB_ROOT_PASSWORD=[choose Password]
MONGODB_REPLICA_SET_KEY=[choose ReplicaKey]
```

Replace all fields between brackets. You may find the twitter documentation for the `SEARCH RULE` <a href="https://developer.twitter.com/en/docs/twitter-api/tweets/filtered-stream/integrate/build-a-rule">here</a>. By default the rule has `lang:en`, `-is:retweet` and `-is:reply` implicit so there's no need to add this parameters.

3. Add password to `mongo-url` on `monstache/monstache.config.toml`:

```toml
mongo-url = "mongodb://root:[Password]@mongo:27017" 
```
Replace fields between brackets.

4. In the project root directory run docker-compose:

```bash
$ docker-compose up -d
```

After this all containers should be up and running and the streaming initiated.

If running locally you can check MongoDB through Mongo Express at `localhost:8081` and search gathered tweets in Kibana at `localhost:5601`.


## Kibana

Kibana allows search and analysis of tweet data from Elasticsearch.

### Kibana Dashboard:

<p align="center">
<img src="doc/kibana_dashboard.png" width=100% />
</p>

This dashboard may be imported to Kibana by navigating to `Stack Management>Saved Objects>Import` and importing the file `doc/kibana_dashboard.ndjson`.

### Kibana Search:

Kibana uses syntax from Apache Lucene to query and filter data. 
Find out more <a href="https://lucene.apache.org/core/2_9_4/queryparsersyntax.html">here</a>.

Here's a simple example:

<p align="center">
<img src="doc/kibana_search.png" width=80% />
</p>

<p align="right">(<a href="#top">back to top</a>)</p>
