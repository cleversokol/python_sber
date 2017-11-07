import re
import sys
import requests

#A = input()
#B = input()

A = "https://stepic.org/media/attachments/lesson/24472/sample0.html"
B = "https://stepic.org/media/attachments/lesson/24472/sample2.html"

#regex = r'<a href=""[\w\?\&=]*"">'
#regex = r'<a href=\"\S*\">'
regex = r'\S*'
patternURL = re.compile(regex)
#patternURL = re.compile(r'<a href=https?://\w*')
#patternB = re.compile(r'')

res = requests.get(A, verify=False)
A = res.text
print("A = ", A)

possible = False

for line in A:
    C = re.search(patternURL, line)
    print("search result = ", C)
    if C != None:
        res = requests.get(C, verify=False)
        print("C status_code = ", res.status_code)
        if res.status_code == 200:
            C = res.text
            print("C = ", C)
            for lineC in C:
                if re.match(B, lineC):
                    possible = True

print("Yes") if possible else print("No")
