import requests
from pprint import pprint

sahifa = "https://kun.uz/news/main"
r=requests.get(sahifa)
pprint(r.text)