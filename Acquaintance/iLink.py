from abc import ABC, abstractmethod


class iLink(ABC):

    @abstractmethod
    def inject_logic(self, iLogic): raise NotImplementedError

    @abstractmethod
    def run(self): raise NotImplementedError
