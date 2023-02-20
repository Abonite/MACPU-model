class PC:
    reg_PC = 0

    def __init__(self):
        self.reg_PC = 0

    def next(self):
        if self.reg_PC + 1 > 0xFFFFFFFF:
            self.reg_PC = 0
        else:
            self.reg_PC += 1
