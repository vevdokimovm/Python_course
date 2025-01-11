def closest_mod_5(a):
    a += (5 - (a % 5)) % 5
    return a