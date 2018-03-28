separator = "="
kv = {}


def read(file):
    with open(file) as f:
        for line in f:
            if separator in line:
                name, value = line.split(separator, 1)
                kv[name.strip()] = value.strip()
    return kv
