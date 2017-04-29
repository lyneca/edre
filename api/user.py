from .request import Requester

class User:
    def __init__(self, d):
        self.__dict__.update(d)
        self.req = Requester()
        self.courses = []
