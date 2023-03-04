from typing import List
from InstructionSet import Instrucitons
from DecoderExceptions import NoInstructionError, IllegalInstructionError


class PreDecoder:
    instructions = Instrucitons()

    instruction = []

    def __init__(self):
        """The pre-decoding pipeline mainly detects data dependencies and adds
        tags to the instructions that generate data"""

    def latchInstruction(self, inst: List[int]):
        self.instruction = inst

    def checkInstruction(self):
        if not self.instruction:
            raise NoInstructionError
        elif self.Instruciton == [0 for _ in range(32)]:
            raise IllegalInstructionError
        else:
            return

    def getInstrucionInfo(self):
        try:
            type, name = self.instructions.findInstruction(self.instruction)
        except Exception as e:
            raise e
