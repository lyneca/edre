from .request import Requester, json

class Comment:
    def __init__(self, d):
        self.__dict__.update(d)
        self.req = Requester()
        self.url = '/comments/' + str(self.id)
        temp = []
        for comment in self.comments:
            temp.append(Comment(comment))
        self.comments = temp
        self.content = json.loads(self.content)

    def like(self):
        return self.req.post(self.url + '/upvote')

    def unlike(self):
        return self.req.post(self.url + '/unvote')

    def reply(self, text):
        return Comment(self.req.post(self.url + '/comments', json.dumps({'comment':{'content':text}})))

    def __str__(self):
        return repr(self)

    def __repr__(self):
        return "Comment{{{}:{:.20}...}}".format(self.id, self.document)
