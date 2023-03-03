from PCExceptions import PCAddressOverFlowError


class PC:
    reg_PC = 0

    max_addr = 0xFFFFFFFF

    def __init__(self, max_addr: int = 0xFFFFFFFF):
        self.reg_PC = 0
        self.max_addr = max_addr

    def next(self):
        if self.reg_PC + 1 > self.max_addr:
            self.reg_PC = 0
        else:
            self.reg_PC += 1

    def setAddr(self, addr: int):
        if addr > self.max_addr:
            raise PCAddressOverFlowError(addr)
        else:
            self.reg_PC = addr
