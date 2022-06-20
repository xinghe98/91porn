import random


def random_ip():
    m = random.randint(0, 255)
    n = random.randint(0, 255)
    x = random.randint(0, 255)
    y = random.randint(0, 255)
    ip = str(m) + '.' + str(n) + '.' + str(x) + '.' + str(y)
    return ip

print(random_ip())