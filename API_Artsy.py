import sys

import requests
import json

client_id = 'bb0ff95db4008bd97374'
client_secret = 'cb9e2d93a4cfa4313e6c7127cf34a2ea'

r = requests.post("https://api.artsy.net/api/tokens/xapp_token",
                  data={
                      "client_id": client_id,
                      "client_secret": client_secret
                  })

j = json.loads(r.text)

token = j["token"]

headers = {"X-Xapp-Token" : token}

lst = []
for line in sys.stdin:
    r = requests.get("https://api.artsy.net/api/artists/" + line.strip(), headers=headers)
    r.encoding = 'utf-8'
    j = json.loads(r.text)
    lst.append((j['sortable_name'], j['birthday']))
lst.sort()
lst.sort(key=lambda x: x[1])
print(*[i[0] for i in lst], sep='\n', end='')


