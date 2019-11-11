import requests
import os
import webbrowser as wb
url = "http://subeen.com/allposts/"
response = requests.get(url)
text = response.text

#print(text)
with open("subeen.html","w", encoding=response.encoding) as f:
    f.write(text)
file_path = os.path.realpath("subeen.html")
print(file_path)
wb.open("file://"+file_path)
