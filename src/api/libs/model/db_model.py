#!/usr/local/bin/python3
# -*- coding: utf-8 -*-
import mongoengine

class Tweet(mongoengine.Document):
    
    userName = mongoengine.StringField()
    userId = mongoengine.StringField()
    followers = mongoengine.IntField()
    dateTime = mongoengine.DateTimeField()
    tag = mongoengine.StringField()
    body = mongoengine.StringField()
    lang = mongoengine.StringField()
    location = mongoengine.StringField()
""" 
USAGE EXAMPLE


from api.libs.models.dbModel import User
from api.libs.models.dbModel import Tweet
from mongoengine import connect
from mongoengine import disconnect
import mongoengine
connect('tweetcatcher', host='mongo')
tweetRecord = Tweet(dateTime="2018-12-19 09:26:03.478039", tag="#devops", body="Devops é muito massa")
userRecord = User(userName="atilaloise", userId="1", followers=10000)
userRecord.tweets.append(tweetRecord)
userRecord.save()
disconnect()
User.objects.first() 

""" 
