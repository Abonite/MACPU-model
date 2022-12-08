from typing import List
from RegisterExceptions import RegisterOverFlowError


class Register:
    name = ""
    width = 0
    bit_flag = []

    is_flag_reg = False

    reg = []

    def __init__(
            self,
            name: str = "default",
            width: int = 16,
            init_value: int = 0,
            bit_flag: List[str] = []
    ):
        self.name = name
        self.width = width
        self.bit_flag = bit_flag

        if init_value > pow(2, width - 1):
            raise RegisterOverFlowError(width, len(bin(init_value)) - 2)
        else:
            self.reg = [x for x in hex(init_value)[2:]]

        if bit_flag:
            self.is_flag_reg = True


class Reg(Register):
    def __init__(self, name: str, width: int, init_vale: int):
        super().__init__(self, name, width, init_vale)


class FlagReg(Register):
    def __init__(
            self,
            name: str,
            width: int,
            bit_flag: List[str],
            init_value: int
    ):
        super().__init__(self, name, width, init_value, bit_flag)
