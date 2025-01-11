n = int(input())
parents = {}

for _ in range(n):
    args = input().split()
    parents[args[0]] = [] if len(args) == 1 else args[2:]
    
# print(parents)

def is_parent(child, parent):
    if parent == child:
        return True
    
    for p in parents[child]:
        if is_parent(p, parent):
            return True
        
    return False

m = int(input())
errors = []
for _ in range(m):
    error = input()
    errors.append(error)
    
    for j in range(len(errors) - 2, -1, -1):
        if is_parent(error, errors[j]):
            print(errors.pop())
            break