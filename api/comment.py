from .request import Requester

class Comment:
    def __init__(self, d):
        self.__dict__.update(d)
        self.req = Requester()
        self.url = '/comments/' + str(self.id)

    def like():
        pass

    def unlike():
        pass

    def reply():
        pass

