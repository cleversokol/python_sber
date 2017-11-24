import requests

url_1 = "http://numbersapi.com/"
url_2 = "/math"

params = {
    'json': 'true'
}

#res = requests.get(api_url, params=params)
#print(res.status)
#print(res.headers["Content-Type"])
#data = res.json()
#print(data["main"]["temp"])

with open("dataset_20668_3.txt") as file:
    for i in file:
        #print("url = ", url_1+i[:-1]+url_2)
        res = requests.get(url_1+i.rstrip()+url_2, params=params)
        #print("res.text = ", res.text)
        data = res.json()
        #print("data.found", data["found"])
        if data["found"]:
            print("Interesting")
        else:
            print("Boring")
