class WriteBack:
    def __init__(self):
        pass

    def isWriteToMem(self, value: int, address: str|int):
        if address is int:
            return True, value, address
        else:
            return False, 