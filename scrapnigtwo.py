import re
import requests
import sys
url="http://books.toscrape.com/catalogue/category/books/mystery_3/index.html"
response = requests.get(url)
text = response.text
text = text.replace("\n"," ")
book_pat = re.compile(r'<h3><a href="(.*?)" title="(.*?)">')
result = re.findall(book_pat,text)
print(len(result))
print(result[0])
print(result[1])
next_page = re.findall(r'<li class="next"><a href="(.*?)">next</a></li>',text)
print(next_page[0])

i = url.rfind("/")
print(i)
print(url[0:i+1])
url = url[0:i+1] + next_page[0]
print(url)