import requests, re, sys


url_list = re.findall(r'<a[^>]*?href.*?=.*?[\"\'](.*?)[\"\'][^>]*?>', requests.get(sys.stdin.read()).text)
site_list = []
for i in url_list:
    j = re.split(r'[\w]*?://', i)
    try:
        x = j[1]
    except IndexError:
        x = j[0]
    y = re.split(r'[:/\'\"]+', x)
    if re.search(r'[\w\.-]+\.[\w\.-]+', y[0]) and y[0] not in site_list:
        site_list.append(y[0])
site_list.sort()
print(*site_list, sep='\n', end='')
