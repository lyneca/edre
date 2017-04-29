from api import Api
api = Api('')
post_ids = [p.id for p in api._get_posts(input("course: "), 10, '')]
while True:
    for p in post_ids:
        api.like(p)
    for p in reversed(post_ids):
        api.unlike(p)
