import os
from tweet_stream import TweetStream

# Get environment variables
BEARER_TOKEN = os.environ.get("BEARER_TOKEN")
MDB_HOST_NAME = os.environ.get("MDB_HOST_NAME")
MDB_DATABASE_NAME = os.environ.get("MDB_DATABASE_NAME")
MDB_COLLECTION_NAME = os.environ.get("MDB_COLLECTION_NAME")
SEARCH_RULE = os.environ.get("SEARCH_RULE")

stream  = TweetStream(BEARER_TOKEN, MDB_HOST_NAME, MDB_DATABASE_NAME, MDB_COLLECTION_NAME, print_cli=False)

#delete any existing rules from previous runs
stream.delete_all_rules()

# apply rules
stream.create_rule(SEARCH_RULE)

#check valid rules
print(stream.get_rules())

stream.filter()