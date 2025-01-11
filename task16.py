from functools import partial

def mod_checker(mod, ostatok=0):
    return lambda x: x % mod == ostatok


mod_3 = mod_checker(3)

print(mod_3(3)) # True
print(mod_3(4)) # False

mod_3_1 = mod_checker(3, 1)
print(mod_3_1(4)) # True