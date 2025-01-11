s = input()
t = input()

counter = 0
pos = 0
while s.find(t, pos) != -1 and pos < len(s):
    pos = s.find(t, pos) + 1
    counter += 1
    
print(counter)