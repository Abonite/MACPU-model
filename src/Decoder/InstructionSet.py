from typing import List
from DecoderExceptions import OperateCodeLenthError, \
    RegisterLabelBitsCrowdedError, \
    InstructionLenthError, \
    RegisterLabelLenthError, \
    ImmediateNumberBitsCrowdedError, \
    NotThisInstructionError, \
    InvalidBitValueError


class Instruction:
    i_type = ""
    i_name = ""

    op_code = []

    __source_register_bits = []
    __target_register_bits = []
    __immediate_number_bits = []

    __inst_lenth = 32
    __op_code_bits = [31, 30, 29, 28, 27, 26, 25, 24]
    __register_label_bit_lenth = 6
    __unused_bit = 0

    __check_flag = [False for _ in range(__inst_lenth)]

    def __init__(
        self,
        instruction_type: str = "",
        instruction_name: str = "",
        op_code: List[int] = [0, 0, 0, 0, 0, 0, 0, 0],
        source_register_bits: List[int] = [],
        target_register_bits: List[int] = [],
        immediate_number: List[int] = []
    ):
        self.i_type = instruction_type
        self.i_name = instruction_name
        self.op_code = op_code
        self.__immediate_number_bits = immediate_number
        self.__source_register_bits = source_register_bits
        self.__target_register_bits = target_register_bits

    def __checkOPCode(self):
        if len(self.op_code) != 10:
            raise OperateCodeLenthError(len(self.__op_code_bits))
        else:
            for i in self.__op_code_bits:
                self.check_flag[self.__inst_lenth - 1 - i] = True

    def __checkImmediateNumber(self):
        if not self.__immediate_number_bits:
            return
        else:
            for i in self.__immediate_number_bits:
                if self.check_flag[self.__inst_lenth - 1 - i]:
                    raise ImmediateNumberBitsCrowdedError(i)
                else:
                    self.check_flag[self.__inst_lenth - 1 - i] = True

    def __isItThisInstruction(self, inst: List[int]) -> bool:
        if len(inst) == self.__inst_lenth:
            raise InstructionLenthError(self.__inst_lenth)
        else:
            if [inst[self.__inst_lenth - 1 - x] for x in self.__op_code_bits] \
                    == self.op_code:
                for i, f, b in enumerate(zip(self.__check_flag, inst)):
                    if f:
                        pass
                    else:
                        if b == self.__unused_bit:
                            pass
                        else:
                            raise InvalidBitValueError(
                                self.i_name,
                                self.__inst_lenth - 1 - i,
                                self.__unused_bit
                            )
            else:
                raise NotThisInstructionError(self.i_name)

    def __checkSourceRegister(self):
        if len(self.__source_regerter_bits) \
                != self.__register_label_bit_lenth:
            raise RegisterLabelLenthError(self.__register_label_bit_lenth)
        else:
            for i in self.__source_register_bits:
                if self.check_flag[self.__inst_lenth - 1 - i]:
                    raise RegisterLabelBitsCrowdedError("source register")
                else:
                    self.check_flag[self.__inst_lenth - 1 - i] = True

    def __checkTargetRegister(self):
        if len(self.__target_register_bits) \
                != self.__register_label_bit_lenth:
            raise RegisterLabelLenthError(self.__register_label_bit_lenth)
        else:
            for i in self.__target_register_bits:
                if self.check_flag[self.__inst_lenth - 1 - i]:
                    raise RegisterLabelBitsCrowdedError("target register")
                else:
                    self.check_flag[self.__inst_lenth - 1 - i] = True


