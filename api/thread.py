from .request import Requester, json

class UnrecognizedFormatException(Exception):
    pass

class OverviewException(Exception):
    pass

def get_thread_from_id(thread_id):
    req = Requester()
    return get_thread(req.get('/threads/' + str(thread_id)))

def get_thread(thread):
    types = {
        'announcement': Announcement,
        'question': Question,
        'post': Post
    }
    if 'type' in thread:
        return types[thread['type']](thread, overview=True)
    for t in types:
        if t in thread:
            return types[t](thread[t])
    return UnrecognizedFormatException('Could not detect thread type')

class Thread:
    def __init__(self, d, overview=False):
        self.overview = overview
        self.__dict__.update(d)
        self.req = Requester()
        self.url = '/threads/' + str(self.id)

    def __repr__(self):
        return "Thread{{{}:{:.20}...}}".format(self.id, self.title)

    def __str__(self):
        return repr(self)

    def __getattr__(self, attr):
        if attr == 'comments':
            raise OverviewException("thread overviews do not store comments")

    def like(self):
        return self.req.post(self.url + '/upvote')
    
    def unlike(self):
        return self.req.post(self.url + '/unvote')
    
    def star(self):
        return self.req.post(self.url + '/star')

    def unstar(self):
        return self.req.post(self.url + '/unstar')
    
    def read(self):
        return self.req.post(self.url + '/read')

    def view(self):
        return self.req.post(self.url + '/view')

    def comment(self, text):  # TODO
        return self.req.post(self.url + '/comments')

class Announcement(Thread):
    def __repr__(self):
        return "Thread.Announcement{{{}:{:.20}...}}".format(self.id, self.title)

class Question(Thread):
    def __repr__(self):
        return "Thread.Question{{{}:{:.20}...}}".format(self.id, self.title)

class Post(Thread):
    def __repr__(self):
        return "Thread.Post{{{}:{:.20}...}}".format(self.id, self.title)
