import os
import re

answer = []
f = open("main_ans.txt", "w")

for current_dir, dirs, files in os.walk("main/"):
    print("current_dir = ", current_dir)
    print("dirs = ", dirs)
    print("files = ", files)
    
    pattern = r".*\.py$"
    for file in files:
        print("** file = ", file)
        if re.match(pattern, file):
            answer.append(current_dir)
            break
        
answer.sort()
print("answer = ", answer)

for ans in answer:
    f.write(ans)
    f.write('\n')
    
f.close()

