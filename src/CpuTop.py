from src.ProgramCounter import PC
from src.Decoder import Decoder
from src.Executer import Executer
from src.CpuException import UndefinedInstructionError
from typing import Tuple


class CpuTop:
    PC = PC()
    DE = Decoder()
    EX = Executer()

    def __init__(self):
        pass

    def getCurrentAddress(self):
        current_address = self.PC.getPointer()
        self.PC.next()
        return current_address

    def decodeInstruction(self, data: int) -> Tuple[bool, list[int, int, int]]:
        return self.DE.setValue(data)

    def executeInstruction(
            self,
            instrction: list[int, int, int]) -> Tuple[bool, int, int | str]:
        try:
            is_write_to_mem, data, address = self.EX.execute(instrction)
        except UndefinedInstructionError:
            print(str(UndefinedInstructionError))
            input("print Enter key to exit...")
            exit()
        else:
            return is_write_to_mem, data, address
