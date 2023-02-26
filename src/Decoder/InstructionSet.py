from typing import List
from DecoderExceptions import OperateCodeLenthError, \
    RegisterLabelBitsCrowdedError, \
    InstructionLenthError, \
    RegisterLabelLenthError, \
    NoThisRegisterError, \
    ImmediateNumberBitsCrowdedError, \
    NotThisInstructionError, \
    InvalidBitValueError


class Instruction:
    i_type = ""
    i_name = ""

    op_code = []

    __inst_lenth = 32
    __op_code_bits = [31, 30, 29, 28, 27, 26, 25, 24]
    __register_label_bit_lenth = 6
    __unused_bit = 0

    __check_flag = [False for _ in range(__inst_lenth)]

    def __init__(
        self,
        instruction_type: str = "",
        instruction_name: str = "",
        op_code: List[int] = [0, 0, 0, 0, 0, 0, 0, 0]
    ):
        self.i_type = instruction_type
        self.i_name = instruction_name
        self.op_code = op_code

    def __checkOPCodeLenth(self):
        if len(self.op_code) != 10:
            raise OperateCodeLenthError(len(self.__op_code_bits))

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


class LOAD(Instruction):
    __tartget_regerter_bits = []
    __immediate_number_bits = []
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
            op_code=op_code
        )

        self.__tartget_regerter_bits = target_register
        self.__immediate_number_bits = immediate_number
        self.__fsource_register_bits = first_source_register
        self.__ssource_register_bits = second_source_register

        self.__checkInstructionIntegrity()

    def __checkInstructionIntegrity(self):
        self.__checkOPCodeLenth()
        self.__checkTargetRegister()

        for i in self.__op_code_bits:
            self.check_flag[self.__inst_lenth - 1 - i] = True

        for i in self.__tartget_regerter_bits:
            if self.check_flag[self.__inst_lenth - 1 - i]:
                raise RegisterLabelBitsCrowdedError("target register")
            else:
                self.check_flag[self.__inst_lenth - 1 - i] = True

        try:
            self.__checkFirstSourceRegister()
        except NoThisRegisterError:
            pass
        except Exception as e:
            raise e
        else:
            for i in self.__fsource_register_bits:
                if self.check_flag[self.__inst_lenth - 1 - i]:
                    raise RegisterLabelBitsCrowdedError(
                        "first source register",
                        i
                    )
                else:
                    self.check_flag[self.__inst_lenth - 1 - i] = True

        try:
            self.__checkSecondSourceRegister()
        except NoThisRegisterError:
            pass
        except Exception as e:
            raise e
        else:
            for i in self.__fsource_register_bits:
                if self.check_flag[self.__inst_lenth - 1 - i]:
                    raise RegisterLabelBitsCrowdedError(
                        "second source register",
                        i
                    )
                else:
                    self.check_flag[self.__inst_lenth - 1 - i] = True

        if not self.__immediate_number_bits:
            pass
        else:
            for i in self.__immediate_number_bits:
                if self.check_flag[self.__inst_lenth - 1 - i]:
                    raise ImmediateNumberBitsCrowdedError(i)

    def __checkTargetRegister(self):
        if len(self.__tartget_regerter_bits) \
                != self.__register_label_bit_lenth:
            raise RegisterLabelLenthError(self.__register_label_bit_lenth)

    def __checkFirstSourceRegister(self):
        if not self.__fsource_register_bits:
            raise NoThisRegisterError("first source register")
        elif len(self.__fsource_register_bits) \
                != self.__register_label_bit_lenth:
            raise RegisterLabelLenthError(
                self.__register_label_bit_lenth,
                "first source registr"
            )

    def __checkSecondSourceRegister(self):
        if not self.__ssource_register_bits:
            raise NoThisRegisterError("second source register")
        elif len(self.__ssource_register_bits) \
                != self.__register_label_bit_lenth:
            raise RegisterLabelLenthError(
                self.__register_label_bit_lenth,
                "second source registr"
            )


