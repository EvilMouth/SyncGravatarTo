from product import Product
import requests
from keys.read import kv
from utils.gravatar import get_image_url
from utils.image import (
    save_image_jpg, delete_image
)

__url_init__ = 'https://www.instagram.com/'
__url_login__ = 'https://www.instagram.com/accounts/login/ajax/'
__url_sync__ = 'https://www.instagram.com/accounts/web_change_profile_picture/'


class Instagram(Product):
    def __init__(self):
        super().__init__('instagram')
        self.username = self.get_self_property('username', kv['instagram_username'])
        self.password = self.get_self_property('password', kv['instagram_password'])

    def sync(self):
        if self.is_enable():
            self.__sync()

    def __sync(self):
        print('connecting instagram...')
        request = requests.get(__url_init__)
        csrftoken = request.cookies['csrftoken']
        session = requests.Session()
        session.headers.update({
            'origin': 'https: // www.instagram.com',
            'referer': 'https://www.instagram.com/',
            'x-csrftoken': csrftoken,
            'x-instagram-ajax': '1',
            'x-requested-with': 'XMLHttpRequest'
        })
        session.cookies.update({
            'csrftoken': csrftoken
        })
        data = {
            'username': self.username,
            'password': self.password
        }
        request = session.post(__url_login__, data=data)
        if 200 == request.status_code and request.json()['authenticated'] is True:
            print('start sync to instagram...')
            csrftoken = request.cookies['csrftoken']
            ds_user_id = request.cookies['ds_user_id']
            sessionid = request.cookies['sessionid']
            session.headers.update({
                'referer': 'https://www.instagram.com/accounts/edit/',
                'x-csrftoken': csrftoken,
            })
            session.cookies.update({
                'csrftoken': csrftoken,
                'ds_user_id': ds_user_id,
                'sessionid': sessionid
            })
            image_url = get_image_url(self.get_email(), 400)
            path = save_image_jpg(image_url, 'instagram')
            files = {'profile_pic': ('profilepic.jpg', open(path, 'rb'), 'image/jpeg')}
            request = session.post(__url_sync__, files=files)
            if 200 == request.status_code and request.json()['changed_profile'] is True:
                print('sync to instagram success!!!')
            else:
                print('sync to instagram fail!!! because. %s' % request.json()['message'])
            delete_image(path)
        else:
            print('connect to instagram fail!!!')


if __name__ == '__main__':
    instagram = Instagram()
    instagram.sync()
