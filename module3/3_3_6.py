import re
import sys
import requests

#A = input()
#B = input()

A = "https://stepic.org/media/attachments/lesson/24472/sample0.html"
B = "https://stepic.org/media/attachments/lesson/24472/sample2.html"

regex = r'<a href=\"\S*\">'
#regex = r'<a href=\"([^"]*)\">'
patternURL = re.compile(regex)


res = requests.get(A, verify=False)
A = res.text
print("A = ", A)

possible = False

#for line in A:
matches = re.findall(patternURL, A)
print("search result = ", matches)
#if C != None:
for match in matches:
    match = re.match(r'"([^"]*)"', match)
    match = match.group(0)
    print("match = ", match)
    res = requests.get(match, verify=False)
    print("C status_code = ", res.status_code)
    if res.status_code == 200:
        C = res.text
        print("C = ", C)
        for lineC in C:
            if re.match(B, lineC):
                possible = True

print("Yes") if possible else print("No")

#def slicer(my_str,sub):
#...   index=my_str.find(sub)
#...   if index !=-1 :
#...         return my_str[index:] 
#...   else :
#...         raise Exception('Sub string not found!')

#regex = r'<a href=""[\w\?\&=]*"">'
#regex = r'"'
#regex = r'\S*'
#patternURL = re.compile(r'<a href=https?://\w*')
#patternB = re.compile(r'')