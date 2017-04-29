from .request import Requester, json
from .comment import Comment

class UnrecognizedFormatException(Exception):
    pass

class OverviewException(Exception):
    pass

def get_thread_from_id(thread_id):
    """
    Returns an object inheriting from :class:`thread.Thread` (:class:`thread.Post`, :class:`thread.Question` or :class:`thread.Announcement`) from a thread ID.

    :param thread_id: Thread ID to get
    """
    req = Requester()
    return get_thread(req.get('/threads/' + str(thread_id)))

def get_thread(thread):
    """
    Creates a Thread object of the correct category from a given JSON-dict thread object.
    """
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
    """
    Superclass for dealing with threads.
    """
    def __init__(self, d, overview=False):
        self.overview = overview
        self.__dict__.update(d)
        self.req = Requester()
        self.url = '/threads/' + str(self.id)
        temp = []
        for comment in self.comments:
            temp.append(Comment(comment))
        self.comments = temp

    def __repr__(self):
        return "Thread{{{}:{:.20}...}}".format(self.id, self.title)

    def __str__(self):
        return repr(self)

    def __getattr__(self, attr):
        if attr == 'comments':
            raise OverviewException("thread overviews do not store comments")

    def like(self):
        """Upvotes this post."""
        return self.req.post(self.url + '/upvote')
    
    def unlike(self):
        """Unvotes this post."""
        return self.req.post(self.url + '/unvote')
    
    def star(self):
        """Stars this post."""
        return self.req.post(self.url + '/star')

    def unstar(self):
        """Unstars this post."""
        return self.req.post(self.url + '/unstar')
    
    def read(self):
        """Sends a read receipt for this post."""
        return self.req.post(self.url + '/read')

    def view(self):
        """Increments this post's view counter."""
        return self.req.post(self.url + '/view')

    def comment(self, text):
        """Adds a comment to this post."""
        return self.req.post(self.url + '/comments')
    
class Announcement(Thread):
    """Subclass for announcement threads."""
    def __repr__(self):
        return "Thread.Announcement{{{}:{:.20}...}}".format(self.id, self.title)

class Question(Thread):
    """Subclass for question threads."""
    def __repr__(self):
        return "Thread.Question{{{}:{:.20}...}}".format(self.id, self.title)

    def answer(self, text):
        """Adds an answer to this question."""
        pass  # TODO

class Post(Thread):
    """Subclass for post threads."""
    def __repr__(self):
        return "Thread.Post{{{}:{:.20}...}}".format(self.id, self.title)
