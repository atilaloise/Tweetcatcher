from twython import Twython

class TweetHandler(Twython):
  def GetTweetsByHashtag(self, hashtags):    
    self.hashtags = hashtags
    for tag in self.hashtags:
      self.query = self.search(q='{}'.format(tag), result_type='recent', count=100)
      self.statuses = self.query['statuses']
    for tweet in self.statuses:
      print(tweet['id_str'], '\n', tweet['text'], '\n\n\n')

""" 
Exemplo de uso


from api.libs.handler.get_tweets import TweetHandler

TWITTER_APP_KEY = 'YezipOoweQ3FbSgyRihKZ5BbZ'  #supply the appropriate value
TWITTER_APP_KEY_SECRET = 'tWRn9kkswLkxbXK78aOuHbxvb7C1BG3SFZDfxVDHgIdLqkFkTy' 
TWITTER_ACCESS_TOKEN = '1237878615942946818-BY4593QtzNK0Ryig8Jh203c8Stq7DO'
TWITTER_ACCESS_TOKEN_SECRET = 'gjlTPvFbNlGYnGh7011lgyjf8oiWOASSmp244Kce1KZ6S'

hashtags = ["#devops"]

apiConnection = TweetHandler(TWITTER_APP_KEY, TWITTER_APP_KEY_SECRET, TWITTER_ACCESS_TOKEN, TWITTER_ACCESS_TOKEN_SECRET)

search = apiConnection.GetTweetsByHashtag(hashtags)
print(apiConnection.GetTweetsByHashtag.__self__.statuses)
print(apiConnection.GetTweetsByHashtag.__self__.query)
 """