class LOAD(Instruction):
    __fsource_register_bits = []
    __ssource_register_bits = []

    def __init__(
        self,
        instruction_type: str = "",
        instruction_name: str = "",
        op_code: List[int] = [0, 0, 0, 0, 0, 0, 0, 0],
        target_register: List[int] = [21, 20, 19, 18, 17, 16],
        immediate_number: List[int] = [],
        first_source_register: List[int] = [],
        second_source_register: List[int] = []
    ):
        super().__init__(
            instruction_type=instruction_type,
            instruction_name=instruction_name,
            op_code=op_code,
            immediate_number=immediate_number,
            target_register_bits=target_register
        )

        self.__fsource_register_bits = first_source_register
        self.__ssource_register_bits = second_source_register

        self.__checkInstructionIntegrity()

    def __checkInstructionIntegrity(self):
        self.__checkOPCode()
        self.__checkTargetRegister()
        self.__checkFirstSourceRegister()
        self.__checkSecondSourceRegister()
        self.__checkImmediateNumber()

    def __checkFirstSourceRegister(self):
        if not self.__fsource_register_bits:
            return
        elif len(self.__fsource_register_bits) \
                != self.__register_label_bit_lenth:
            raise RegisterLabelLenthError(
                self.__register_label_bit_lenth,
                "first source registr"
            )
        else:
            for i in self.__fsource_register_bits:
                if self.check_flag[self.__inst_lenth - 1 - i]:
                    raise RegisterLabelBitsCrowdedError(
                        "first source register",
                        i
                    )
                else:
                    self.check_flag[self.__inst_lenth - 1 - i] = True

    def __checkSecondSourceRegister(self):
        if not self.__ssource_register_bits:
            return
        elif len(self.__ssource_register_bits) \
                != self.__register_label_bit_lenth:
            raise RegisterLabelLenthError(
                self.__register_label_bit_lenth,
                "second source registr"
            )
        else:
            for i in self.__fsource_register_bits:
                if self.check_flag[self.__inst_lenth - 1 - i]:
                    raise RegisterLabelBitsCrowdedError(
                        "second source register",
                        i
                    )
                else:
                    self.check_flag[self.__inst_lenth - 1 - i] = True


class STORE(Instruction):
    __ftarget_register_bits = []
    __starget_register_bits = []

    def __init__(
        self,
        instruction_type: str = "",
        instruction_name: str = "",
        op_code: List[int] = [0, 0, 0, 0, 0, 0, 0, 0],
        source_register: List[int] = [21, 20, 19, 18, 17, 16],
        first_target_register: List[int] = [],
        second_target_register: List[int] = []
    ):
        super().__init__(
            instruction_type=instruction_type,
            instruction_name=instruction_name,
            op_code=op_code,
            source_register_bits=source_register
        )

        self.__ftarget_register_bits = first_target_register
        self.__starget_register_bits = second_target_register

        self.__checkInstructionIntegrity()

    def __checkInstructionIntegrity(self):
        self.__checkOPCode()
        self.__checkSourceRegister()
        self.__checkFirstTargetRegister()
        self.__checkSecondTargetRegister()

    def __checkFirstTargetRegister(self):
        if not self.__ftarget_register_bits:
            return
        elif len(self.__ftarget_register_bits) \
                != self.__register_label_bit_lenth:
            raise RegisterLabelLenthError(
                self.__register_label_bit_lenth,
                "first target registr"
            )
        else:
            for i in self.__fsource_register_bits:
                if self.check_flag[self.__inst_lenth - 1 - i]:
                    raise RegisterLabelBitsCrowdedError(
                        "first target register",
                        i
                    )
                else:
                    self.check_flag[self.__inst_lenth - 1 - i] = True

    def __checkSecondTargetRegister(self):
        if not self.__starget_register_bits:
            return
        elif len(self.__starget_register_bits) \
                != self.__register_label_bit_lenth:
            raise RegisterLabelLenthError(
                self.__register_label_bit_lenth,
                "second target registr"
            )
        else:
            for i in self.__fsource_register_bits:
                if self.check_flag[self.__inst_lenth - 1 - i]:
                    raise RegisterLabelBitsCrowdedError(
                        "second target register",
                        i
                    )
                else:
                    self.check_flag[self.__inst_lenth - 1 - i] = True


