import re
import sys
import requests

A = input()
B = input()

patternURL = re.compile(r'https?://\w*')
#patternB = re.compile(r'')

res = requests.get(A)
A = res.text
print("A = ", A)

possible = False

for line in A:
    C = re.search(patternURL, line)
    if C != None:
        res = requests.get(C)
        print("C status_code = ", res.status_code)
        if res.status_code == 200:
            C = res.text
            print("C = ", C)
            for lineC in C:
                if re.match(B, lineC):
                    possible = True

print("Yes") if possible else print("No")
