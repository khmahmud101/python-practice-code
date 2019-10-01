import requests
import os
import webbrowser as wb
import sys
url="http://subeen.com"
response = requests.get(url)
text = response.text
print(response.ok)
print(response.status_code)
print(response.reason)
fp = open("test.txt","w")
print(fp.write("this file written in python usdhgiurh"))
fp.close()
with open("test.txt","w") as f:
    f.write("hello,python\n")
with open("test.txt","a") as f:
    f.write("another hello")


url = "http://subeen.com"

response = requests.get(url)
print(response.ok)
with open("dimik.html","w", encoding=response.encoding) as f:
    f.write(response.text)

file_path = os.path.realpath("dimik.html")
#wb.open("file://" + file_path)

img_url = "https://www.facebook.com/photo.php?fbid=645805702546763&set=a.122394114887927&type=3&theater"
r = requests.get(img_url)
with open("img.png","wb") as f:
    f.write(r.content)









