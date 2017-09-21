from .request import Requester, json
from .formatting import convert_to_markdown
class Challenge:
    def __init__(self, d):
        self.__dict__.update(d)
        self.req = Requester()
    def convert_spec_to_md(self):
        return convert_to_markdown(json.loads(self.content))