class MOVE(Instruction):
    def __init__(
        self,
        instruction_type: str = "",
        instruction_name: str = "",
        op_code: List[int] = [0, 0, 0, 0, 0, 0, 0, 0],
        source_register: List[int] = [5, 4, 3, 2, 1, 0],
        target_register: List[int] = [21, 20, 19, 18, 17, 16],
    ):
        super().__init__(
            instruction_type=instruction_type,
            instruction_name=instruction_name,
            op_code=op_code,
            source_register_bits=source_register,
            target_register_bits=target_register
        )

        self.__checkInstructionIntegrity()

    def __checkInstructionIntegrity(self):
        self.__checkOPCodeLenth()
        self.__checkSourceRegister()
        self.__checkTargetRegister()


class INTEGER(Instruction):
    __asource_register_bits = []
    __aimmediate_number_bits = []

    def __init__(
        self,
        instruction_type: str = "",
        instruction_name: str = "",
        op_code: List[int] = [0, 0, 0, 0, 0, 0, 0, 0],
        target_register: List[int] = [21, 20, 19, 18, 17, 16],
        source_register: List[int] = [11, 10, 9, 8, 7, 6],
        another_source_register: List[int] = [],
        immediate_number: List[int] = [],
        another_immediate_number: List[int] = []
    ):
        super().__init__(
            instruction_type=instruction_type,
            instruction_name=instruction_name,
            op_code=op_code,
            target_register_bits=target_register,
            source_register_bits=source_register,
            immediate_number=immediate_number,
        )

        self.__asource_register_bits = another_source_register
        self.__aimmediate_number_bits = another_immediate_number

        self.__checkInstructionIntegrity()

    def __checkInstructionIntegrity(self):
        self.__checkOPCodeLenth()
        self.__checkSourceRegister()
        self.__checkTargetRegister()
        self.__checkASourceRegister()
        self.__checkImmediateNumber()
        self.__checkAImmediateNumber()

    def __checkASourceRegister(self):
        if not self.__asource_register_bits:
            return
        elif len(self.__asource_register_bits) \
                != self.__register_label_bit_lenth:
            raise RegisterLabelLenthError(
                self.__register_label_bit_lenth,
                "another source register"
            )
        else:
            for i in self.__asource_register_bits:
                if self.check_flag[self.__inst_lenth - 1 - i]:
                    raise RegisterLabelBitsCrowdedError(
                        "another source register"
                    )
                else:
                    self.check_flag[self.__inst_lenth - 1 - i] = True

    def __checkAImmediateNumber(self):
        if not self.__aimmediate_number_bits:
            return
        else:
            for i in self.__aimmediate_number_bits:
                if self.check_flag[self.__inst_lenth - 1 - i]:
                    raise ImmediateNumberBitsCrowdedError(i)
                else:
                    self.check_flag[self.__inst_lenth - 1 - i] = True


class BRANCH(Instruction):
    __asource_register_bits = []

    def __init__(
        self,
        instruction_type: str = "",
        instruction_name: str = "",
        op_code: List[int] = [0, 0, 0, 0, 0, 0, 0, 0],
        target_register: List[int] = [21, 20, 19, 18, 17, 16],
        source_register: List[int] = [11, 10, 9, 8, 7, 6],
        another_source_register: List[int] = [],
        immediate_number: List[int] = []
    ):
        super().__init__(
            instruction_type=instruction_type,
            instruction_name=instruction_name,
            op_code=op_code,
            target_register_bits=target_register,
            source_register_bits=source_register,
            immediate_number=immediate_number,
        )

        self.__asource_register_bits = another_source_register

        self.__checkInstructionIntegrity()

    def __checkInstructionIntegrity(self):
        self.__checkOPCodeLenth()
        self.__checkSourceRegister()
        self.__checkTargetRegister()
        self.__checkASourceRegister()
        self.__immediate_number_bits()

    def __checkASourceRegister(self):
        if not self.__asource_register_bits:
            return
        elif len(self.__asource_register_bits) \
                != self.__register_label_bit_lenth:
            raise RegisterLabelLenthError(
                self.__register_label_bit_lenth,
                "another source register"
            )
        else:
            for i in self.__asource_register_bits:
                if self.check_flag[self.__inst_lenth - 1 - i]:
                    raise RegisterLabelBitsCrowdedError(
                        "another source register"
                    )
                else:
                    self.check_flag[self.__inst_lenth - 1 - i] = True


