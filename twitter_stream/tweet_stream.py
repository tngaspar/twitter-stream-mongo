import tweepy
import time
from mongodb import TweetColection
from elasticsearch import Elasticsearch

es = Elasticsearch("http://elasticsearch:9200")

class TweetStream(tweepy.StreamingClient):
    
    def __init__(self, bearer_token, \
                mongo_host_name, mongo_db_name, mongo_collection_name, print_cli:bool = False):
        
        tweepy.StreamingClient.__init__(self, bearer_token)
        self.colection = TweetColection(mongo_host_name, mongo_db_name, mongo_collection_name)
        self.print_cli = print_cli       
        
    def on_connect(self):
        print("Successful Connection\n")
        
    def on_tweet(self, tweet):
        # rename dict key
        tweet_dict = tweet.data
        tweet_dict["tweet_id"] = tweet_dict.pop("id")

        #insert to es
        es.index(index="tweetdb",
                 document=tweet_dict)
        
        #insert to db
        self.colection.insert(tweet_dict)

        
        if self.print_cli is True:
            print("URL: https://twitter.com/twitter/status/"+tweet_dict.get('tweet_id'))
            print("Text: ",tweet_dict.get('text'),"\n") 
        
        time.sleep(0.1)
        
    def delete_all_rules(self):
        rules = self.get_rules()
        if type(rules.data):
            for rule in rules.data or []:
                self.delete_rules(rule.id)
                
    def add_rules(self, rule: str):
        return tweepy.StreamingClient.add_rules(self, tweepy.StreamRule(rule))
        
    def create_rule(self, rule_str: str ,language:str='en', replies:bool = False, retweets:bool = False, quote_tweets:bool = True):
        
        #language
        rule_str += ' lang:' + language
        
        #conjunction terms:
        if not replies:
            rule_str += ' -is:reply'
        if not retweets: 
            rule_str += ' -is:retweet'
        if not quote_tweets: 
            rule_str += ' -is:quote'
        
        print(rule_str)
        return self.add_rules(rule_str)    

    def create_inclusion_exclusion_rule(self, include:list, exclude:list=None ,language:str='en', replies:bool = False, retweets:bool = False, quote_tweets:bool = True):

        rule_str = ''
        #inclusion list
        include = ['"'+ elem + '"' for elem in include]
        rule_str += ' '.join(map(str, include))
        
        #exclusion list
        if exclude is not None:
            exclude = ['-"'+ elem + '"' for elem in exclude]
            rule_str += ' '+' '.join(map(str, exclude))

        return self.create_rule(rule_str, language, replies, retweets, quote_tweets)
    
    
    def filter(self, tweet_fields:list=['author_id', 'created_at', 'entities', 'geo']):
        tweepy.StreamingClient.filter(self, tweet_fields=tweet_fields)
        
