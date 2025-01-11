import requests
import re
import sys

urlA = input()
urlB = input()

resA = requests.get(urlA)
resB = requests.get(urlB)
    
# <a href="copyright.html">Copyright</a>
# <a href="bugs.html">Found a bug</a>
# <a href="https://www.python.org/">Python</a>

html = resA.text.replace('stepic.org', 'stepik.org')
pattern = r'href=["\'](https?://.*?)(["\'])'
links = re.findall(pattern, html)
urls = [link[0] for link in links]

for i, link in enumerate(urls, start=1):
#     print("link = ", link)
    resC = requests.get(link)
    html = resC.text.replace('stepic.org', 'stepik.org')
    links = re.findall(pattern, html)
    urls = [link[0] for link in links]
#     print("urls = ", urls)
#     print("urlB = ", urlB)
    
    if urlB in urls:
        print("Yes")
        sys.exit()


print("No")    