class JUMP(Instruction):
    __fsource_register_bits = []
    __ssource_register_bits = []

    def __init__(
        self,
        instruction_type: str = "",
        instruction_name: str = "",
        op_code: List[int] = [0, 0, 0, 0, 0, 0, 0, 0],
        first_source_register: List[int] = [],
        second_source_register: List[int] = [],
        immediate_number: List[int] = []
    ):
        super().__init__(
            instruction_type=instruction_type,
            instruction_name=instruction_name,
            op_code=op_code,
            immediate_number=immediate_number
        )

        self.__fsource_register_bits = first_source_register
        self.__ssource_register_bits = second_source_register

        self.__checkInstructionIntegrity()

    def __checkInstructionIntegrity(self):
        self.__checkOPCodeLenth()
        self.__checkFirstSourceRegister()
        self.__checkSecondSourceRegister()

    def __checkFirstSourceRegister(self):
        if not self.__fsource_register_bits:
            return
        elif len(self.__fsource_register_bits) \
                != self.__register_label_bit_lenth:
            raise RegisterLabelLenthError(
                self.__register_label_bit_lenth,
                "first source registr"
            )
        else:
            for i in self.__fsource_register_bits:
                if self.check_flag[self.__inst_lenth - 1 - i]:
                    raise RegisterLabelBitsCrowdedError(
                        "first source register",
                        i
                    )
                else:
                    self.check_flag[self.__inst_lenth - 1 - i] = True

    def __checkSecondSourceRegister(self):
        if not self.__ssource_register_bits:
            return
        elif len(self.__ssource_register_bits) \
                != self.__register_label_bit_lenth:
            raise RegisterLabelLenthError(
                self.__register_label_bit_lenth,
                "second source registr"
            )
        else:
            for i in self.__fsource_register_bits:
                if self.check_flag[self.__inst_lenth - 1 - i]:
                    raise RegisterLabelBitsCrowdedError(
                        "second source register",
                        i
                    )
                else:
                    self.check_flag[self.__inst_lenth - 1 - i] = True


