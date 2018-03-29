from twitter.twitter import Twitter
from telegram.telegram import Telegram

twitter = Twitter()
twitter.sync()

print('--------------------------------------------------')

telegram = Telegram()
telegram.sync()
