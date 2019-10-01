import requests
import webbrowser as wb
import os
url = "http://subeen.com/allposts"
response = requests.get(url)
print(response.ok)
print(response.reason)
print(response.status_code)
print(response.text)
with open("code.txt","w") as f:
    f.write("This is new file")

url = "http://dimikcomputing.com"
response = requests.get(url)

with open("dimik.html","w",encoding=response.encoding) as f:
    f.write(response.text)
path = os.path.realpath("dimik.html")
print(path)
wb.open("file://" + path)