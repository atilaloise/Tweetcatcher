#!/usr/local/bin/python3
# -*- coding: utf-8 -*-
from flask import Flask, request, jsonify
from flask_restful import Resource, Api
import json
from libs.handler.get_tweet import TweetHandler
from libs.handler.get_from_db import DbHandler

# query = DbHandler()
# query.GetByDayHour()
# # #query.GetByTagLocationLang()

app = Flask(__name__)
api = Api(app)

class V1(Resource):
  def get(self):
     return "Bem vindo ao tweetCatcher"

class GetTweet(Resource):
  def get(self):
    self.TWITTER_APP_KEY = 'YezipOoweQ3FbSgyRihKZ5BbZ'  # supply the appropriate value
    self.TWITTER_APP_KEY_SECRET = 'tWRn9kkswLkxbXK78aOuHbxvb7C1BG3SFZDfxVDHgIdLqkFkTy'
    self.TWITTER_ACCESS_TOKEN = '1237878615942946818-BY4593QtzNK0Ryig8Jh203c8Stq7DO'
    self.TWITTER_ACCESS_TOKEN_SECRET = 'gjlTPvFbNlGYnGh7011lgyjf8oiWOASSmp244Kce1KZ6S'
    #self.hashtags = ["#swagger", "#devops"]
    self.hashtags = ["#openbanking", "#apifirst", "#devops", "#cloudfirst", "#microservices", "#apigateway", "#oauth", "#swagger", "#raml", "#openapis"]
    self.queryTwitter = TweetHandler(self.TWITTER_APP_KEY, self.TWITTER_APP_KEY_SECRET,self.TWITTER_ACCESS_TOKEN, self.TWITTER_ACCESS_TOKEN_SECRET)
    self.response = []
    for tag in self.hashtags:
      self.dict = {tag:[]}
      for item in self.queryTwitter.GetTweetsByHashtag(tag):
        self.dict[tag].append(item)
      self.response.append(self.dict)
    return self.response

class GetFromDB(Resource):
   def post(self):
   	a = 1

class GetByTagLocationLang(Resource):
   def post(self):
   	a = 1

class GetByDayHour(Resource):
   def post(self):
   	a = 1


api.add_resource(V1, '/v1')
api.add_resource(GetTweet, '/v1/tweets')
api.add_resource(GetFromDB, '/v1/tweets/GetFromDB')
api.add_resource(GetByTagLocationLang, '/v1/tweets/GetFromDB/bytaglocationlang')
api.add_resource(GetByDayHour, '/v1/tweets/GetFromDB/bydayhour')


if __name__ == '__main__':
    app.run(host='0.0.0.0')


# query = GetFromDb()
# query.GetByDayHour()
# query.GetByTagLocationLang()

# TWITTER_APP_KEY = 'YezipOoweQ3FbSgyRihKZ5BbZ'  # supply the appropriate value
# TWITTER_APP_KEY_SECRET = 'tWRn9kkswLkxbXK78aOuHbxvb7C1BG3SFZDfxVDHgIdLqkFkTy'
# TWITTER_ACCESS_TOKEN = '1237878615942946818-BY4593QtzNK0Ryig8Jh203c8Stq7DO'
# TWITTER_ACCESS_TOKEN_SECRET = 'gjlTPvFbNlGYnGh7011lgyjf8oiWOASSmp244Kce1KZ6S'

# hashtags = ["#swagger", "#devops"]
# # hashtags = ["#openbanking", "#apifirst", "#devops", "cloudfirst", "#microservices", "#apigateway", "#oauth", "#swagger", "#raml", "#openapis"]


# queryTwitter = TweetHandler(TWITTER_APP_KEY, TWITTER_APP_KEY_SECRET,TWITTER_ACCESS_TOKEN, TWITTER_ACCESS_TOKEN_SECRET)

# for tag in hashtags:
#   print(queryTwitter.GetTweetsByHashtag(tag))
#   queryTwitter.StoreTweet()
#   print(topFive)

