import sys
from api import Api
api = Api("ltut8436@uni.sydney.edu.au")
while True: api.view(sys.argv[1])
