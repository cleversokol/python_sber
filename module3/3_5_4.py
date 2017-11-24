#beaeuqky@sharklasers.com
import requests
import json

#client_id = 'fc84c57093be3860e483'
#client_secret = 'b91b060b34e881083eea16ba38dbdf1f'
#
## инициируем запрос на получение токена
#r = requests.post("https://api.artsy.net/api/tokens/xapp_token",
#                  data={
#                      "client_id": client_id,
#                      "client_secret": client_secret
#                  },
#                  verify=False)
#
## разбираем ответ сервера
#j = json.loads(r.text)
#
## достаем токен
#token = j["token"]
##print(token)

## создаем заголовок, содержащий наш токен
headers = {"X-Xapp-Token" : "eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJyb2xlcyI6IiIsImV4cCI6MTUxMjA1NTQ0MCwiaWF0IjoxNTExNDUwNjQwLCJhdWQiOiI1YTE2ZTgxMDljMThkYjQzYmUwMjJiN2EiLCJpc3MiOiJHcmF2aXR5IiwianRpIjoiNWExNmU4MTBiMjAyYTM0ZDgzMDc2ODJhIn0.h-bxbvu04w-WCMDy2Di_o_oyKV7kx-sAQ4eRTT8t360" }
#headers = {"X-Xapp-Token" : token }

temp = {}
result = []
with open("dataset_20668_4.txt") as file:
    for i in file:
        i = i.rstrip()
        # инициируем запрос с заголовком
        r = requests.get("https://api.artsy.net/api/artists/"+i, headers=headers, verify=False)
        # разбираем ответ сервера
        j = json.loads(r.text)
        temp.update({j["sortable_name"]:j["birthday"]})
for key in temp:
    value = temp.get(key)
    result.append((key,value))
result.sort(key=lambda elem: (elem[1], elem[0]))
print(result)
for i in result:
    print(i[0])

