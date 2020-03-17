#!/usr/local/bin/python3
# -*- coding: utf-8 -*-
from flask import Flask, request, jsonify, render_template, flash, redirect, url_for
from flask_restful import Resource, Api
import json
from libs.handler.get_tweet import TweetHandler
from libs.handler.get_from_db import DbHandler
from libs.handler.forms import CredentialsForm


app = Flask(__name__)
app.config['SECRET_KEY']= '75cea5dc74444b8389e5bc6ee0afc0da'

api = Api(app)

TWITTER_APP_KEY = ''
TWITTER_APP_KEY_SECRET = ''
TWITTER_ACCESS_TOKEN = ''
TWITTER_ACCESS_TOKEN_SECRET = ''
hashtags = []


class V1(Resource):
  def get(self):
     return "Bem vindo ao tweetCatcher"

class GetTweet(Resource):
  def get(self):
    global TWITTER_ACCESS_TOKEN_SECRET
    global TWITTER_ACCESS_TOKEN
    global TWITTER_APP_KEY
    global TWITTER_APP_KEY_SECRET
    global hashtags
    self.TWITTER_APP_KEY = TWITTER_APP_KEY
    self.TWITTER_APP_KEY_SECRET = TWITTER_APP_KEY_SECRET
    self.TWITTER_ACCESS_TOKEN = TWITTER_ACCESS_TOKEN
    self.TWITTER_ACCESS_TOKEN_SECRET = TWITTER_ACCESS_TOKEN_SECRET
    self.hashtags = hashtags
    self.queryTwitter = TweetHandler(self.TWITTER_APP_KEY, self.TWITTER_APP_KEY_SECRET,self.TWITTER_ACCESS_TOKEN, self.TWITTER_ACCESS_TOKEN_SECRET)
    self.response = []
    for tag in self.hashtags:
      self.dict = {tag:[]}
      for item in self.queryTwitter.GetTweetsByHashtag(tag):
        self.dict[tag].append(item)
      self.response.append(self.dict)
    return self.response
  def post(self):
    print(request.json)
    self.TWITTER_APP_KEY = request.json['TWITTER_APP_KEY']
    self.TWITTER_APP_KEY_SECRET = request.json['TWITTER_APP_KEY_SECRET']
    self.TWITTER_ACCESS_TOKEN = request.json['TWITTER_ACCESS_TOKEN']
    self.TWITTER_ACCESS_TOKEN_SECRET = request.json['TWITTER_ACCESS_TOKEN_SECRET']
    self.hashtags = request.json['hashtags']
    self.queryTwitter = TweetHandler(self.TWITTER_APP_KEY, self.TWITTER_APP_KEY_SECRET,self.TWITTER_ACCESS_TOKEN, self.TWITTER_ACCESS_TOKEN_SECRET)
    self.response = []
    for tag in self.hashtags:
      self.dict = {tag:[]}
      for item in self.queryTwitter.GetTweetsByHashtag(tag):
        self.dict[tag].append(item)
      self.response.append(self.dict)
    return self.response

class GetByTagLocationLang(Resource):
  def get(self):
    self.query = DbHandler()
    return self.query.GetByTagLocationLang()


class GetByDayHour(Resource):
  def get(self):
    self.query = DbHandler()
    return self.query.GetByDayHour()


api.add_resource(V1, '/v1')
api.add_resource(GetTweet, '/v1/tweets')
api.add_resource(GetByTagLocationLang, '/v1/tweets/bytaglocationlang')
api.add_resource(GetByDayHour, '/v1/tweets/bydayhour')


apiRoutes = [{
              'path': '/v1/tweets',
              'title': 'Pega Amostra,salva e mostra Top5',
              'desc': 'Obtém Amostra de 100 Tweets por Hashtag, grava no MongoDb e mostra o top 5 por Hashtag'
            },{
              'path': '/v1/tweets/bytaglocationlang',
              'title': 'Agrupa todas as amostras por Tag, local e lingua',
              'desc': 'Recupera do banco de dados o total de tweets agrupados por Hashtag, localizaçao e Linguagem'
            },{
              'path': '/v1/tweets/bydayhour',
              'title': 'Agrupa todas as amostras por Hora do dia',
              'desc': 'Recupera do banco de dados o total de tweets, agrupados por hora do dia'
            }]




@app.route('/')
def Index():
  return render_template('index.htm', title='Home', apiroutes=apiRoutes)

@app.route('/help')
def Help():
    return render_template('help.htm', title='Help Page')

@app.route('/credentials', methods=['GET', 'POST'])
def credentials():
  form = CredentialsForm()
  if form.validate_on_submit():
    global TWITTER_ACCESS_TOKEN_SECRET
    global TWITTER_ACCESS_TOKEN
    global TWITTER_APP_KEY
    global TWITTER_APP_KEY_SECRET
    global hashtags
    TWITTER_APP_KEY = form.TWITTER_APP_KEY.data
    TWITTER_APP_KEY_SECRET = form.TWITTER_APP_KEY_SECRET.data
    TWITTER_ACCESS_TOKEN = form.TWITTER_ACCESS_TOKEN.data
    TWITTER_ACCESS_TOKEN_SECRET = form.TWITTER_ACCESS_TOKEN_SECRET.data
    hashtags = form.HASHTAGS.data.split(" ")
    flash(f'Credenciais registradas!{ TWITTER_APP_KEY }', 'success')
    return redirect(url_for('Index'))
  return render_template('credentials.htm', title='Registrar Credenciais', form=form)

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')

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

""" {
"TWITTER_APP_KEY": "YezipOoweQ3FbSgyRihKZ5BbZ",
"TWITTER_APP_KEY_SECRET": "tWRn9kkswLkxbXK78aOuHbxvb7C1BG3SFZDfxVDHgIdLqkFkTy",
"TWITTER_ACCESS_TOKEN": "1237878615942946818-BY4593QtzNK0Ryig8Jh203c8Stq7DO",
"TWITTER_ACCESS_TOKEN_SECRET": "gjlTPvFbNlGYnGh7011lgyjf8oiWOASSmp244Kce1KZ6S",
"hashtags": ["#swagger", "#devops"]
} """