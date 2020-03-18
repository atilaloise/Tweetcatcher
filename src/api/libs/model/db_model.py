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
