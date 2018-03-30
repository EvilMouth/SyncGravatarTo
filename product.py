import os
import json
import abc

with open(os.path.dirname(__file__) + '/property.json') as j:
    _property = json.load(j)


class Product:
    def __init__(self, name):
        self.name = name

    def get_self_property(self, key, default_value):
        try:
            value = _property[self.name][key]
            if not value:
                value = default_value
            return value
        except KeyError:
            return default_value

    def get_email(self):
        try:
            email = _property[self.name]['email']
        except KeyError:
            email = _property['mainEmail']
        if not email:
            raise RuntimeError("email must not be null")
        return email

    @abc.abstractmethod
    def sync(self):
        """Method that should do something."""


if __name__ == '__main__':
    t = Product('twitter')
    print(t.get_email())
