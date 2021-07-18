import memory


ADDRESS = 0
DATA = 0


def read(address: int) -> int:
    if (0 <= address) and (address <= memory.getVal("memsize")):
        return memory.getMemoryVal(address)
    else:
        return 0


def write(address: int, data: int):
    if (0 <= address) and (address <= memory.getVal("memsize")):
        memory.setMemoryVal(address, data)
    else:
        pass
