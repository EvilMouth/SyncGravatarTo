from keys.read import kv
import socks
from telethon import TelegramClient
from telethon.tl.functions.photos import UploadProfilePhotoRequest
from product import Product
from utils.gravatar import get_image_url
from utils.image import (
    save_image, delete_image
)
import os


class Telegram(Product):
    def __init__(self):
        super().__init__('telegram')
        self.api_id = self.get_self_property('api_id', kv['telegram_api_id'])
        self.api_hash = self.get_self_property('api_hash', kv['telegram_api_hash'])

    def sync(self):
        print('connecting telegram...')
        session_path = os.path.dirname(__file__) + '/sgitt.session'
        client = TelegramClient(session_path, self.api_id, self.api_hash,
                                proxy=(socks.SOCKS5, 'localhost', 1086))
        client.start()
        print('start sync to telegram...')
        image_url = get_image_url(self.get_email(), 400)
        path = save_image(image_url, 'telegram')
        input_file = client.upload_file(path)
        result = client(UploadProfilePhotoRequest(input_file))
        if result:
            print('sync to telegram success!!!')
        else:
            print('sync to telegram fail!!!')
        delete_image(path)


if __name__ == '__main__':
    telegram = Telegram()
    telegram.sync()
