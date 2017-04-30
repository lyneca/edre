from .request import Requester

class User:
    """
    Class for dealing with User objects.

    :param d: Dict representing the user
    """
    def __init__(self, d):
        self.__dict__.update(d)
        self.req = Requester()
        self.courses = []
