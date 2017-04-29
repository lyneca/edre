"""
ED API

Author: Luke Tuthill
"""

from . import request
from .request import Requester, NetworkException, json
from .course import Course
from .thread import get_thread_from_id
from .comment import Comment
from .user import User
from getpass import getpass
import os


class Api:
    def __init__(self):
        pass

    def login(self, username='', password=''):
        token = ''
        print('logging in...')
        request.base_url = "https://edstem.com.au/api"
        self.req = Requester()
        if os.path.exists('.session_key'):
            print("found saved session key. testing... ", end='')
            with open('.session_key') as f:
                token = f.read()
            request.token = token
            temp_req = Requester()
            try:
                temp_req.get('/user')
            except NetworkException as e:
                if e.args[0] == 401:
                    print('invalid.')
                    print('requesting new key...')
                    os.remove('.session_key')
                    token = self._get_token(username, password)
                    self._save_session_key(token)
                else:
                    raise e
            else:
                print('valid.')
        else:
            token = self._get_token(username, password)
            self._save_session_key(token)
        request.token = token
        self.req.update_token()
        print("done.")
        print("getting user/course info... ", end='')
        self.get_info()
        print("done.")
    
    def _save_session_key(self, token):
        with open('.session_key', 'x') as f:
            f.write(token)


    def _get_token(self, username='', password=''):
        return self.req.post(
            '/token',
            json.dumps({
                'login':    username if username else input('email: '),
                'password': password if password else getpass('password: ')
            })
        )['token']

    def key(self):
        return self.req.access_token

    def get_info(self):
        r = self.req.get('/user')
        self.user = User(r['user'])
        self.courses = [Course(x) for x in r['courses']]
    
if __name__ == '__main__':
    api = Api()
    print(get_thread_from_id(30499).comments)
