import requests
import sys
base_url = "http://subeen.com/download/"
url = base_url + "process.php"
data_info ={"name": "khaled","email":"kmahmud101@gmail.com","country":"Bangladesh"}
r = requests.post(url,data = data_info)
if r.ok is False:
    sys.exit("Download file error")
with open("book.pdf","wb") as f:
    f.write(r.content)
print("successfully download")