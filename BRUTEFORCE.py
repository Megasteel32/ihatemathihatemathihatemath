limit = 10**100
da_numba = 1
while da_numba <= limit:
    seed = da_numba
    print(seed)
    while seed != 1:
        if (seed % 2) == 0:
            seed /= 2
        else:
            seed = (3 * seed) + 1
    da_numba += 1