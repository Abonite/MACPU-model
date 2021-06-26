MEMsize = 0
MEM = []


def setMEM(size, memory):
    global MEMsize
    global MEM
    MEM = memory
    MEMsize = size


def getVal(key):
    global MEMsize
    global MEM
    if key == "memsize":
        return MEMsize
    elif key == "mem":
        return MEM
