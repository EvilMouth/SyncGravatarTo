import requests
import os


def save_image(url, suffix='sgt'):
    file = 'temp_%s.png' % suffix
    r = requests.get(url, stream=True)
    with open(file, 'wb') as fd:
        for chunk in r.iter_content():
            fd.write(chunk)
    return os.path.abspath(file)


def delete_image(path):
    os.remove(path)
