import requests
from requests_oauthlib import OAuth1
from utils.property import read

# url
url = "https://api.twitter.com/1.1/account/update_profile_image.json"

# key
kv = read('twitter/key.property')
auth = OAuth1(kv['consumer_key'], kv['consumer_secret'], kv['token_key'], kv['token_secret'])


def post(path):
    files = {'image': open(path, 'rb')}
    request = requests.post(url, auth=auth, files=files)
    return request.status_code
