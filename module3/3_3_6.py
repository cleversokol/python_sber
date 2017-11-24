import re
import sys
import requests

A = input()
B = input()

#A = "https://stepic.org/media/attachments/lesson/24472/sample0.html"
#B = "https://stepic.org/media/attachments/lesson/24472/sample2.html"

regex = r'<a href=\"\S*\">'
patternURL = re.compile(regex)

res = requests.get(A)
A = res.text
possible = False
matches = re.findall(patternURL, A)
for match in matches:
    match = re.search(r'"([^"]*)"', match).group(1)
    res = requests.get(match)
    if res.status_code == 200:
        C = res.text
        if re.search(B, C) != None:
            possible = True

print("Yes") if possible else print("No")
