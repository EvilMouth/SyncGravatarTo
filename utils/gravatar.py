from libgravatar import Gravatar


def get_image_url(email, size=0):
    g = Gravatar(email)
    url = g.get_image()
    if size > 0:
        url += "?s=%s" % size
    return url
