import requests
import json
import getpass
import shutil
import os

WIDTH = shutil.get_terminal_size()[0] - 3

def pad(s, n, ps=' '):
    return str(s)[:n] if len(str(s)) > n else str(s) + (n - len(str(s))) * ps

def lpad(s, n, ps=' '):
    return str(s)[:n] if len(str(s)) > n else (n - len(str(s))) * ps + str(s)

class Post:
    def __init__(self, d):
        self.__dict__.update(d)

    def __str__(self):
        return self.user.name.split()[0] + ': ' + self.title

class Course:
    def __init__(self, d):
        self.__dict__.update(d)

class User:
    def __init__(self, d):
        self.__dict__.update(d)

class ApiError(Exception):
    pass

class Api:
    def __init__(self, email):
        self._key = ''
        print('logging in...')
        if os.path.exists('.session_key'):
            with open('.session_key') as f:
                self._key = f.read()
        else:
            self._key = self._login(email)
            with open('.session_key', 'x') as f:
                f.write(self._key)
        info = self._get_user_info()
        self.user = User(info['user'])
        self.courses = [Course(x) for x in info['courses']]
        print('done.')

    def _error(self, response):
        raise ApiError("{code}: {reason}".format(code=response.status_code, reason=response.reason))

    def _post(self, endpoint, data={}):
        headers = {'content-type': 'application/json;charset=UTF-8'}
        if self._key:
            headers['X-Token'] = self._key
        r = requests.post('https://edstem.com.au/api' + endpoint, headers=headers, data=data)
        if not 200 <= r.status_code < 300:
            return self._error(r)
        if r.content:
            return r.json()

    def _get(self, endpoint, params={}):
        headers = {
            'X-Token': self._key,
        }
        r = requests.get('https://edstem.com.au/api' + endpoint, headers=headers, params=params)
        if not r.status_code == 200:
            return self._error(r)
        return r.json()

    def _login(self, email):
        return self._post('/token', json.dumps({'login': email, 'password': getpass.getpass('password: ')}))['token']

    def _get_posts(self, course, count, filt):
        return [Post(x) for x in self._get(
            '/courses/' + course + '/threads',
            {
                'limit': str(count),
                'sort': 'date',
                'order': 'desc'
            }
        )['threads']]

    def _get_role_symbol(self, user):
        if user.course_role == 'admin': return 'a'
        elif user.course_role == 'tutor': return 't'
        else: return 's'

    def _get_post_flags(self, post):
        out = ''
        out += '.' if post.is_seen else '*'
        out += 'p' if post.type == 'post' else 'q'
        out += '.' if post.is_answered else '?'
        out += '*' if post.is_endorsed else '.'
        out += self._get_role_symbol(post.user)
        return out

    def _get_user_info(self):
        return self._get('/user')
    
    def _get_unread(self):
        print(self._get('/threads/unread')['courses'])  # TODO Do this!

    def post(self, title, content='', category='', staff=False):
        pass

    def like(self, thread_id):
        return self._post('/threads/' + str(thread_id) + '/upvote')

    def unlike(self, thread_id):
        return self._post('/threads/' + str(thread_id) + '/unvote')

    def show_courses(self):
        i = 0
        print('  +---+--------+------+')
        print('  |ID |Name    |Unread|')
        print('+-+---+--------+------+')
        for course in self.courses:
            print(
                '|' +
                chr(i + ord('a')) +
                '|' +
                str(course.id) +
                '|' +
                course.name +
                '|' 
            )
        pass
    
    def list_posts(self, course, count=20, filt=''):
        posts = self._get_posts(str(course), count, filt)
        print('  +-----+' + '-' * (WIDTH - 16) + '+---+---+')
        print('  |staer|' + 'User: Title' + ' ' * (WIDTH - 27) + '|Str|Ans|')
        print('+-+-----+' + '-' * (WIDTH - 16) + '+---+---+')
        i = 0
        for post in posts:
            post.user = User(post.user)
            print(
                '|' + 
                chr(i + ord('a')) + 
                '|' +
                pad(self._get_post_flags(post), 5) + 
                '|' +
                pad(post, (WIDTH - 16)) + 
                '|' + 
                lpad(post.vote_count, 3, '0') +
                '|' + 
                lpad(post.reply_count, 3, '0') +
                '|'
            )
            i += 1
        print('+-+-----+' + '-' * (WIDTH - 16) + '+---+---+')

