import sys
import re

ans = []

for line in sys.stdin:
    line = line.rstrip()
    pos = 0
    cnt = 0
    while True:
        if line.find("cat", pos) != -1:
            pos = line.find("cat", pos) + len("cat")
            cnt += 1
        else:
            break
            
        if cnt == 2:
            break
            
    if cnt == 2:
        ans.append(line)
        
for line in ans:
    print(line)