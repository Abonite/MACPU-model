from src.ROM import Rom
from src.RAM import Ram
from src.CpuTop import CpuTop
from src.CpuException import ExitError, MemoryCapacityTooSmallError, \
    UndefinedRegisterError, UndefinedOperaterError


class Memory:
    def __init__(self, ram_size: int):
        self.rom = Rom()
        self.rom_size = self.rom.getRomSize()

        self.ram_size = ram_size
        try:
            self.ram = Ram(ram_size)
        except MemoryCapacityTooSmallError:
            print(str(MemoryCapacityTooSmallError))
            input("print Enter to exit...")
            exit()
        else:
            pass

    def getValue(self, address: int):
        if address < self.rom_size:
            return self.rom.getValue(address)
        else:
            return self.ram.getValue(address)

    def setValue(self, address: int, data: int):
        self.ram.setValue(address, data)


class SystemTop:
    def __init__(self, memory_size: int):
        self.cpu = CpuTop(memory_size)
        self.memory = Memory(memory_size)

    def risingEdge(self):
        address = self.cpu.getCurrentAddress()
        data = self.memory.getValue(address)
        is_done, instruction = self.cpu.decodeInstruction(data)
        if is_done:
            try:
                write_to, data, address = \
                    self.cpu.executeInstruction(instruction)
            except ExitError:
                raise ExitError()
            else:
                if write_to == "DMEM":
                    self.memory.setValue(address, data)
                elif write_to == "DREG":
                    match address:
                        case "PC":
                            self.cpu.PC.setPointer(data)
                        case _:
                            raise UndefinedRegisterError(address)
                elif write_to == "IDMEM":
                    self.memory.setValue(address, self.memory.getValue(data))
                elif write_to == "IDREG":
                    match address:
                        case "PC":
                            self.cpu.PC.setPointer(self.memory.getValue(data))
                        case "RegA":
                            self.cpu.EX.reg_a = self.memory.getValue(data)
                        case "RegB":
                            self.cpu.EX.reg_b = self.memory.getValue(data)
                        case "RegC":
                            self.cpu.EX.reg_c = self.memory.getValue(data)
                        case "RegD":
                            self.cpu.EX.reg_d = self.memory.getValue(data)
                        case "RegE":
                            self.cpu.EX.reg_e = self.memory.getValue(data)
                        case "RegF":
                            self.cpu.EX.reg_f = self.memory.getValue(data)
                        case "RegX":
                            self.cpu.EX.reg_x = self.memory.getValue(data)
                        case "RegZ":
                            self.cpu.EX.reg_z = self.memory.getValue(data)
                        case _:
                            raise UndefinedRegisterError(address)
                elif write_to == "NAN":
                    pass
                else:
                    raise UndefinedOperaterError(write_to)
        else:
            pass
