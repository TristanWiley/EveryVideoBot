import requests, tweepy

def login_to_twitter(consumer_key, consumer_secret, access_token, access_token_secret):

    auth = tweepy.OAuthHandler(consumer_key,  consumer_secret)
    auth.set_access_token(access_token,       access_token_secret)

    api = tweepy.API(auth)
    ret = {}
    ret['api'] = api
    ret['auth'] = auth
    return api

def post_video():

    consumer_key = ''
    consumer_secret = ''
    access_token = ''
    access_token_secret =  ''

    message = get_video_url()

    api = login_to_twitter(consumer_key, consumer_secret, access_token, access_token_secret )

    ret = api.update_status(status=message)

def get_video_url():
    r = requests.get(url='https://randomyoutube.net/api/getvid?api_token=')
    video_link = "https://www.youtube.com/watch?v=" + r.json()['vid']
    return video_link

post_video()
