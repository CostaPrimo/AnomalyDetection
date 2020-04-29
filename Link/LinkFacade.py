from Acquaintance import iLink, iLogic
from Link import RequestHandler

class linkFacade(iLink.iLink):

    def __init__(self):
        self.logic = iLogic.iLogic
        self.test_text = ""

    def inject_logic(self, iLogic):
        self.logic = iLogic
        self.test_text = "Link Virker"

    def run(self, main):
        RequestHandler.run_app(main)

    def printTest(self):
        print(self.test_text)
