import requests
url = "http://subeen.com/allposts/"
response = requests.get(url)
text = response.text

print(text)
print(dir(response))


print(response.ok)
print(response.status_code)
print(response.reason)