import re

#s= "Afganistan, America, Bangladesh, Cananda, Denmark, England, Greenland, Iceland, Netherlands, New Zealand, Sweden, Switzerland"
#li = re.findall(r'(\w+lands*)', s)
#print(li)

#match = re.search('Bangla', 'Bangladesh')
#print(match)
#print(match.group())

#match = re.search('desh','Bangladesh')
#print(match.group())

#match = re.search('dets','Bangladesh')

#print(match is None)


#match = re.search('.',s)
#print(match.group())
#match = re.search('B.n...',s)
#print(match.group())
#match = re.search('B.n.........',s)
#print(match.group())

#match = re.search('o\w\w', s)
#print(match.group())

#match = re.search('i\w\w', s)
#print(match)


#match = re.search('B\w+h',s)
#print(match.group())


#match = re.search('B.+h',s)
#print(match.group())

#match = re.search('B\w+?h',s)
#print(match.group())

#text= "house 5 phone number: 01620663567"

#match = re.search('\d{11}',text)  #if we use \d it return 5 but we search phone number thats why we write \d{11} why 11 bcz our phone number is 11 digit
#print(match.group())


#text= "house 5 phone number: 016 20663567"

#match = re.search('\d{11}',text)
#print(match.group())

#text= "house 5 phone number: 016 20663567" #\s+ means have to one or more space, \s* 0 or more space, \s? only one not more

#match = re.search('\d{3}\s*\d{8}',text)
#print(match.group())

#text= "house 5 phone number: 01620663567, 01782222222, 017 82222228,00000000000"
#match = re.findall(r'\d{3}\s*\d{8}',text)
#print(match)

#text= "house 5 phone number: 01620663567, 01782222222, 017 82222228,00000000000"
#match = re.findall(r'01[56789]\s*\d{8}',text)
#print(match)
#with open("file", "r") as f:
    #text =f.read()

#txt=  re.findall(r'^.*?$',text,re.M) #use re.M bcz our string have new line
#print(txt)

#name = "<li>Tamim</li><li>Shakib</li><li>Mahmudullah</li><li>Mominul</li>"
#result = re.findall(r'<li>(.*?)</li>',name)
#print(result)
#text = "This is line 1.Date is 2017/06/01. And there is another date:2017-07-01. The Third and final darw is 2017/08/30"
#pat = re.compile(r'(\d{4})[-/](\d{2})[-/](\d{2})')
#result = pat.findall(text)
#print(result)
#print(type(pat))



#with open("test.html","r") as f:
    #text = f.read()

#result = re.findall(r'(\w.*)',text)
#print(result)
s = "Email your feedback here: book at subeen.com, py.book (at) subeen dot com, book [at] subeen [dot] com "
text = re.sub(r'\s+[\(\[]*\s*at\s*[\)\]]*\s+','@',s, flags= re.I)
print(text)

