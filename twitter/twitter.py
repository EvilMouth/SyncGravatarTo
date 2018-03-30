from product import Product
import requests
from requests_oauthlib import OAuth1
from keys.read import kv
from utils.gravatar import get_image_url
from utils.image import (
    save_image, delete_image
)

# url
url = "https://api.twitter.com/1.1/account/update_profile_image.json"


class Twitter(Product):
    def __init__(self):
        super().__init__('twitter')
        consumer_key = self.get_self_property('consumer_key', kv['twitter_consumer_key'])
        consumer_secret = self.get_self_property('consumer_secret', kv['twitter_consumer_secret'])
        token_key = self.get_self_property('token_key', kv['twitter_token_key'])
        token_secret = self.get_self_property('token_secret', kv['twitter_token_secret'])
        self.auth = OAuth1(consumer_key, consumer_secret, token_key, token_secret)

    def sync(self):
        print('start sync to twitter...')
        image_url = get_image_url(self.get_email(), 400)
        path = save_image(image_url, 'twitter')
        files = {'image': open(path, 'rb')}
        request = requests.post(url, auth=self.auth, files=files)
        if 200 == request.status_code:
            print('sync to twitter success!!!')
        else:
            print('sync to twitter fail!!!')
        delete_image(path)

# if __name__ == '__main__':
#     r = requests.post("https://api.twitter.com/oauth/request_token", auth=auth)
#     print(r.text)
#
#     ot, ots, occ = r.text.split('&')
#     ty, tv = ot.split('=')
#     sy, sv = ots.split('=')
#     auth = OAuth1(kv['consumer_key'], kv['consumer_secret'], tv, sv)
#
#     r = requests.get("https://api.twitter.com/oauth/authenticate", auth=auth,
#                      params={'oauth_token': tv})
#     print(r.text)
