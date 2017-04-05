from api import *
import time

api = Api(input("Email: "))
thread = int(input('Thread ID: '))
print("starting likespam...")
while True:
    try:
        api.like(thread)
        time.sleep(0.5)
        api.unlike(thread)
        time.sleep(0.5)
    except KeyboardInterrupt:
        print("Stopped.")
        break
