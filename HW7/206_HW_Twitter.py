import unittest
import tweepy
import requests
import json
import twitter_info

## SI 206 - HW
## COMMENT WITH:
## Your section day/time: Wednesday 6-7
## Any names of people you worked with on this assignment:


## Write code that uses the tweepy library to search for tweets with three different phrases of the 
## user's choice (should use the Python input function), and prints out the Tweet text and the 
## created_at value (note that this will be in GMT time) of the first FIVE tweets with at least 
## 1 blank line in between each of them, e.g.


## You should cache all of the data from this exercise in a file, and submit the cache file 
## along with your assignment. 

## So, for example, if you submit your assignment files, and you have already searched for tweets 
## about "rock climbing", when we run your code, the code should use CACHED data, and should not 
## need to make any new request to the Twitter API.  But if, for instance, you have never 
## searched for "bicycles" before you submitted your final files, then if we enter "bicycles" 
## when we run your code, it _should_ make a request to the Twitter API.

## Because it is dependent on user input, there are no unit tests for this -- we will 
## run your assignments in a batch to grade them!

## We've provided some starter code below, like what is in the class tweepy examples.

##SAMPLE OUTPUT
## See: https://docs.google.com/a/umich.edu/document/d/1o8CWsdO2aRT7iUz9okiCHCVgU5x_FyZkabu2l9qwkf8/edit?usp=sharing



## **** For extra credit, create another file called twitter_info.py that 
## contains your consumer_key, consumer_secret, access_token, and access_token_secret, 
## import that file here.  Do NOT add and commit that file to a public GitHub repository.

## **** If you choose not to do that, we strongly advise using authentication information 
## for an 'extra' Twitter account you make just for this class, and not your personal 
## account, because it's not ideal to share your authentication information for a real 
## account that you use frequently.

## Get your secret values to authenticate to Twitter. You may replace each of these 
## with variables rather than filling in the empty strings if you choose to do the secure way 
## for EC points

#consumer_key = "a6IMZVWT6HFrQYKEqdmdena51" 
#consumer_secret = "cuBVDftT4hKTsumFgtc2HstAtlQDIRAYN5nTbaQVdUi6gbBaKk"
#access_token = "3161503221-fwDGO7JQNGOXRwki0NxHPsei1BTBJ4uFHinG0T3"
#access_token_secret = "k6lyIPkdPn86zxZJiqCHJxjcp767fANjcxbvRnWNWj6jw"

consumer_key = twitter_info.consumer_key
consumer_secret = twitter_info.consumer_secret
access_token = twitter_info.access_token
access_token_secret = twitter_info.access_token_secret

## Set up your authentication to Twitter
auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)
# Set up library to grab stuff from twitter with your authentication, and 
# return it in a JSON-formatted way

api = tweepy.API(auth, parser=tweepy.parsers.JSONParser())
#public_tweets = api.home_timeline()

def pretty(obj):
    return json.dumps(obj, sort_keys=True, indent=2)

CACHE_FNAME = 'twitter_cache.json'

## Write the rest of your code here!

#### Recommended order of tasks: ####
## 1. Set up the caching pattern start -- the dictionary and the try/except 
## 		statement shown in class.

try:
    cache_file = open(CACHE_FNAME, 'r') # Try to read the data from the file
    cache_contents = cache_file.read()  # If it's there, get it into a string
    CACHE_DICTION = json.loads(cache_contents) # And then load it into a dictionary (Python Object)
    cache_file.close() # Close the file
except:
    CACHE_DICTION = {} #If opening the cached data doesn't work then create an empty dictionary to hold the data I'll be caching


## 2. Write a function to get twitter data that works with the caching pattern, 
## 		so it either gets new data or caches data, depending upon what the input 
##		to search for is. 

## Helper functions not necessary

def getTweetsWithCaching(loc):

    if loc in CACHE_DICTION:
        print("using cache")
        return CACHE_DICTION[loc] #if the data (returned from what you searched) is in the cache dictionary already, if so grab it and return it to use
    else:
        print("fetching")
        results = api.search(q = term, count = 5) #If not in cache dictionary, make a request to tweepy api and return dictionary
        try:
            CACHE_DICTION[term] = results #Add key-value pair to cache dictionary, where the key is the request, and the data you get back from that request.
            dumped_json_cache = json.dumps(CACHE_DICTION) #Dump the whole cache dictionary to a string
            fw = open(CACHE_FNAME,"w") #open the file for writing 
            fw.write(dumped_json_cache) #write the string version of the cache dictionary to that dictionary
            fw.close() # Close the open file
            return CACHE_DICTION[loc]
        except:
            print("Wasn't in cache and wasn't valid search either")
            return None


## 3. Using a loop, invoke your function, save the return value in a variable, and explore the 
##		data you got back!

while True:
	term = input("Insert three different phrases: ") 
	data = getTweetsWithCaching(term)
	break
	
## 4. With what you learn from the data -- e.g. how exactly to find the 
##		text of each tweet in the big nested structure -- write code to print out 
## 		content from 5 tweets, as shown in the linked example.

#print (pretty(data))
for tweet in data['statuses']: #iterate through the statuses dictionary
	text = tweet['text'] #pull out the test of each tweet
	created = tweet['created_at'] #pull out when the tweet was created
	print ('TEXT:', text)
	print ('CREATED AT:', created)
	print ('\n')







