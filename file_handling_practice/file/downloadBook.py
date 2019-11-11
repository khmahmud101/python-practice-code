import requests
import sys

base_url = "https://subeen.com/download/"
info_dt = {"name":"khaled", "email":"kmahmud101@gmail.com","country":"Bangladesh"}

url = base_url + "process.php"
response = requests.post(url, data=info_dt)

if response.ok is False:
    sys.exit("Error downloading the file")

with open("cpbook.pdf","wb") as fp:
    fp.write(response.content)

print("Book Download complete!")