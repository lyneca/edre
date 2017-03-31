import requests

cookies = {
    '__cfduid': 'd32fe8a2b19e0d403ef32c112e797576d1489465461',
}

headers = {
    'Accept-Encoding': 'gzip, deflate, sdch, br',
    'X-Token': 'eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJleHAiOjE0OTAzMTI3OTksInNlc3Npb25faWQiOjQ2MjUxOCwidXNlcl9pZCI6MjY4NzZ9.4kIF4p-vLPd5AWgDlyX1SPJmWoWZlnRnhodlg7Fm31c',
    'Accept-Language': 'en-GB,en-US;q=0.8,en;q=0.6',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/57.0.2987.98 Safari/537.36',
    'Accept': 'application/json, text/plain, */*',
    'Referer': 'https://edstem.com.au/courses/450/discussion/',
    'X-Requested-With': 'XMLHttpRequest',
    'Connection': 'keep-alive',
}

params = {
    'limit': '20',
    'sort': 'date',
    'order': 'desc'
}

r = requests.get('https://edstem.com.au/api/courses/450/threads', headers=headers, params=params, cookies=cookies)
print(r.status_code, r.reason)
for k in r.json()['threads'][5]:
    print(k + ':', r.json()['threads'][5][k])
print('fetched {} threads'.format(len(r.json()['threads'])))
for post in r.json()['threads']:
    print(post['user']['name'] + ': ' + post['title'])
