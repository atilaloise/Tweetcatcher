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
    connect('tweetcatcher', host='mongo')
    for tweet in self.query['statuses']:
      self.userName = tweet['user']['screen_name']
      self.userId = tweet['user']['id']
      self.followers = tweet['user']['followers_count']
      self.date = tweet['created_at']
      self.lang = tweet['metadata']['iso_language_code']
      self.location = tweet['user']['location']
      self.body = tweet['text'].replace('\n', ' ').replace('\r', '').replace('\'', '').replace('\"', '')
      self.tag = self.hashtag
      self.tweetInfo = json.loads(r'''{{"userName": "{}", "userId": "{}", "followers": "{}", "dateTime": "{}", "tag": "{}", "body": "{}", "lang": "{}", "location": "{}"}}'''.format(self.userName, self.userId, self.followers, self.date, self.tag, self.body, self.lang, self.location).replace("\\", ""), strict=False)
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
    