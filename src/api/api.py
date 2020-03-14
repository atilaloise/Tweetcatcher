#!/usr/local/bin/python3
# -*- coding: utf-8 -*-
from flask import Flask, request, jsonify
from flask_restful import Resource, Api
import json
from libs.handler.get_tweet import TweetHandler


TWITTER_APP_KEY = 'YezipOoweQ3FbSgyRihKZ5BbZ'  # supply the appropriate value
TWITTER_APP_KEY_SECRET = 'tWRn9kkswLkxbXK78aOuHbxvb7C1BG3SFZDfxVDHgIdLqkFkTy'
TWITTER_ACCESS_TOKEN = '1237878615942946818-BY4593QtzNK0Ryig8Jh203c8Stq7DO'
TWITTER_ACCESS_TOKEN_SECRET = 'gjlTPvFbNlGYnGh7011lgyjf8oiWOASSmp244Kce1KZ6S'

hashtags = ["#swagger"]
#hashtags = ["#openbanking", "#apifirst", "#devops", "cloudfirst", "#microservices", "#apigateway", "#oauth", "#swagger", "#raml", "#openapis"]


queryTwitter = TweetHandler(TWITTER_APP_KEY, TWITTER_APP_KEY_SECRET,TWITTER_ACCESS_TOKEN, TWITTER_ACCESS_TOKEN_SECRET)

for tag in hashtags:
  topFive = queryTwitter.GetTweetsByHashtag(tag)
  queryTwitter.StoreTweet()
  print(topFive)

# app = Flask(__name__)
# api = Api(app)


# class authorization(Resource):
#    def post(self):
#    	a = 1


# api.add_resource(authorization, '/authorization')
# if __name__ == '__main__':
#     app.run(host='0.0.0.0')
