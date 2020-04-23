from Acquaintance import iLink, iLogic


class linkFacade(iLink.iLink):

    def __init__(self):
        self.logic = iLogic.iLogic
        self.test_text = ""

    def inject_logic(self, iLogic):
        self.logic = iLogic
        self.test_text = "Link Virker"

    def run(self): raise NotImplementedError

    def printTest(self):
        print(self.test_text)
