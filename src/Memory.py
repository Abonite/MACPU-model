from CpuException import MemoryCapacityTooSmallError


class Memory:
    DEFAULT_IVE_SIZE = 128
    CUSTOM_IVT_SIZE = 64

    def __init__(self, size_of_mem: int):
        if size_of_mem <= self.DEFAULT_IVE_SIZE + self.CUSTOM_IVT_SIZE:
            raise MemoryCapacityTooSmallError(
                self.DEFAULT_IVE_SIZE + self.CUSTOM_IVT_SIZE
            )
        else:
            self.memory = [0 for i in range(0, size_of_mem)]

    def getValue(self, address: int):
        return self.memory[address]

    def setValue(self, address: int, value: int):
        self.memory[address] = value
