from api import Api
import json
import sys
import requests
commentstr = {'comment': {'content': '{"version":0,"nodeNextId":24,"blockNextId":0,"document":{"paragraphs":[{"id":10,"style":{"listType":0,"listLevel":0},"blocks":[],"runs":[{"id":12,"spans":[{"id":13,"HELLO":"test","url":null,"style":{}}]}]}]}}','document': "HELLO"}}
api = Api("")
def spam(id): requests.delete("https://edstem.com.au/api/comments/" + str(api._post("/comments/" + str(id) + "/comments", json.dumps(commentstr))['comment']['id']), headers={'X-Token': api._key})

while True:
    spam(sys.argv[1])
