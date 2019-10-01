import requests
import sys
base_url = "http://subeen.com/download/"
info_dt ={"name":"Mahmud","email":"kmahmud1991@gmail.com","country":"Bangladesh"}
url = base_url + "process.php"
response = requests.post(url,data=info_dt)
if response.ok is False:
    sys.exit("Download Error")
with open("cpbook2.pdf","wb") as fp:
    fp.write(response.content)
print("Download complete")