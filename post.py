import requests

cookies = {
    '__cfduid': 'd32fe8a2b19e0d403ef32c112e797576d1489465461',
}

headers = {
    'Origin': 'https://edstem.com.au',
    'Accept-Encoding': 'gzip, deflate, br',
    'X-Token': 'eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJleHAiOjE0OTAzMTI3OTksInNlc3Npb25faWQiOjQ2MjUxOCwidXNlcl9pZCI6MjY4NzZ9.4kIF4p-vLPd5AWgDlyX1SPJmWoWZlnRnhodlg7Fm31c',
    'Accept-Language': 'en-GB,en-US;q=0.8,en;q=0.6',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/57.0.2987.98 Safari/537.36',
    'Content-Type': 'application/json;charset=UTF-8',
    'Accept': 'application/json, text/plain, */*',
    'Referer': 'https://edstem.com.au/courses/450/discussion/new',
    'X-Requested-With': 'XMLHttpRequest',
    'Connection': 'keep-alive',
}

data = '{"question":{"type":"question","title":"Python Lectures","category":"Staff","subcategory":"","content":"{\\"version\\":0,\\"nodeNextId\\":2714,\\"blockNextId\\":0,\\"document\\":{\\"paragraphs\\":[{\\"id\\":1247,\\"style\\":{\\"listType\\":0,\\"listLevel\\":0},\\"blocks\\":[],\\"runs\\":[{\\"id\\":1249,\\"spans\\":[{\\"id\\":1250,\\"text\\":\\"Which lectures are going to be Intro to Python? Will there be a particular lecture dedicated to Python?\\",\\"url\\":null,\\"style\\":{}}]}]}]}}","is_pinned":false,"is_private":false,"is_anonymous":false,"document":"Which lectures are going to be Intro to Python? Will there be a particular lecture dedicated to Python?"}}'

requests.post('https://edstem.com.au/api/courses/450/threads', headers=headers, cookies=cookies, data=data)

