s = input() # Base string
a = input() # Find this pattern a
b = input() # and replace it with b

counter = 0
if a == b and s.find(a) == -1:
    counter = 0
elif a in b:
    counter = "Impossible"
else:
    for i in range(1, 1000):
        if s.replace(a, b) == s:
            break
        else:
            s = s.replace(a, b)
            counter += 1

print(counter)