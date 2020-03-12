# -*- coding: utf-8 -*-
import mongoengine

class Tweet(mongoengine.EmbeddedDocument):
    dateTime = mongoengine.DateTimeField()
    tag = mongoengine.StringField()
    body = mongoengine.StringField()

class User(mongoengine.Document):
    
    userName = mongoengine.StringField()
    userId = mongoengine.StringField()
    followers = mongoengine.IntField()
    tweets = mongoengine.ListField(mongoengine.EmbeddedDocumentField(Tweet))

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