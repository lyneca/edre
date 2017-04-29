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
    def __init__(self, silent=False):
        self.silent = silent
    
    def get_thread_from_id(self, thread_id):
        return get_thread_from_id(thread_id)
    
    def debug(self, *args, **kwargs):
        if not self.silent: print(*args, **kwargs)

    def login(self, username='', password=''):
        token = ''
        self.debug('logging in...')
        request.base_url = "https://edstem.com.au/api"
        self.req = Requester()
        if os.path.exists('.session_key'):
            self.debug("found saved session key. testing... ", end='')
            with open('.session_key') as f:
                token = f.read()
            request.token = token
            temp_req = Requester()
            try:
                temp_req.get('/user')
            except NetworkException as e:
                if e.args[0] == 401:
                    self.debug('invalid.')
                    self.debug('requesting new key...')
                    os.remove('.session_key')
                    token = self._get_token(username, password)
                    self._save_session_key(token)
                else:
                    raise e
            else:
                self.debug('valid.')
        else:
            token = self._get_token(username, password)
            self._save_session_key(token)
        request.token = token
        self.req.update_token()
        self.debug("done.")
        self.debug("getting user/course info... ", end='')
        self.get_info()
        self.debug("done.")
    
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
    
    
