# TODO: interrupt table
# TODO: add it into mem

import mem

itrtablesize = 0


def setITRtable():
    global itrtablesize
    # 0x00: print
    # 0x01: get from keybord
    # 0x02: read from disk
    # 0x03: write to disk
    itr_list = [
        # ITR 0 - print
        0x000F, 0x0000, 0x0000, 0x0000, 0x0000, 0x0000, 0x0000, 0x0000,
        0x0000, 0x0000, 0x0000, 0x0000, 0x0000, 0x0000, 0x0000, 0x0000,
        # print
        # RDB
        # F910 "THE DATA REGISTER OFVIDEO OUTPUT"
        # OUT
        # RDA
        # 0080 "PRINT DATA ON SCREEN"
        # RDB
        # F900 "THE CONTROL REGISTER ADDRESS OF VIDEO OUTPUT"
        # OUT
        # RDA "THERE MUST BE WHERE THE VALUE OF REGISTER A STORAGED"
        # POP
        # JMP
        0x0002, 0xF910, 0x0070, 0x0001, 0x0080, 0x0002, 0xF900, 0x0070, 0x0021, 0x0030,
        # get from key board
        0x0000, 0x0000, 0x0000, 0x0000, 0x0000, 0x0000,
        0x0000, 0x0000, 0x0000, 0x0000, 0x0000, 0x0000, 0x0000, 0x0000,
        0x0000, 0x0000, 0x0000, 0x0000, 0x0000, 0x0000, 0x0000, 0x0000,
        0x0000, 0x0000, 0x0000, 0x0000, 0x0000, 0x0000, 0x0000, 0x0000,
        ]

    itrtablesize = len(itr_list)

    mem.setITR(itr_list)


def getITRsize():
    global itrtablesize

    return itrtablesize
