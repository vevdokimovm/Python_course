with open("dataset_24465_4.txt") as f, open("answer.txt", "w") as w:
    f_lines = []
    for line in f:
        f_lines.append(line)
        
    while len(f_lines) != 0:
        w.write(f_lines.pop())