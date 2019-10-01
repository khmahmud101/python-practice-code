import re

s= "Afganistan, America, Bangladesh, Cananda, Denmark, England, Greenland, Iceland, Netherlands, New Zealand, Sweden, Switzerland"
#countries = s.split(",")
#print(countries)
#li = [item for item in countries if item.endswith("land") or item.endswith("lands")]
#print(li)

s="Bangladesh is our homeland"
#result = re.search("Bangla","bangladesh")
#print(result is None)
st="Bangladesh"
result=re.search(".",st)
print(result.group())
result=re.search("B.n",st)
print(result.group())
result=re.search("B.n...",st)
print(result.group())
result=re.search(".................",s)
print(result.group())

result=re.search("o\w\w",s)
print(result.group())
result=re.search("i\w\w",s)
print(result)

result=re.search("B\w+h",s)
print(result.group())

result=re.search("B.+h",s)
print(result.group())

result=re.search("B.+?h",s)
print(result.group())

text= "phone number: 01711101001"
match= re.search('\d+',text)
print(match.group())

text= "house number 5: phone number: 01711101001"
match= re.search('\d+',text)
print(match.group())


match= re.search('\d{11}',text)
print(match.group())

text= "house number 5: phone number: 017 11101001"
match= re.search('\d{3}\s*\d{8}',text)
print(match.group())

text= "house number 5: phone number: 017 11101001, 016 11101002, 017 11101001, 00000000000"
match= re.findall(r'\d{3}\s*\d{8}',text)
print(match)

text= "house number 5: phone number: 017 11101001, 016 11101002, 017 11101001, 00000000000"
match= re.findall(r'01[3456789]\s*\d{8}',text)
print(match)
with open("file.txt","r") as f:
    text = f.read()
match = re.findall(r'^.+?$',text,re.MULTILINE)
print(match)

name = "<li>Tamim</li><li>Shakib</li><li>Mahmudullah</li><li>Mominul</li>"
result = re.findall(r'<li>(.+?)</li>',name)
print(result)

# REGEX COMPILE
text = "This is line 1.Date is 2017/06/01. And there is another date:2017-07-01. The Third and final darw is 2017/08/30"
com = re.compile(r'(\d{4})[-/](\d{2})[-/](\d{2})')
result=com.findall(text)
print(result)
text2="new date: 2017/06/15"
result=com.findall(text2)
print(result)

s= "Abcd 1234 - 33"
result= re.sub(r'\d','0',s)
print(result)
s="22/07/2017, 20/01/2017, 01/01/2018"
new_s = re.sub(r'(\d{2})/(\d{2})/(\d{4})',r'\3-\2-\2',s)
print(new_s)
text = "Email your feedback here: book at subeen.com, py.book (at) subeen dot com, book [at] subeen [dot] com "
text=re.sub(r'\s+')






