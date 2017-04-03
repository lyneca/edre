
from api import *

api = Api(input("Email: "))
thread = int(input('Thread ID: '))
print("starting likespam...")
while True:
    try:
        api.like(thread)
        api.unlike(thread)
    except KeyboardInterrupt:
        print("Stopped.")
        break
