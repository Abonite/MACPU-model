from drc import DRC
import mem

MEM = []
MEMsize = 0

wireADDR = 0
wireDATA = 0

sigRST = 0

regIP = 0

regA = 0
regB = 0
regC = 0
regD = 0
regE = 0
regI = 0

regSTCKsize = 64
regSTCKpntr = 0
STCK = [
    0, 0, 0, 0, 0, 0, 0, 0,
    0, 0, 0, 0, 0, 0, 0, 0,
    0, 0, 0, 0, 0, 0, 0, 0,
    0, 0, 0, 0, 0, 0, 0, 0,
    0, 0, 0, 0, 0, 0, 0, 0,
    0, 0, 0, 0, 0, 0, 0, 0,
    0, 0, 0, 0, 0, 0, 0, 0,
    0, 0, 0, 0, 0, 0, 0, 0
    ]


def readAddr(IP):
    global regI
    global MEM

    regI = MEM[IP]


def decode_exec(regI):
    global wireADDR
    global wireDATA
    global regA
    global regB
    global regC
    global regD
    global regE
    global regIP
    global regSTCKpntr
    global regSTCKsize
    global MEM

    if regI == DRC["SLP"]:
        pass
    elif regI == DRC["RDA"]:
        regA = MEM[regIP + 1]
        regIP += 1
    elif regI == DRC["RDB"]:
        regB = MEM[regIP + 1]
        regIP += 1
    elif regI == DRC["RDC"]:
        regC = MEM[regIP + 1]
        regIP += 1
    elif regI == DRC["RDD"]:
        regD = MEM[regIP + 1]
        regIP += 1
    elif regI == DRC["RDE"]:
        regE = MEM[regIP + 1]
        regIP += 1
    elif regI == DRC["WRA"]:
        MEM[regE] = regA
    elif regI == DRC["WRB"]:
        MEM[regE] = regB
    elif regI == DRC["WRC"]:
        MEM[regE] = regC
    elif regI == DRC["WRD"]:
        MEM[regE] = regD
    elif regI == DRC["MAE"]:
        regE = regA
    elif regI == DRC["MEA"]:
        regA = regE
    elif regI == DRC["MBE"]:
        regE = regB
    elif regI == DRC["MEB"]:
        regB = regE
    elif regI == DRC["MAB"]:
        regB = regA

    elif regI == DRC["ADD"]:
        regA += regB
    elif regI == DRC["SUB"]:
        regA -= regB

    elif regI == DRC["PSH"]:
        if regSTCKpntr + 7 <= regSTCKsize:
            STCK[regSTCKpntr] = regA
            STCK[regSTCKpntr + 1] = regB
            STCK[regSTCKpntr + 2] = regC
            STCK[regSTCKpntr + 3] = regD
            STCK[regSTCKpntr + 4] = regE
            STCK[regSTCKpntr + 5] = regI
            STCK[regSTCKpntr + 6] = regIP
            regSTCKpntr += 7
        else:
            print("stack overflow")
    elif regI == DRC["POP"]:
        if regSTCKpntr - 7 >= 0:
            regA = STCK[regSTCKpntr]
            regB = STCK[regSTCKpntr + 1]
            regC = STCK[regSTCKpntr + 2]
            regD = STCK[regSTCKpntr + 3]
            regE = STCK[regSTCKpntr + 4]
            regI = STCK[regSTCKpntr + 5]
            regIP = STCK[regSTCKpntr + 6]
            regSTCKpntr -= 7
        else:
            print("stack empty")

    elif regI == DRC["JMP"]:
        regIP = regE
    elif regI == DRC["JCZ"]:
        if regC == 0:
            regIP = MEM[regE]
        else:
            pass
    elif regI == DRC["JCNZ"]:
        if regC != 0:
            regIP = regE
        else:
            pass
    elif regI == DRC["JDZ"]:
        if regD == 0:
            regIP = regE
        else:
            pass
    elif regI == DRC["JDNZ"]:
        if regD != 0:
            regIP = regE
        else:
            pass
    elif regI == DRC["AEB"]:
        if regA == regB:
            regC = 0
        else:
            pass
    elif regI == DRC["ANEB"]:
        if regA != regB:
            regC = 0
        else:
            pass
    elif regI == DRC["DDO"]:
        regD -= 1
    elif regI == DRC["CDO"]:
        regC -= 1

    elif regI == DRC["OUT"]:
        wireDATA = regA
        wireADDR = regB

    elif regI == DRC["ITR"]:
        regE = MEM[1024 + int(MEM[regIP + 1])]

    elif regI == DRC["STP"]:
        regIP = MEMsize
    else:
        print("wrong drc")


def clrAllReg():
    global regA
    global regB
    global regIP
    global regI

    regA = 0
    regB = 0
    regIP = 0
    regI = 0


def startcpu():
    global regIP
    global regI
    global MEMsize
    global MEM

    MEM = mem.getVal("mem")
    MEMsize = mem.getVal("memsize")

    while True:
        if sigRST:
            clrAllReg()
        else:
            readAddr(regIP)
            decode_exec(regI)
            regIP += 1
            if regIP > MEMsize - 1:
                mem.setMEM(MEMsize, MEM)
                break
