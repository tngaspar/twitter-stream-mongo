from config import (bearer_token, mdb_host_name, 
                    mdb_database_name, mdb_collection_name, search_rule)
from tweet_stream import TweetStream


stream  = TweetStream(bearer_token, mdb_host_name, mdb_database_name, mdb_collection_name, print_cli=True)

#delete any existing rules from previous runs
stream.delete_all_rules()

# apply rules
stream.create_rule(search_rule)

#check valid rules
print(stream.get_rules())

stream.filter()