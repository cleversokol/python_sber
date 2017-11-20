import re
import sys
import requests

link = input()
file = requests.get(link).text

regex = r'<a href=[\"\']\S*[\"\']>'
pattern = re.compile(regex)

matches = re.findall(patternURL, A)
result = set(matches)
for i in sorted(result):
    print(i)
