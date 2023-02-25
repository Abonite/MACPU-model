from typing import List
from .DecoderExceptions import OperateCodeLenthError, \
    RegisterLabelBitsCrowdedError


class Instruction:
    i_type = ""
    i_name = ""
    i_args = []

    op_code = []

    has_t_r = False
    t_r_start_bit = 0

    has_r_1 = False
    r_1_start_bit = 0

    has_r_2 = False
    r_2_start_bit = 0

    has_imdn = False
    imdn_bits = []

    __inst_lenth = 32
    __op_code_lenth = 10
    __op_code_start_bit = 22
    __register_label_bit_lenth = 6
    __unused_bit = 0

    def __init__(
        self,
        instruction_type: str = "",
        instruction_name: str = "",
        instruction_arguments: List[str] = [],
        op_code: List[int] = [0, 0, 0, 0, 0, 0, 0, 0],
        has_target_register: bool = False,
        target_register_start_bit: int = 0,
        has_register_1: bool = False,
        register_1_start_bit: int = 0,
        has_register_2: bool = False,
        register_2_start_bit: int = 0,
        has_immediate_number: bool = False,
        immediate_number: List[int] = []
    ):
        """The start bit of all registers indicates the lowest bit position of
        the register label in the instruction.Bit positions in instructions
        start at 0.
        List of instruction: [bit32, bit31, ..., bit0]
        """

        self.i_type = instruction_type
        self.i_name = instruction_name
        self.i_args = instruction_arguments

        self.op_code = op_code

        self.has_t_r = has_target_register
        self.t_r_start_bit = target_register_start_bit

        self.has_r_1 = has_register_1
        self.r_1_start_bit = register_1_start_bit

        self.has_r_2 = has_register_2
        self.r_2_start_bit = register_2_start_bit

        self.has_imdn = has_immediate_number
        self.imdn_bits = immediate_number

        self.__checkInstrction()

    def __checkInstrction(self):
        if len(self.op_code) == self.__op_code_lenth:
            pass
        else:
            raise OperateCodeLenthError(self.__op_code_lenth)

        __inst = [False for _ in range(self.__inst_lenth)]
        for i in range(self.__op_code_lenth):
            __inst[self.__inst_lenth - i - self.__op_code_start_bit] = True

        if self.has_t_r:
            for i in range(self.__register_label_bit_lenth):
                if __inst[self.__inst_lenth - i - self.t_r_start_bit] is True:
                    raise RegisterLabelBitsCrowdedError("Target")
                else:
                    __inst[self.__inst_lenth - i - self.t_r_start_bit] = True

        if self.has_r_1:
            for i in range(self.__register_label_bit_lenth):
                if __inst[self.__inst_lenth - i - self.r_1_start_bit] is True:
                    raise RegisterLabelBitsCrowdedError("First")
                else:
                    __inst[self.__inst_lenth - i - self.r_1_start_bit] = True

        if self.has_r_2:
            for i in range(self.__register_label_bit_lenth):
                if __inst[self.__inst_lenth - i - self.r_2_start_bit] is True:
                    raise RegisterLabelBitsCrowdedError("Second")
                else:
                    __inst[self.__inst_lenth - i - self.r_2_start_bit] = True

    def isItThisInstruction(self, instruction: List[int]) -> bool:
        start_bit = self.__inst_lenth - self.__op_code_start_bit
        inst_op_code = instruction[
            start_bit + self.__op_code_lenth:start_bit:-1
        ]
        if inst_op_code == self.op_code:
            return True
        else:
            return False


class Instrucitons:
    __LOAD8_IR = Instruction(
        "memory",
        "LOAD8",
        ["imd", "reg"]
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
        True,
        16,
        has_immediate_number=True,
        immediate_number=[7, 6, 5, 4, 3, 2, 1, 0]
    )

    __LOAD8_RR = Instruction(
        "memory",
        "LOAD8",
        ["reg", "reg"]
        [0, 0, 0, 0, 0, 0, 0, 0, 1, 0],
        True,
        16,
        True,
        11,
        True,
        0
    )

    __LOAD16_IR = Instruction(
        "memory",
        "LOAD16",
        ["imd", "reg"]
        [0, 0, 0, 0, 0, 0, 0, 0, 1, 1],
        True,
        16,
        has_immediate_number=True,
        immediate_number=[15, 14, 13, 12, 11, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1, 0]
    )

    __LOAD16_RR = Instruction(
        "memory",
        "LOAD16",
        ["reg", "reg"]
        [0, 0, 0, 0, 0, 0, 0, 1, 0, 0],
        True,
        16,
        True,
        11,
        True,
        0
    )

    __LOAD32_RR = Instruction(
        "memory",
        "LOAD32",
        ["reg", "reg"]
        [0, 0, 0, 0, 0, 0, 0, 1, 0, 1],
        True,
        16,
        True,
        11,
        True,
        0
    )

    __STORE8 = Instruction(
        "memory",
        "STORE8",
        [],
        [0, 0, 0, 0, 0, 0, 0, 1, 1, 0],
        True,

    )

    def __inst__(self):
        pass