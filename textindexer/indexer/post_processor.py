from textindexer.database import DocsDatabase

class PostProcessor():

    def __init__(self, mongo={}, mq={}):
        self._db = DocsDatabase(mongo=mongo)

    def test(self):
        pass
