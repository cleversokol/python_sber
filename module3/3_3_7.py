import re
import sys
import requests

text = "<a href=\"http://stepic.org/courses\"><a href=\'https://stepic.org\'><a href=\'http://neerc.ifmo.ru:1345\'><a href=\"ftp://mail.ru/distib\" ><a href=\"ya.ru\"><a href=\"www.ya.ru\"><a href=\"../skip_relative_links\">"
#text = "<a href=\"http://stepic.org/courses\">"
#text = "<a href='https://stepic.org'>"
#text = <a href='http://neerc.ifmo.ru:1345'>
#text = <a href="ftp://mail.ru/distib" >
#text = <a href="ya.ru">
#text = <a href="www.ya.ru">
#text = <a href="../skip_relative_links">
#print(text)
#link = input()
#file = requests.get(link).text

#regex = r'<a[^>]+href=[\'"][\w:/]*[\.]*([^/: >]*)[^>]*[\'"]>'
#regex = r'<a[^>]+href=[\'"]((https?|ftp)://)*([^\.]+[^/: >]*)[^>]*[\'"] *>'
#regex = r'<a[^>]+href=[\'"]((https?|ftp)://)?([^\.]+[^/: >]*)[^>\'"]*[\'"][^>]*>'
regex = r'<a[^>]+href=[\'"]((https?|ftp)://)?([^\.]+[^/: <>\'"]*)[^>\'"]*[\'"][^>]*>'
pattern = re.compile(regex)

matches = re.findall(pattern, text)
#print(matches)
temp = [elem[2] for elem in matches]
result = set(temp)
#result = set(matches)
#for i in matches:
#    result.add(i[2])

for i in sorted(result):
    print(i)


## Final answer:
#import re
#import sys
#import requests
#
#link = input()
#file = requests.get(link).text
#
#regex = r'<a[^>]+href=[\'"]((https?|ftp)://)?([^\.]+[^/: <>\'"]*)[^>\'"]*[\'"][^>]*>'
#pattern = re.compile(regex)
#matches = re.findall(pattern, file)
#temp = [elem[2] for elem in matches]
#result = set(temp)
#for i in sorted(result):
#    print(i)
