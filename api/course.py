from .request import Requester, json
from .thread import get_thread

class Course:
    def __init__(self, d):
        self.__dict__.update(d)
        self.req = Requester()
        self.url = '/courses/' + str(self.id)

    def post(self, title, text, thread_type="p", category="General", subcategory="", pinned=False, private=False, anon=False):
        thread_type = {'q':'question','p':'post','a':'announcement'}[thread_type]
        thread = {
            "post":{
                "type": thread_type,
                "title": title,
                "category": category,
                "subcategory": subcategory, 
                "content": text,
                "is_pinned": str(pinned).lower(),
                "is_private": str(private).lower(),
                "is_anonymous": str(anon).lower()
            }
        }
        return self.req.post('/courses/542/threads', json.dumps(thread))


    def get_thread_overviews(self, limit=20, sort='date', order='desc'):
        return [get_thread(t) for t in self.req.get(self.url + '/threads', params={'limit':limit, 'sort': sort, 'order': order})['threads']]

    def __str__(self):
        return repr(self)

    def __repr__(self):
        return "Course{{{}:{}}}".format(self.id, self.code)
