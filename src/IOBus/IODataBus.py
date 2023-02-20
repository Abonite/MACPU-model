class DataBus:
    mode = "high_impedance"
    value = 0

    def __init__(self):
        self.mode = "input"
        self.value = 0

    def readMem(self, data: int):
        if self.mode == "input":
            self.value = data
        else:
            raise IOBusCanNotReadError

    def writeMem(self):
        if self.mode == "output":
            return self.value
        else:
            raise IOBusCanNotWriteError

    def setInput(self):
        self.mode = "input"

    def setOutput(self):
        self.mode = "output"

    def deviceReadBus(self):
        if self.mode == "input":
            return self.value
        else:
            raise IOBusCanNotReadError

    def deviceWriteBus(self, data: int):
        if self.mode == "output":
            self.value = data
        else:
            raise IOBusCanNotWriteError
