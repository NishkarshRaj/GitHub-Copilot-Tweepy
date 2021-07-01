import tweepy
import os

class Main:
    def fetch_tweets(self):
        consumer_key = os.environ.get('API_KEY')
        consumer_secret = os.environ.get('API_SECRET')
        access_token = os.environ.get('ACCESS_TOKEN')
        access_token_secret = os.environ.get('SECRET_ACCESS_TOKEN')

        auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
        auth.set_access_token(access_token, access_token_secret)

        api = tweepy.API(auth)
        print('Successfully Authenticated')

        
        # Fetch Tweets
        public_tweets = api.search('GitHubCopilot')

        # Print Tweets
        for tweet in public_tweets:
            print(tweet.text)
            print("")
            print('##########################')
            print("")

main = Main()
main.fetch_tweets()
