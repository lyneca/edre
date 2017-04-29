from api import *

api = Api(input("Email: "))
thread = int(input('Thread ID: '))
while True:
    api.like(thread)
    api.unlike(thread)
