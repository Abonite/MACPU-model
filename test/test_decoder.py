from sys import path


path.append("E:\\Code\\python\\pycpu\\src")


from Decoder import InstructionSet


def test_inst_judge_1():
    NOP = InstructionSet.Instruction("Others", "NOP", [1, 1, 0, 0, 0, 0, 0, 1, 1, 0])
    assert(not NOP.isItThisInstruction([0 for _ in range(32)]))


def test_inst_judge_2():
    NOP = InstructionSet.Instruction("Others", "NOP", [1, 1, 0, 0, 0, 0, 0, 1, 1, 0])
    assert(NOP.isItThisInstruction(
        [1, 1, 0, 0, 0, 0, 0, 1, 1, 0,
            0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
            0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
            0, 0]
    ))
