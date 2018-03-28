import requests
from requests_oauthlib import OAuth1
from keys.read import kv

# url
url = "https://api.twitter.com/1.1/account/update_profile_image.json"

# oauth1
auth = OAuth1(kv['consumer_key'], kv['consumer_secret'], kv['token_key'], kv['token_secret'])


def post(path):
    files = {'image': open(path, 'rb')}
    request = requests.post(url, auth=auth, files=files)
    return request.status_code


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
