from .request import Requester
from .thread import get_thread

class Course:
    def __init__(self, d):
        self.__dict__.update(d)
        self.req = Requester()
        self.url = '/courses/' + str(self.id)

    def post(self, text, type="q"):
        pass

    def get_thread_overviews(self, limit=20, sort='date', order='desc'):
        return [get_thread(t) for t in self.req.get(self.url + '/threads', params={'limit':limit, 'sort': sort, 'order': order})['threads']]

    def __str__(self):
        return repr(self)

    def __repr__(self):
        return "Course{{{}:{}}}".format(self.id, self.code)
