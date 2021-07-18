from drc import DRC
import memory
import interrupt


def encodefile():
    buffer = []

    with open("test_Fibonacci.pcc", "r") as pcc:
        for line in pcc:
            code_line = line.rstrip("\n").split(" ")
            for val in code_line:
                if code_line.index(val) == 0:
                    buffer.append(DRC[val])
                else:
                    buffer.append(int(val))

        pcc.close()

    buffer += [0 for i in range(1024 - len(buffer))]
    mem.setMEM(1024, buffer)
    interrupt.setITRtable()
