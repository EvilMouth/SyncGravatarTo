from product import Product
import requests
from keys.read import kv
from utils.gravatar import get_image_url
from utils.image import (
    save_image, delete_image
)

url = 'https://www.v2ex.com/settings/avatar'


class V2EX(Product):
    def __init__(self):
        super().__init__('v2ex')
        self.a2 = self.get_self_property('a2', kv['v2ex_a2'])

    def sync(self):
        if self.is_enable():
            self.__sync()

    def __sync(self):
        print('start sync to v2ex...')
        image_url = get_image_url(self.get_email(), 400)
        path = save_image(image_url, 'v2ex')
        files = {'avatar': open(path, 'rb')}
        request = requests.post(url, files=files, cookies={'A2': self.a2})
        if '当前头像' in request.text:
            print('sync to v2ex success!!!')
        else:
            print('sync to v2ex fail!!!')
        delete_image(path)