class STORE(Instruction):
    __source_regerter_bits = []
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
            op_code=op_code
        )

        self.__source_regerter_bits = source_register
        self.__ftarget_register_bits = first_target_register
        self.__starget_register_bits = second_target_register

        self.__checkInstructionIntegrity()

    def __checkInstructionIntegrity(self):
        self.__checkOPCodeLenth()
        self.__checkSourceRegister()

        for i in self.__op_code_bits:
            self.check_flag[self.__inst_lenth - 1 - i] = True

        for i in self.__source_regerter_bits:
            if self.check_flag[self.__inst_lenth - 1 - i]:
                raise RegisterLabelBitsCrowdedError("source register")
            else:
                self.check_flag[self.__inst_lenth - 1 - i] = True

        try:
            self.__checkFirstTargetRegister()
        except NoThisRegisterError:
            pass
        except Exception as e:
            raise e
        else:
            for i in self.__fsource_register_bits:
                if self.check_flag[self.__inst_lenth - 1 - i]:
                    raise RegisterLabelBitsCrowdedError(
                        "first target register",
                        i
                    )
                else:
                    self.check_flag[self.__inst_lenth - 1 - i] = True

        try:
            self.__checkSecondTargetRegister()
        except NoThisRegisterError:
            pass
        except Exception as e:
            raise e
        else:
            for i in self.__fsource_register_bits:
                if self.check_flag[self.__inst_lenth - 1 - i]:
                    raise RegisterLabelBitsCrowdedError(
                        "second target register",
                        i
                    )
                else:
                    self.check_flag[self.__inst_lenth - 1 - i] = True

    def __checkSourceRegister(self):
        if len(self.__source_regerter_bits) \
                != self.__register_label_bit_lenth:
            raise RegisterLabelLenthError(self.__register_label_bit_lenth)

    def __checkFirstTargetRegister(self):
        if not self.__ftarget_register_bits:
            raise NoThisRegisterError("first target register")
        elif len(self.__ftarget_register_bits) \
                != self.__register_label_bit_lenth:
            raise RegisterLabelLenthError(
                self.__register_label_bit_lenth,
                "first target registr"
            )

    def __checkSecondTargetRegister(self):
        if not self.__starget_register_bits:
            raise NoThisRegisterError("second target register")
        elif len(self.__starget_register_bits) \
                != self.__register_label_bit_lenth:
            raise RegisterLabelLenthError(
                self.__register_label_bit_lenth,
                "second target registr"
            )


class MOVE(Instruction):
    __source_regerter_bits = []
    __target_register_bits = []

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
            op_code=op_code
        )

        self.__source_regerter_bits = source_register
        self.__target_register_bits = target_register

        self.__checkInstructionIntegrity()

    def __checkInstructionIntegrity(self):
        self.__checkOPCodeLenth()
        self.__checkSourceRegister()
        self.__checkTargetRegister()

    def __checkSourceRegister(self):
        if len(self.__source_regerter_bits) \
                != self.__register_label_bit_lenth:
            raise RegisterLabelLenthError(self.__register_label_bit_lenth)

    def __checkTargetRegister(self):
        if len(self.__target_regerter_bits) \
                != self.__register_label_bit_lenth:
            raise RegisterLabelLenthError(self.__register_label_bit_lenth)


class INTEGER(Instruction):
    __target_register_bits = []
    __immediate_number_bits = []
    __fsource_regerter_bits = []
    __ssource_regerter_bits = []

    def __init__(
        self,
        instruction_type: str = "",
        instruction_name: str = "",
        op_code: List[int] = [0, 0, 0, 0, 0, 0, 0, 0],
        target_register: List[int] = [21, 20, 19, 18, 17, 16],
        first_source_register: List[int] = [5, 4, 3, 2, 1, 0],
        immediate_number: List[int] = []
        # TODO finish here
    ):
        super().__init__(
            instruction_type=instruction_type,
            instruction_name=instruction_name,
            op_code=op_code
        )

        self.__fsource_regerter_bits = first_source_register
        self.__target_register_bits = target_register

        self.__checkInstructionIntegrity()

    def __checkInstructionIntegrity(self):
        self.__checkOPCodeLenth()
        self.__checkSourceRegister()
        self.__checkTargetRegister()

    def __checkSourceRegister(self):
        if len(self.__source_regerter_bits) \
                != self.__register_label_bit_lenth:
            raise RegisterLabelLenthError(self.__register_label_bit_lenth)

    def __checkTargetRegister(self):
        if len(self.__target_regerter_bits) \
                != self.__register_label_bit_lenth:
            raise RegisterLabelLenthError(self.__register_label_bit_lenth)


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

    def __inst__(self):
        pass
