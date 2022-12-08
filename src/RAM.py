from src.CpuException import MemoryCapacityTooSmallError


class Ram:
    def __init__(self, size_of_mem: int, ive_size=128, custom_ive_size=64):
        if size_of_mem <= ive_size + custom_ive_size:
            raise MemoryCapacityTooSmallError(ive_size + custom_ive_size)
        else:
            self.memory = [0 for i in range(0, size_of_mem)]

    def getValue(self, address: int):
        return self.memory[address]

    def setValue(self, address: int, value: int):
        self.memory[address] = value

    def printInLine(self):
        i = 0
        for v in range(0, int(len(self.memory)/16)):
            mem_str = [str(x) for x in self.memory[v*16:(v*16)+16]]
            print("{:04x}: {}".format(i*16, "\t\t".join(mem_str)))
            i += 1
