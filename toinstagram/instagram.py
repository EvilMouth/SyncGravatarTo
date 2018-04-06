from product import Product
import requests
from keys.read import kv
from utils.gravatar import get_image_url
from utils.image import (
    save_image_jpg, delete_image
)
import os
from utils.cookies import load_cookies, save_cookies

__cookies_path__ = os.path.dirname(__file__) + '/sgiti.cookies'
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
        need_login = False
        cookies = load_cookies(__cookies_path__)
        if cookies:
            code = self.__upload_instagram(cookies)
            if 403 == code:
                print('cookies overdue, reconnection...')
                need_login = True
        else:
            need_login = True

        if need_login is True:
            print('connecting instagram...')
            cookies = self.__login_instagram()
            if cookies:
                self.__upload_instagram(cookies)
            else:
                print('connect to instagram fail!!!')

    def __upload_instagram(self, cookies):
        print('start sync to instagram...')
        csrftoken = cookies['csrftoken']
        session = requests.Session()
        session.headers.update({
            'origin': 'https: // www.instagram.com',
            'referer': 'https://www.instagram.com/accounts/edit/',
            'x-csrftoken': csrftoken,
            'x-instagram-ajax': '1',
            'x-requested-with': 'XMLHttpRequest'
        })
        session.cookies.update(cookies)
        image_url = get_image_url(self.get_email(), 400)
        path = save_image_jpg(image_url, 'instagram')
        files = {'profile_pic': ('profilepic.jpg', open(path, 'rb'), 'image/jpeg')}
        request = session.post(__url_sync__, files=files)
        if 200 == request.status_code and request.json()['changed_profile'] is True:
            print('sync to instagram success!!!')
            # save cookies
            cookies.update(request.cookies)
            save_cookies(cookies, __cookies_path__)
        elif 403 == request.status_code:
            return 403
        else:
            print('sync to instagram fail!!! because. %s' % request.json()['message'])
        delete_image(path)

    def __login_instagram(self):
        # init to get csrftoken
        request = requests.get(__url_init__)
        cookies = request.cookies
        # login to get new cookies
        csrftoken = cookies['csrftoken']
        session = requests.Session()
        session.headers.update({
            'origin': 'https: // www.instagram.com',
            'referer': 'https://www.instagram.com/',
            'x-csrftoken': csrftoken,
            'x-instagram-ajax': '1',
            'x-requested-with': 'XMLHttpRequest'
        })
        session.cookies.update(cookies)
        data = {
            'username': self.username,
            'password': self.password
        }
        request = session.post(__url_login__, data=data)
        if 200 == request.status_code and request.json()['authenticated'] is True:
            return request.cookies


if __name__ == '__main__':
    instagram = Instagram()
    instagram.sync()
