from time import time

from Acquaintance import iLink, iLogic


class linkFacade(iLink.iLink):

    def __init__(self):
        self.logic = iLogic.iLogic

    def inject_logic(self, iLogic):
        self.logic = iLogic

    def run(self):
        v = time()
        print(self.logic.getStreamStatus("humidity"))
        print(time()-v)

