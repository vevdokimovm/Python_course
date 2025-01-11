def find_all_children(parent):
    global all_children
    all_children += children[parent]
    
    for child in children[parent]:
        if child != parent:
            find_all_children(child)
    
    
    


n = int(input())

children = {}

for _ in range(n):
    args = input().split()
    child = args[0]
    if child not in children.keys():
        children[child] = [child]
    
    for i in range(2, len(args)):
        parent = args[i]
        if parent not in children.keys():
            children[parent] = [parent]
        children[parent].append(child)
    
    
# print(children)
q = int(input())

for _ in range(q):
    is_parent, is_child = input().split()
    
    all_children = []
    find_all_children(is_parent)
    
    if is_child in all_children:
        print("Yes")
    else:
        print("No")

    
    
    
    