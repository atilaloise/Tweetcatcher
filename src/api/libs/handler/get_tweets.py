from twython import Twython
#import pandas as pd
import json
import re

class TweetHandler(Twython):
  def GetTweetsByHashtag(self, hashtag):    
    self.hashtag = hashtag
    self.dict_ = {'userName': [], 'userId': [], 'followers': [], 'date': [], 'text': [], 'tag': []}
    self.query = self.search(q='{}'.format(self.hashtag), result_type='recent', count=2)
    # for tweet in self.query['statuses']:
    #   self.dict_['userName'].append(tweet['user']['screen_name'])
    #   self.dict_['userId'].append(tweet['user']['id'])
    #   self.dict_['followers'].append(tweet['user']['followers_count'])
    #   self.dict_['date'].append(tweet['created_at'])
    #   self.dict_['text'].append(tweet['text'])
    #   self.dict_['tag'].append(self.hashtag)
    # # ESTRUTURANDO DADOS EM DATAFRAMES PARA MELHOR visualização
    # self.dataFrame = pd.DataFrame(self.dict_)
    # self.dataFrame.sort_values(by='followers', inplace=True, ascending=False)
    # return self.dataFrame.head(5)  
  def ParseRecordsForMongoEngine(self):
    self.records = []
    for tweet in self.query['statuses']:
      self.userName = tweet['user']['screen_name']
      self.userId = tweet['user']['id']
      self.followers = tweet['user']['followers_count']
      self.date = tweet['created_at']
      self.body = tweet['text'].replace('\n', ' ').replace('\r', '').replace('\'', '').replace('\"', '')
      self.tag = self.hashtag
      self.tweetRecord = '{{"dateTime": "{}", "tag": "{}", "body": "{}"}}'.format(self.date, self.tag, self.body)    
      self.record = '"{{"userName": "{}", "userId": "{}", "followers": "{}", "tweet": [{}]}}"'.format(self.userName, self.userId, self.followers, self.tweetRecord)    
      self.records.append(self.record)
    return self.records




""" 

Exemplo de uso


from api.libs.handler.get_tweets import TweetHandler


TWITTER_APP_KEY = 'YezipOoweQ3FbSgyRihKZ5BbZ'  #supply the appropriate value
TWITTER_APP_KEY_SECRET = 'tWRn9kkswLkxbXK78aOuHbxvb7C1BG3SFZDfxVDHgIdLqkFkTy' 
TWITTER_ACCESS_TOKEN = '1237878615942946818-BY4593QtzNK0Ryig8Jh203c8Stq7DO'
TWITTER_ACCESS_TOKEN_SECRET = 'gjlTPvFbNlGYnGh7011lgyjf8oiWOASSmp244Kce1KZ6S'

hashtags = ["#apifirst", "#openbanking"]
#hashtags = ["#openbanking", "#apifirst", "#devops", "cloudfirst", "#microservices", "#apigateway", "#oauth", "#swagger", "#raml", "#openapis"]


apiConnection = TweetHandler(TWITTER_APP_KEY, TWITTER_APP_KEY_SECRET, TWITTER_ACCESS_TOKEN, TWITTER_ACCESS_TOKEN_SECRET)

for tag in hashtags:
  print(tag)
  apiConnection.GetTweetsByHashtag(tag)
  payload = apiConnection.ParseRecordsForMongoEngine()
#   if payload:
#     print(payload)

for record in payload:
  print(record)



print(apiConnection.GetTweetsByHashtag.__self__.statuses)
print(apiConnection.GetTweetsByHashtag.__self__.query)
print(apiConnection.GetTweetsByHashtag.__self__.dataFrame.head(10))
print(apiConnection.GetTweetsByHashtag.__self__.query['statuses'][0]['text'])

 """
