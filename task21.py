import re
import requests

url = input()
response = requests.get(url)
html = response.text
pattern = r'<a\s+[^>]*?href=["\'](.*?)["\'][^>]*?>'
links = re.findall(pattern, html)

chars = [':', '/']
ans = []
for url in links:
    domen = ""
    pos = url.find('//')
    pos = 0 if pos == -1 else pos + 2
    while pos < len(url) and url[pos] not in chars:
        domen += url[pos]
        pos += 1
        
    if domen not in ans and domen[0] != '.':
        ans.append(domen)
        
ans.sort()
for line in ans:
    print(line)
        
