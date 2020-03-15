#!/usr/local/bin/python3
from pymongo import MongoClient
import pprint

class DbHandler():
    def __init__(self):
        self.client = MongoClient('localhost', 27017)
        self.db = self.client.tweetcatcher
    def GetByDayHour(self):
        self.query = [
                  {
                      '$group': {
                          '_id': {
                              '$dateToString': {
                                  'format': '%H_horas', 
                                  'date': '$dateTime'
                              }
                          }, 
                          'count': {
                              '$sum': 1
                          }
                      }
                  }
              ]
        return list(self.db.tweet.aggregate(self.query))
    def GetByTagLocationLang(self):
        self.query = [
                        {
                            '$group': {
                                '_id': {
                                    'Lang': '$lang', 
                                    'Location': '$location', 
                                    'tag': '$tag'
                                }, 
                                'count': {
                                    '$sum': 1
                                }
                            }
                        }
                    ]
        return list(self.db.tweet.aggregate(self.query))


'''
USO:

from libs.handler.get_from_db import GetFromDb

query = GetFromDb()
query.GetByDayHour()
query.GetByTagLocationLang()
'''
