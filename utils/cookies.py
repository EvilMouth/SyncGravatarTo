import pickle


def save_cookies(cookiejar, filepath):
    with open(filepath, 'wb') as f:
        pickle.dump(cookiejar, f)


def load_cookies(filepath):
    try:
        with open(filepath, 'rb') as f:
            return pickle.load(f)
    except FileNotFoundError:
        print('No such file or directory to load cookies: %s' % filepath)
