import numpy.random as random

def seed_gen():
    random.default_rng()
    seed = random.randint(429496729)
    seed *= random.randint(429496729)
    seed *= random.randint(429496729)
    seed *= random.randint(429496729)
    seed *= random.randint(429496729)
    seed *= random.randint(429496729)
    return seed

def collatz_time(seed):
    print(seed)
    while seed != 1:
        if (seed % 2) == 0:
            seed /= 2
            print(seed)
        else:
            seed = (3 * seed) + 1
            print(seed)
    print("Done!")

while 1 == 1:
    collatz_time(seed_gen())
