from twitter.twitter import Twitter
from telegram.telegram import Telegram
from v2ex.v2ex import V2EX


def sync():
    twitter = Twitter()
    twitter.sync()

    print('--------------------------------------------------')

    telegram = Telegram()
    telegram.sync()

    print('--------------------------------------------------')

    v2ex = V2EX()
    v2ex.sync()


if __name__ == '__main__':
    sync()
