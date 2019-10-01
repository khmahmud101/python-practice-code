import re
import requests
import sys
url="http://books.toscrape.com/index.html"
response = requests.get(url)
text = response.text
if response.ok is False:
   sys.exit("server hot found")
print(len(text))
result= re.findall(r'<div class="side_categories">(.*?)</div>',text,re.M | re.DOTALL)
print(len(result))


category_pat = re.compile(r'<li>\s*<a href="(.*?)">(.*?)<',re.M | re.DOTALL)
category_pat = re.compile(r'<li>\s*<a href="(.*?)">\s*(\w+[\s\w]+\w)\s*?<',re.M | re.DOTALL)
result = re.findall(category_pat,text)
for item in result:
   print(item)



