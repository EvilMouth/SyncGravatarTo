from utils.gravatar import get_image_url
from utils.image import save_image
from utils.image import delete_image
from twitter.twitter import post

email = input('input your gravatar email:')
while not email:
    print('fuck you email must not be empty')
    email = input('input your gravatar email:')

print('------start get your image_url------')
image_url = get_image_url(email, 400)

order = input('check your image_url %s (y/n):' % image_url)
if order == 'n':
    print('stop sync by user')
    exit()

print('------stare download image------')
path = save_image(image_url)

print('start sync...')
code = post(path)

if code == 200:
    print('sync success!!!')
else:
    print('sync fail!!!')

delete_image(path)
