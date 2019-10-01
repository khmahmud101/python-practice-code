import requests
import sys
img_url = sys.argv[1]
img_file = sys.argv[2]
response = requests.get(img_url)
with open("img2.png","wb") as f:
    f.write(response.content)