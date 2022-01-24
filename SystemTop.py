from src.Memory import Memory
from src.CpuTop import CpuTop
from src.CpuException import MemoryCapacityTooSmallError


class SystemTop:
    cpu = CpuTop()

    def __init__(self, memory_size: int):
        try:
            self.memory = Memory(memory_size)
        except MemoryCapacityTooSmallError:
            print(str(MemoryCapacityTooSmallError))
            input("print Enter to exit...")
            exit()
        else:
            pass

    def risingEdge(self):
        address = self.cpu.getCurrentAddress()
        data = self.memory.getValue(address)
        is_done, instruction = self.cpu.decodeInstruction(data)
        if is_done:
            # TODO: need three different state here: write to memory,
            # write to register, or noting to do
            is_write_to_mem, data, address = \
                self.cpu.executeInstruction(instruction)
            if is_write_to_mem:
                self.memory.setValue(address, data)
            else:
                pass
        else:
            pass
