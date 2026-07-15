import requests

url = "https://app.rockgympro.com/b/widget/"

params = {
    "a" : "fcfeed",
    "widget_guid" : "980235b6ef094cd38a1356a41a60ef2c",
    "mode" : "e",
    "start" : "1785045600",
    "end": "1788674400",
}

r = requests.get(url=url, params=params, timeout=10)

print(r.url)
print(r.status_code)
print(r.json())