class instrucitons:
    __LOAD8_IR = LOAD(
        "memory",
        "LOAD8",
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
        immediate_number=[7, 6, 5, 4, 3, 2, 1, 0]
    )

    __LOAD8_RR = LOAD(
        "memory",
        "LOAD8",
        [0, 0, 0, 0, 0, 0, 0, 0, 1, 0],
        first_source_register=[11, 10, 9, 8, 7, 6],
        second_source_register=[5, 4, 3, 2, 1, 0]
    )

    __LOAD16_IR = LOAD(
        "memory",
        "LOAD16",
        [0, 0, 0, 0, 0, 0, 0, 0, 1, 1],
        immediate_number=[15, 14, 13, 12, 11, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1, 0]
    )

    __LOAD16_RR = LOAD(
        "memory",
        "LOAD16",
        [0, 0, 0, 0, 0, 0, 0, 1, 0, 0],
        first_source_register=[11, 10, 9, 8, 7, 6],
        second_source_register=[5, 4, 3, 2, 1, 0]
    )

    __LOAD32 = LOAD(
        "memory",
        "LOAD32",
        [0, 0, 0, 0, 0, 0, 0, 1, 0, 1],
        first_source_register=[11, 10, 9, 8, 7, 6],
        second_source_register=[5, 4, 3, 2, 1, 0]
    )

    __STORE8 = STORE(
        "memory",
        "STORE8",
        [0, 0, 0, 0, 0, 0, 0, 1, 0, 1],
        first_target_register=[11, 10, 9, 8, 7, 6],
        second_target_register=[5, 4, 3, 2, 1, 0]
    )

    __STORE16 = STORE(
        "memory",
        "STORE16",
        [0, 0, 0, 0, 0, 0, 0, 1, 1, 0],
        first_target_register=[11, 10, 9, 8, 7, 6],
        second_target_register=[5, 4, 3, 2, 1, 0]
    )

    __STORE32 = STORE(
        "memory",
        "STORE32",
        [0, 0, 0, 0, 0, 0, 0, 1, 1, 1],
        first_target_register=[11, 10, 9, 8, 7, 6],
        second_target_register=[5, 4, 3, 2, 1, 0]
    )

    __MOVE = MOVE(
        "register",
        "MOVE",
        [0, 0, 0, 0, 0, 0, 1, 0, 0, 1]
    )

    __ADD_RR = INTEGER(
        "integer",
        "ADD",
        [1, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        another_source_register=[5, 4, 3, 2, 1, 0]
    )

    __ADD_IR = INTEGER(
        "integer",
        "ADD",
        [1, 0, 0, 0, 0, 0, 0, 0, 0, 1],
        immediate_number=[15, 14, 13, 12, 5, 4, 3, 2, 1, 0]
    )

    __SUB_RR = INTEGER(
        "integer",
        "SUB",
        [1, 0, 0, 0, 0, 0, 0, 0, 1, 0],
        another_source_register=[5, 4, 3, 2, 1, 0]
    )

    __SUB_RI = INTEGER(
        "integer",
        "SUB",
        [1, 0, 0, 0, 0, 0, 0, 0, 1, 1],
        immediate_number=[15, 14, 13, 12, 5, 4, 3, 2, 1, 0]
    )

    __SUB_IR = INTEGER(
        "integer",
        "SUB",
        [1, 0, 0, 0, 0, 0, 0, 1, 0, 0],
        immediate_number=[15, 14, 13, 12, 5, 4, 3, 2, 1, 0]
    )

    __BAND_RR = INTEGER(
        "integer",
        "BAND",
        [1, 0, 0, 0, 0, 0, 0, 1, 0, 1],
        another_source_register=[5, 4, 3, 2, 1, 0]
    )

    __BAND_IR = INTEGER(
        "integer",
        "BAND",
        [1, 0, 0, 0, 0, 0, 0, 1, 1, 0],
        immediate_number=[15, 14, 13, 12, 5, 4, 3, 2, 1, 0]
    )

    __BOR_RR = INTEGER(
        "integer",
        "BOR",
        [1, 0, 0, 0, 0, 0, 0, 1, 1, 0],
        another_source_register=[5, 4, 3, 2, 1, 0]
    )

    __BOR_IR = INTEGER(
        "integer",
        "BOR",
        [1, 0, 0, 0, 0, 0, 0, 1, 1, 1],
        immediate_number=[15, 14, 13, 12, 5, 4, 3, 2, 1, 0]
    )

    __BNOT_R = INTEGER(
        "integer",
        "BNOT",
        [1, 0, 0, 0, 0, 0, 1, 0, 0, 0],
        source_register=[],
        another_source_register=[5, 4, 3, 2, 1, 0]
    )

    __BNOT_I = INTEGER(
        "integer",
        "BNOT",
        [1, 0, 0, 0, 0, 0, 1, 0, 0, 1],
        immediate_number=[15, 14, 13, 12, 11, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1, 0]
    )

    __BXOR_RR = INTEGER(
        "integer",
        "BOR",
        [1, 0, 0, 0, 0, 0, 1, 0, 1, 0],
        another_source_register=[5, 4, 3, 2, 1, 0]
    )

    __BXOR_IR = INTEGER(
        "integer",
        "BOR",
        [1, 0, 0, 0, 0, 0, 1, 0, 1, 1],
        immediate_number=[15, 14, 13, 12, 5, 4, 3, 2, 1, 0]
    )

    __RAND = INTEGER(
        "integer",
        "RAND",
        [1, 0, 0, 0, 0, 0, 1, 1, 0, 0],
    )

    __ROR = INTEGER(
        "integer",
        "ROR",
        [1, 0, 0, 0, 0, 0, 1, 1, 0, 1],
    )

    __RXOR = INTEGER(
        "integer",
        "RXOR",
        [1, 0, 0, 0, 0, 0, 1, 1, 1, 0],
    )

    __MUL_RR = INTEGER(
        "integer",
        "MUL",
        [1, 0, 0, 0, 0, 0, 1, 1, 1, 1],
        another_source_register=[5, 4, 3, 2, 1, 0]
    )

    __MUL_RI = INTEGER(
        "integer",
        "MUL",
        [1, 0, 0, 0, 0, 1, 0, 0, 0, 0],
        immediate_number=[15, 14, 13, 12, 5, 4, 3, 2, 1, 0]
    )

    __DIV_RR = INTEGER(
        "integer",
        "DIV",
        [1, 0, 0, 0, 0, 1, 0, 0, 0, 1],
        another_source_register=[5, 4, 3, 2, 1, 0]
    )

    __DIV_RI = INTEGER(
        "integer",
        "DIV",
        [1, 0, 0, 0, 0, 1, 0, 0, 1, 0],
        immediate_number=[15, 14, 13, 12, 5, 4, 3, 2, 1, 0]
    )

    __DIV_IR = INTEGER(
        "integer",
        "DIV",
        [1, 0, 0, 0, 0, 1, 0, 0, 1, 1],
        immediate_number=[15, 14, 13, 12, 5, 4, 3, 2, 1, 0]
    )

    __LS_RR = INTEGER(
        "integer",
        "LS",
        [1, 0, 0, 0, 0, 0, 1, 0, 1, 0, 0],
        source_register=[11, 10, 9, 8, 7, 6],
        another_source_register=[5, 4, 3, 2, 1, 0]
    )

    __LS_RI = INTEGER(
        "integer",
        "LS",
        [1, 0, 0, 0, 0, 0, 1, 0, 1, 0, 1],
        source_register=[11, 10, 9, 8, 7, 6],
        immediate_number=[15, 14, 13, 12, 5, 4, 3, 2, 1, 0]
    )

    __LS_IR = INTEGER(
        "integer",
        "LS",
        [1, 0, 0, 0, 0, 0, 1, 0, 1, 1, 0],
        source_register=[11, 10, 9, 8, 7, 6],
        immediate_number=[15, 14, 13, 12, 5, 4, 3, 2, 1, 0]
    )

    __LS_II = INTEGER(
        "integer",
        "LS",
        [1, 0, 0, 0, 0, 0, 1, 0, 1, 1, 1],
        immediate_number=[15, 14, 13, 12, 11, 10, 9, 8, 7, 6],
        another_immediate_number=[5, 4, 3, 2, 1, 0]
    )

    __LRS_RR = INTEGER(
        "integer",
        "LRS",
        [1, 0, 0, 0, 0, 0, 1, 1, 0, 0, 0],
        source_register=[11, 10, 9, 8, 7, 6],
        another_source_register=[5, 4, 3, 2, 1, 0]
    )

    __LRS_RI = INTEGER(
        "integer",
        "LRS",
        [1, 0, 0, 0, 0, 0, 1, 1, 0, 0, 1],
        source_register=[11, 10, 9, 8, 7, 6],
        immediate_number=[15, 14, 13, 12, 5, 4, 3, 2, 1, 0]
    )

    __LRS_IR = INTEGER(
        "integer",
        "LRS",
        [1, 0, 0, 0, 0, 0, 1, 1, 0, 1, 0],
        source_register=[11, 10, 9, 8, 7, 6],
        immediate_number=[15, 14, 13, 12, 5, 4, 3, 2, 1, 0]
    )

    __LRS_II = INTEGER(
        "integer",
        "LRS",
        [1, 0, 0, 0, 0, 0, 1, 1, 0, 1, 1],
        immediate_number=[15, 14, 13, 12, 11, 10, 9, 8, 7, 6],
        another_immediate_number=[5, 4, 3, 2, 1, 0]
    )

    __ARS_RR = INTEGER(
        "integer",
        "ARS",
        [1, 0, 0, 0, 0, 0, 1, 1, 1, 0, 0],
        source_register=[11, 10, 9, 8, 7, 6],
        another_source_register=[5, 4, 3, 2, 1, 0]
    )

    __ARS_RI = INTEGER(
        "integer",
        "ARS",
        [1, 0, 0, 0, 0, 0, 1, 1, 1, 0, 1],
        source_register=[11, 10, 9, 8, 7, 6],
        immediate_number=[15, 14, 13, 12, 5, 4, 3, 2, 1, 0]
    )

    __ARS_IR = INTEGER(
        "integer",
        "ARS",
        [1, 0, 0, 0, 0, 0, 1, 1, 1, 1, 0],
        source_register=[11, 10, 9, 8, 7, 6],
        immediate_number=[15, 14, 13, 12, 5, 4, 3, 2, 1, 0]
    )

    __ARS_II = INTEGER(
        "integer",
        "ARS",
        [1, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1],
        immediate_number=[15, 14, 13, 12, 11, 10, 9, 8, 7, 6],
        another_immediate_number=[5, 4, 3, 2, 1, 0]
    )

    __LCS_RR = INTEGER(
        "integer",
        "LCS",
        [1, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0],
        source_register=[11, 10, 9, 8, 7, 6],
        another_source_register=[5, 4, 3, 2, 1, 0]
    )

    __LCS_RI = INTEGER(
        "integer",
        "LCS",
        [1, 0, 0, 0, 0, 1, 0, 0, 0, 0, 1],
        source_register=[11, 10, 9, 8, 7, 6],
        immediate_number=[15, 14, 13, 12, 5, 4, 3, 2, 1, 0]
    )

    __LCS_IR = INTEGER(
        "integer",
        "LCS",
        [1, 0, 0, 0, 0, 1, 0, 0, 0, 1, 0],
        source_register=[11, 10, 9, 8, 7, 6],
        immediate_number=[15, 14, 13, 12, 5, 4, 3, 2, 1, 0]
    )

    __LCS_II = INTEGER(
        "integer",
        "LCS",
        [1, 0, 0, 0, 0, 1, 0, 0, 0, 1, 1],
        immediate_number=[15, 14, 13, 12, 11, 10, 9, 8, 7, 6],
        another_immediate_number=[5, 4, 3, 2, 1, 0]
    )

    __GT_RR = BRANCH(
        "branch",
        "GT",
        [1, 0, 0, 1, 0, 0, 0, 0, 0, 0],
        source_register=[11, 10, 9, 8, 7, 6],
        another_source_register=[5, 4, 3, 2, 1, 0]
    )

    __GT_RI = BRANCH(
        "branch",
        "GT",
        [1, 0, 0, 1, 0, 0, 0, 0, 0, 1],
        source_register=[11, 10, 9, 8, 7, 6],
        immediate_number=[15, 14, 13, 12, 11, 10, 9, 8, 7, 6]
    )

    __EQ_RR = BRANCH(
        "branch",
        "EQ",
        [1, 0, 0, 1, 0, 0, 0, 0, 1, 0],
        source_register=[11, 10, 9, 8, 7, 6],
        another_source_register=[5, 4, 3, 2, 1, 0]
    )

    __EQ_RI = BRANCH(
        "branch",
        "EQ",
        [1, 0, 0, 1, 0, 0, 0, 0, 1, 1],
        source_register=[11, 10, 9, 8, 7, 6],
        immediate_number=[15, 14, 13, 12, 11, 10, 9, 8, 7, 6]
    )

    __LT_RR = BRANCH(
        "branch",
        "LT",
        [1, 0, 0, 1, 0, 0, 0, 1, 0, 0],
        source_register=[11, 10, 9, 8, 7, 6],
        another_source_register=[5, 4, 3, 2, 1, 0]
    )

    __LT_RI = BRANCH(
        "branch",
        "LT",
        [1, 0, 0, 1, 0, 0, 0, 1, 0, 1],
        source_register=[11, 10, 9, 8, 7, 6],
        immediate_number=[15, 14, 13, 12, 11, 10, 9, 8, 7, 6]
    )

    __GTE_RR = BRANCH(
        "branch",
        "GTE",
        [1, 0, 0, 1, 0, 0, 0, 1, 1, 0],
        source_register=[11, 10, 9, 8, 7, 6],
        another_source_register=[5, 4, 3, 2, 1, 0]
    )

    __GTE_RI = BRANCH(
        "branch",
        "GTE",
        [1, 0, 0, 1, 0, 0, 0, 1, 1, 1],
        source_register=[11, 10, 9, 8, 7, 6],
        immediate_number=[15, 14, 13, 12, 11, 10, 9, 8, 7, 6]
    )

    __LTE_RR = BRANCH(
        "branch",
        "LTE",
        [1, 0, 0, 1, 0, 0, 1, 0, 0, 0],
        source_register=[11, 10, 9, 8, 7, 6],
        another_source_register=[5, 4, 3, 2, 1, 0]
    )

    __LTE_RI = BRANCH(
        "branch",
        "LTE",
        [1, 0, 0, 1, 0, 0, 1, 0, 0, 1],
        source_register=[11, 10, 9, 8, 7, 6],
        immediate_number=[15, 14, 13, 12, 11, 10, 9, 8, 7, 6]
    )

    __JMP_I = JUMP(
        "jump",
        "JMP",
        [1, 1, 0, 0, 0, 0, 0, 0, 0, 0],
        immediate_number=[21, 20, 19, 18, 17, 16, 15, 14, 13, 12, 11,
                          10, 9, 8, 7, 6, 5, 4, 3, 2, 1, 0]
    )

    __JMP_R = JUMP(
        "jump",
        "JMP",
        [1, 1, 0, 0, 0, 0, 0, 0, 0, 1],
        first_source_register=[11, 10, 9, 8, 7, 6],
        second_source_register=[5, 4, 3, 2, 1, 0]
    )

    __OJMP_I = JUMP(
        "jump",
        "OJMP",
        [1, 1, 0, 0, 0, 0, 0, 0, 1, 0],
        immediate_number=[21, 20, 19, 18, 17, 16, 15, 14, 13, 12, 11,
                          10, 9, 8, 7, 6, 5, 4, 3, 2, 1, 0]
    )

    __OJMP_R = JUMP(
        "jump",
        "OJMP",
        [1, 1, 0, 0, 0, 0, 0, 0, 1, 1],
        first_source_register=[11, 10, 9, 8, 7, 6],
        second_source_register=[5, 4, 3, 2, 1, 0]
    )

    __ZJMP_I = JUMP(
        "jump",
        "ZJMP",
        [1, 1, 0, 0, 0, 0, 0, 1, 0, 0],
        immediate_number=[21, 20, 19, 18, 17, 16, 15, 14, 13, 12, 11,
                          10, 9, 8, 7, 6, 5, 4, 3, 2, 1, 0]
    )

    __ZJMP_R = JUMP(
        "jump",
        "ZJMP",
        [1, 1, 0, 0, 0, 0, 0, 1, 0, 1],
        first_source_register=[11, 10, 9, 8, 7, 6],
        second_source_register=[5, 4, 3, 2, 1, 0]
    )

    __NOP = Instruction(
        "others",
        "NOP",
        [1, 1, 0, 0, 0, 0, 0, 1, 1, 0]
    )

    def __inst__(self):
        pass
