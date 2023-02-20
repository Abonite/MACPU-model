from src.PC.ProgramCounter import PC
from src.Decoder.Decoder import Decoder
from src.Executer import Executer
from src.CpuException import ExitError, UndefinedInstructionError
from typing import Tuple


class CpuTop:
    def __init__(self, mem_size: int, ive_size=128, custom_ive_size=64):
        self.mem_size = mem_size
        self.ive_size = ive_size
        self.custom_ive_size = custom_ive_size
        self.PC = PC()
        self.DE = Decoder()
        self.EX = Executer(1024, 128)

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
        except ExitError:
            raise ExitError()
        else:
            return is_write_to_mem, data, address
