import re
import requests
import sys
url="http://books.toscrape.com"
response = requests.get(url)
text = response.text
text = text.replace("\n"," ")
single_pat = re.findall(r'<div class="item-active"><img src="(.*?)" alt="The Exiled"/></div>',text)
print(single_pat)