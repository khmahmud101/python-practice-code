import re
import requests
import sys
url = "http://dimik.pub"
response = requests.get(url)
if response.ok is False:
    sys.exit("could not get response from server")

page_content = response.text
regexp = re.compile(r'<div class="book-cover">\s*<a href="(.*?)>\s*<img src="(.*?)".*?<h2 class="sd-title"><.*?>(.*?)<',re.S)
result = re.findall(regexp,page_content)

for item in result:
    print("Name:",item[2])
    print("URL:", item[0])
    print("Image:", item[1])

s="http://dimik.pub/book/30/programming-career-guideline-by-tamim-shahriar"
regex = re.compile(r'book/(\d+)/(\w+)-(\w+)-')
result = re.findall(regex,s)
print(result[0])
li = list(result[0])
print(li)
dir_name="_".join(li)
print(dir_name)
