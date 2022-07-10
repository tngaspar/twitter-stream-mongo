# Twitter Stream – Mongo + Docker + ELK



## Features

* Dockerized realtime tweet streaming to <a href="https://www.mongodb.com/">MongoDB</a> based on search rules;
* MongoDB collection is continuosly synced with an <a href="https://www.elastic.co/elasticsearch/">Elasticsearch</a> index using <a href="https://github.com/rwynn/monstache">Monstache</a>;
* MongoDB queried with <a href="https://github.com/rwynn/monstache">Mongo Express</a>, a web-based MongoDB admin interface;
* <a href="https://www.elastic.co/kibana/">Kibana</a> used to visualize and search tweets.

&nbsp;
<h2 style="text-align: center;">Project Components</h2>
<p align="center">
<img src="doc/architecture.png" width=90% />
</p>