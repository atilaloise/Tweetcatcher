#!/usr/local/bin/python3
from libs.model.db_model import Tweet
from mongoengine import connect
from mongoengine import disconnect
from twython import Twython
import pandas as pd
import json

class TweetHandler(Twython):
  def GetTweetsByHashtag(self, hashtag):    
    self.hashtag = hashtag
    self.response = []
    self.dict_ = {'userName': [], 'userId': [], 'followers': [], 'lang': [], 'location': [], 'date': [], 'text': [], 'tag': []}
    self.query = self.search(q='{}'.format(self.hashtag), result_type='recent', count=100)
    connect('tweetcatcher', host='localhost')
    for tweet in self.query['statuses']:
      self.userName = tweet['user']['screen_name']
      self.userId = tweet['user']['id']
      self.followers = tweet['user']['followers_count']
      self.date = tweet['created_at']
      self.lang = tweet['metadata']['iso_language_code']
      self.location = tweet['user']['location']
      self.body = tweet['text'].replace('\n', ' ').replace('\r', '').replace('\'', '').replace('\"', '')
      self.tag = self.hashtag
      self.tweetInfo = json.loads(r'''{{"userName": "{}", "userId": "{}", "followers": "{}", "dateTime": "{}", "tag": "{}", "body": "{}", "lang": "{}", "location": "{}"}}'''.format(self.userName, self.userId, self.followers, self.date, self.tag, self.body, self.lang, self.location), strict=False)
      self.tweetRecord = Tweet(**self.tweetInfo)
      self.tweetRecord.save()
      self.dict_['userName'].append(tweet['user']['screen_name'])
      self.dict_['userId'].append(tweet['user']['id'])
      self.dict_['followers'].append(tweet['user']['followers_count'])
      self.dict_['lang'].append(tweet['metadata']['iso_language_code'])
      self.dict_['location'].append(tweet['user']['location'])
      self.dict_['date'].append(tweet['created_at'])
      self.dict_['text'].append(tweet['text'])
      self.dict_['tag'].append(self.hashtag)
    self.dataFrame = pd.DataFrame(self.dict_)
    self.dataFrame.sort_values(by='followers', inplace=True, ascending=False)
    #print(self.dataFrame.head(5))
    #print(self.dataFrame.head(5).to_json(orient='records'))
    self.response.append(json.loads(self.dataFrame.head(5).to_json(orient='records')))

    disconnect()
    return self.response
    
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



#    self.dict_ = {'userName': [], 'userId': [], 'followers': [], 'lang': [], 'location': [], 'date': [], 'text': [], 'tag': []}

#  self.dict_['userName'].append(tweet['user']['screen_name'])
#       self.dict_['userId'].append(tweet['user']['id'])
#       self.dict_['followers'].append(tweet['user']['followers_count'])
#       self.dict_['lang'].append(tweet['metadata']['iso_language_code'])
#       self.dict_['location'].append(tweet['user']['location'])
#       self.dict_['date'].append(tweet['created_at'])
#       self.dict_['text'].append(tweet['text'])
#       self.dict_['tag'].append(self.hashtag)
#     # ESTRUTURANDO DADOS EM DATAFRAMES PARA MELHOR visualização
#     self.dataFrame = pd.DataFrame(self.dict_)
#     self.dataFrame.sort_values(by='followers', inplace=True, ascending=False)
#     return self.dataFrame.head(5)