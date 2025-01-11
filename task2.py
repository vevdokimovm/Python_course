objects = [1, 2, 1, 5, True, False, True, 'false', [], [1,2], [1,2]] 
# Right answer – 8 {1, 2, 5, True, False, 'false', [], [1, 2]}

res = 0
flag = False

for i in range(len(objects)):
    flag = False
    for j in range(i + 1, len(objects)):
        if objects[i] is objects[j]:
            flag = True
        if type(objects[i]) in [type([])] and objects[i] == objects[j]:
            flag = True
    if not flag:
        res += 1
        print(objects[i])
        
print(res)

