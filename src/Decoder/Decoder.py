from typing import List
from InstructionSet import Instrucitons


class Decoder:
    curr_instruction = [0 for _ in range(32)]

    __i_s = Instrucitons()

    def __init__(self):
        """left is high bit, right is low"""
        pass

    def decode(self, inst: List[int]):
        self.__i_s.findInstruction(inst)


d = Decoder()
d.decode([
    1, 0, 0, 0, 1, 0, 0, 0,
    0, 0, 0, 0, 0, 0, 0, 0,
    0, 0, 0, 0, 0, 0, 0, 0,
    0, 0, 0, 0, 0, 0, 0, 0])
