from time import time
from Acquaintance import iLink, iLogic
import types


class linkFacade(iLink.iLink):

    def __init__(self):
        self.logic = iLogic.iLogic

    def __get__(self, obj, objtype=None):
        print("__get__")
        if obj is None:
            return self
        return types.MethodType(self, obj)

    def inject_logic(self, iLogic):
        self.logic = iLogic

    def run(self, main):
        print("test")
        v = time()
        print(self.logic.getStreamStatus("humidity"))
        print(time() - v)

    def printTest(self, streamstype):
        print("hEJJJEE")
        logic = self.logic
        result = logic.getStreamStatus(streamstype)
        print("hEJJJEE2")
        return "This data is from the LinkFacade"
