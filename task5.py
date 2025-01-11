n = int(input())

namespaces = {
    'global': []
}

for _ in range(n):
    request = input().split()
    function = request[0]
    namespace = request[1]
    
    if function == 'create':
        parent = request[2]
        namespaces[namespace] = [parent]
        
    elif function == 'add':
        variable = request[2]
        namespaces[namespace].append(variable)
        
    elif function == 'get':
        variable = request[2]
        flag = False
        while namespace != 'global' and not flag:
            if variable in namespaces[namespace]:
                print(namespace)
                flag = True
            else:
                namespace = namespaces[namespace][0]
                
        if namespace == 'global' and not flag:
            if variable in namespaces['global']:
                print('global')
            else:
                print('None')
        
#print('\n', namespaces)