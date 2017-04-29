from .request import Requester

class Comment:
    def __init__(self, d):
        self.__dict__.update(d)
        self.req = Requester()
        self.url = '/comments/' + str(self.id)

    def like():
        return self.req.post(self.url + '/upvote')

    def unlike():
        return self.req.post(self.url + '/unvote')

    def reply():  # TODO
        pass

