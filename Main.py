from Link import LinkFacade
from Logic import LogicFacade
from Persistence import PersistenceFacade


persistence = PersistenceFacade.persistenceFacade()
logic = LogicFacade.logicFacade()
link = LinkFacade.linkFacade()

logic.inject_persistence(persistence)
link.inject_logic(logic)

print("Starting the application")
link.run(__name__)
