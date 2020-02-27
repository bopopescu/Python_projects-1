from lib.db_manager import Db_manager, manager



try:
    manager()
except Exception as e:
    print("Error => ", e)
