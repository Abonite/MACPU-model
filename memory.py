MEMORY_SIZE = 0
MEMORY = []


def initMemory(memsize: int = 1024):
    global MEMORY
    global MEMORY_SIZE

    MEMORY_SIZE = memsize
    MEMORY = [0 for i in range(MEMORY_SIZE)]


def getVal(key) -> int:
    global MEMORY_SIZE
    global MEMORY
    if key == "memsize":
        return MEMORY_SIZE
    elif key == "mem":
        return MEMORY


def initITR(
        itrtbl: list = [0, 0, 0, 0, 0, 0, 0, 0],
        itrsrvrtns: list = []):
    global MEMORY
    global MEMORY_SIZE

    MEMORY = itrtbl + itrsrvrtns + MEMORY


def refreshMemory(Memory: list):
    global MEMORY

    MEMORY = Memory


def getMemoryVal(address: int) -> int:
    global MEMORY

    return MEMORY[address]


def setMemoryVal(address: int, data: int):
    global MEMORY

    MEMORY[address] = data
