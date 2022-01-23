class PC:
    def __init__(self):
        self.pointer = 0

    def next(self):
        self.pointer += 1

    def setPointer(self, value: int):
        self.pointer = value

    def last(self):
        self.pointer -= 1

    def getPointer(self, value: int):
        return self.pointer()
