import os

separator = "="
kv = {}

with open(os.path.dirname(__file__) + '/key.property') as f:
    for line in f:
        if separator in line:
            name, value = line.split(separator, 1)
            kv[name.strip()] = value.strip()

if __name__ == '__main__':
    print(kv)
