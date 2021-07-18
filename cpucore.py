import memory
import bus
import drc


class cpu():
    regX = 0
    regZ = 0

    regA = 0
    regB = 0
    regC = 0
    regD = 0
    regE = 0
    regF = 0

    STCK = [0 for i in range(64)]
    STCK_PNTR = 0

    wire_address = 0
    wire_data = 0

    def __init__(
            self,
            coreidx: int = 0,
            memsize: int = 1024,
            itrtblsize: int = 8,
            itrtbl: list = [0, 0, 0, 0],
            itrsrvrtns: list = []):

        memory.initMemory(memsize - itrtblsize - len(itrsrvrtns))
        memory.initITR(itrtbl, itrsrvrtns)
        self.coreindex = coreidx

    # instructions fetch
    def IF(self):
        self.wire_address = self.regX
        self.readBUS()
        self.regZ = self.wire_data

    # decode,execute
    def DC_EX(self):
        self.wire_address = 0
        self.wire_data = 0

        DRC = drc.DRC

        if self.regZ == DRC["SLP"]:
            pass

        elif self.regZ == DRC["RDA"]:
            # TODO:how
            pass

    def readBUS(self):
        self.wire_data = bus.read(self.wire_address)

    def wireBUS(self):
        bus.write(self.wire_address, self.wire_data)
