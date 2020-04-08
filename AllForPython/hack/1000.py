import requests
import re

flag = True
pattern = r'href=(.+?)\s'
url1 = 'https://click1000.training.hackerdom.ru/'
u_get = requests.get(url1+'start')
i = 1

while flag and u_get.status_code == 200:
    for href1 in re.findall(pattern, u_get.text):
        u_get = requests.get(url1+href1)
        print(url1+href1)
        print(i)
        i += 1
        if not u_get:
            flag = False
