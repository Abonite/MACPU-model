from typing import List
from DecoderExceptions import OperateCodeLenthError, \
    RegisterLabelBitsCrowdedError, InstructionLenthError, \
    RegisterLabelLenthError, ImmediateNumberBitsCrowdedError, \
    NotThisInstructionError, InvalidBitValueError, \
    RegisterNotBeAllowedError


class Instruction:
    i_type = ""
    i_name = ""

    op_code = []

    source_register_bits = []
    target_register_bits = []
    immediate_number_bits = []

    source_register_allowed = []
    target_register_allowed = []

    inst_lenth = 32
    op_code_bits = [31, 30, 29, 28, 27, 26, 25, 24, 23, 22]
    register_label_bit_lenth = 6
    unused_bit = 0

    def __init__(
        self,
        instruction_type: str = "",
        instruction_name: str = "",
        op_code: List[int] = [0, 0, 0, 0, 0, 0, 0, 0],
        source_register_bits: List[int] = [],
        target_register_bits: List[int] = [],
        immediate_number: List[int] = [],
        source_register_allowed: List[int] = [],
        target_register_allowed: List[int] = []
    ):
        self.i_type = instruction_type
        self.i_name = instruction_name
        self.op_code = op_code
        self.immediate_number_bits = immediate_number
        self.source_register_bits = source_register_bits
        self.target_register_bits = target_register_bits
        self.target_register_allowed = target_register_allowed
        self.source_register_allowed = source_register_allowed

        self.check_flag = [False for _ in range(self.inst_lenth)]

    def checkOPCode(self):
        if len(self.op_code) != 10:
            raise OperateCodeLenthError(len(self.op_code_bits))
        else:
            for i in self.op_code_bits:
                self.check_flag[self.inst_lenth - 1 - i] = True

    def checkImmediateNumber(self):
        if not self.immediate_number_bits:
            return
        else:
            for i in self.immediate_number_bits:
                if self.check_flag[self.inst_lenth - 1 - i]:
                    raise ImmediateNumberBitsCrowdedError(i)
                else:
                    self.check_flag[self.inst_lenth - 1 - i] = True

    def isItThisInstruction(self, inst: List[int]):
        if len(inst) != self.inst_lenth:
            raise InstructionLenthError(self.inst_lenth)
        else:
            if [inst[self.inst_lenth - 1 - x] for x in self.op_code_bits] \
                    == self.op_code:
                i = 0
                for f, b in zip(self.check_flag, inst):
                    if f:
                        pass
                    else:
                        if b == self.unused_bit:
                            pass
                        else:
                            raise InvalidBitValueError(
                                self.i_name,
                                self.inst_lenth - 1 - i,
                                self.unused_bit
                            )
                    i += 1
            else:
                raise NotThisInstructionError(self.i_name)

    def checkSourceRegister(self):
        if not self.source_register_bits:
            return
        elif len(self.source_register_bits) \
                != self.register_label_bit_lenth:
            raise RegisterLabelLenthError(self.register_label_bit_lenth)
        else:
            for i in self.source_register_bits:
                if self.check_flag[self.inst_lenth - 1 - i]:
                    raise RegisterLabelBitsCrowdedError("source register", i)
                else:
                    self.check_flag[self.inst_lenth - 1 - i] = True

    def checkSourceRegisterIsAllowed(self, inst: List[int]):
        if not self.source_register_bits:
            return
        elif [
            inst[self.inst_lenth - i - 1] for i in self.source_register_bits
        ] not in self.source_register_allowed:
            raise RegisterNotBeAllowedError(self.i_name, "source register")

    def checkTargetRegisterIsAllowed(self, inst: List[int]):
        if not self.source_register_bits:
            return
        elif [
            inst[self.inst_lenth - i - 1] for i in self.target_register_bits
        ] not in self.target_register_allowed:
            raise RegisterNotBeAllowedError(self.i_name, "target register")

    def checkTargetRegister(self):
        if not self.target_register_bits:
            return
        elif len(self.target_register_bits) \
                != self.register_label_bit_lenth:
            raise RegisterLabelLenthError(self.register_label_bit_lenth)
        else:
            for i in self.target_register_bits:
                if self.check_flag[self.inst_lenth - 1 - i]:
                    raise RegisterLabelBitsCrowdedError("target register", i)
                else:
                    self.check_flag[self.inst_lenth - 1 - i] = True


class LOAD(Instruction):
    fsource_register_bits = []
    ssource_register_bits = []
    fsource_register_allowed = []
    ssource_register_allowed = []

    def __init__(
        self,
        instruction_type: str = "",
        instruction_name: str = "",
        op_code: List[int] = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        target_register: List[int] = [21, 20, 19, 18, 17, 16],
        immediate_number: List[int] = [],
        first_source_register: List[int] = [],
        second_source_register: List[int] = [],
        target_register_allowed: List[int] = [],
        first_source_register_allowed: List[int] = [],
        second_source_register_allowed: List[int] = []
    ):
        super().__init__(
            instruction_type=instruction_type,
            instruction_name=instruction_name,
            op_code=op_code,
            immediate_number=immediate_number,
            target_register_bits=target_register,
            target_register_allowed=target_register_allowed
        )

        self.fsource_register_bits = first_source_register
        self.ssource_register_bits = second_source_register

        self.fsource_register_allowed = first_source_register_allowed
        self.ssource_register_allowed = second_source_register_allowed

        self.checkInstructionIntegrity()

    def checkInstructionIntegrity(self):
        self.checkOPCode()
        self.checkTargetRegister()
        self.checkFirstSourceRegister()
        self.checkSecondSourceRegister()
        self.checkImmediateNumber()

    def checkFirstSourceRegister(self):
        if not self.fsource_register_bits:
            return
        elif len(self.fsource_register_bits) \
                != self.register_label_bit_lenth:
            raise RegisterLabelLenthError(
                self.register_label_bit_lenth,
                "first source registr"
            )
        else:
            for i in self.fsource_register_bits:
                if self.check_flag[self.inst_lenth - 1 - i]:
                    raise RegisterLabelBitsCrowdedError(
                        "first source register",
                        i
                    )
                else:
                    self.check_flag[self.inst_lenth - 1 - i] = True

    def checkSecondSourceRegister(self):
        if not self.ssource_register_bits:
            return
        elif len(self.ssource_register_bits) \
                != self.register_label_bit_lenth:
            raise RegisterLabelLenthError(
                self.register_label_bit_lenth,
                "second source registr"
            )
        else:
            for i in self.ssource_register_bits:
                if self.check_flag[self.inst_lenth - 1 - i]:
                    raise RegisterLabelBitsCrowdedError(
                        "second source register",
                        i
                    )
                else:
                    self.check_flag[self.inst_lenth - 1 - i] = True

    def checkFirstSourceRegisterIsAllowed(self, inst: List[int]):
        if not self.fsource_register_bits:
            return
        elif [
            inst[self.inst_lenth - i - 1] for i in self.fsource_register_bits
        ] not in self.fsource_register_allowed:
            raise RegisterNotBeAllowedError(
                self.i_name,
                "first source register"
            )

    def checkSecondSourceRegisterIsAllowed(self, inst: List[int]):
        if not self.ssource_register_bits:
            return
        elif [
            inst[self.inst_lenth - i - 1] for i in self.ssource_register_bits
        ] not in self.ssource_register_allowed:
            raise RegisterNotBeAllowedError(
                self.i_name,
                "second source register"
            )


class STORE(Instruction):
    ftarget_register_bits = []
    starget_register_bits = []
    ftarget_register_allowed = []
    starget_register_allowed = []

    def __init__(
        self,
        instruction_type: str = "",
        instruction_name: str = "",
        op_code: List[int] = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        source_register: List[int] = [21, 20, 19, 18, 17, 16],
        first_target_register: List[int] = [],
        second_target_register: List[int] = [],
        source_register_allowed: List[int] = [],
        first_target_register_allowed: List[int] = [],
        second_target_register_allowed: List[int] = []
    ):
        super().__init__(
            instruction_type=instruction_type,
            instruction_name=instruction_name,
            op_code=op_code,
            source_register_bits=source_register,
            source_register_allowed=source_register_allowed
        )

        self.ftarget_register_bits = first_target_register
        self.starget_register_bits = second_target_register
        self.ftarget_register_allowed = first_target_register_allowed
        self.starget_register_allowed = second_target_register_allowed

        self.checkInstructionIntegrity()

    def checkInstructionIntegrity(self):
        self.checkOPCode()
        self.checkSourceRegister()
        self.checkFirstTargetRegister()
        self.checkSecondTargetRegister()

    def checkFirstTargetRegister(self):
        if not self.ftarget_register_bits:
            return
        elif len(self.ftarget_register_bits) \
                != self.register_label_bit_lenth:
            raise RegisterLabelLenthError(
                self.register_label_bit_lenth,
                "first target registr"
            )
        else:
            for i in self.ftarget_register_bits:
                if self.check_flag[self.inst_lenth - 1 - i]:
                    raise RegisterLabelBitsCrowdedError(
                        "first target register",
                        i
                    )
                else:
                    self.check_flag[self.inst_lenth - 1 - i] = True

    def checkSecondTargetRegister(self):
        if not self.starget_register_bits:
            return
        elif len(self.starget_register_bits) \
                != self.register_label_bit_lenth:
            raise RegisterLabelLenthError(
                self.register_label_bit_lenth,
                "second target registr"
            )
        else:
            for i in self.starget_register_bits:
                if self.check_flag[self.inst_lenth - 1 - i]:
                    raise RegisterLabelBitsCrowdedError(
                        "second target register",
                        i
                    )
                else:
                    self.check_flag[self.inst_lenth - 1 - i] = True

    def checkFirstTargetRegisterIsAllowed(self, inst: List[int]):
        if not self.ftarget_register_bits:
            return
        elif [
            inst[self.inst_lenth - i - 1] for i in self.ftarget_register_bits
        ] not in self.ftarget_register_allowed:
            raise RegisterNotBeAllowedError(
                self.i_name,
                "first target register"
            )

    def checkSecondTargetRegisterIsAllowed(self, inst: List[int]):
        if not self.source_register_bits:
            return
        elif [
            inst[self.inst_lenth - i - 1] for i in self.starget_register_bits
        ] not in self.starget_register_allowed:
            raise RegisterNotBeAllowedError(
                self.i_name,
                "second target register"
            )


class MOVE(Instruction):
    def __init__(
        self,
        instruction_type: str = "",
        instruction_name: str = "",
        op_code: List[int] = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        source_register: List[int] = [5, 4, 3, 2, 1, 0],
        target_register: List[int] = [21, 20, 19, 18, 17, 16],
        source_register_allowed: List[int] = [],
        target_register_allowed: List[int] = []
    ):
        super().__init__(
            instruction_type=instruction_type,
            instruction_name=instruction_name,
            op_code=op_code,
            source_register_bits=source_register,
            target_register_bits=target_register,
            source_register_allowed=source_register_allowed,
            target_register_allowed=target_register_allowed
        )

        self.checkInstructionIntegrity()

    def checkInstructionIntegrity(self):
        self.checkOPCode()
        self.checkSourceRegister()
        self.checkTargetRegister()


class INTEGER(Instruction):
    asource_register_bits = []
    aimmediate_number_bits = []
    asource_register_allowed = []

    def __init__(
        self,
        instruction_type: str = "",
        instruction_name: str = "",
        op_code: List[int] = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        target_register: List[int] = [21, 20, 19, 18, 17, 16],
        source_register: List[int] = [],
        another_source_register: List[int] = [],
        immediate_number: List[int] = [],
        target_register_allowed: List[int] = [],
        source_register_allowed: List[int] = [],
        another_immediate_number: List[int] = [],
        another_source_register_allowed: List[int] = []
    ):
        super().__init__(
            instruction_type=instruction_type,
            instruction_name=instruction_name,
            op_code=op_code,
            target_register_bits=target_register,
            source_register_bits=source_register,
            immediate_number=immediate_number,
            target_register_allowed=target_register_allowed,
            source_register_allowed=source_register_allowed
        )

        self.asource_register_bits = another_source_register
        self.aimmediate_number_bits = another_immediate_number
        self.asource_register_allowed = another_source_register_allowed

        self.checkInstructionIntegrity()

    def checkInstructionIntegrity(self):
        self.checkOPCode()
        self.checkSourceRegister()
        self.checkTargetRegister()
        self.checkASourceRegister()
        self.checkImmediateNumber()
        self.checkAImmediateNumber()

    def checkASourceRegister(self):
        if not self.asource_register_bits:
            return
        elif len(self.asource_register_bits) \
                != self.register_label_bit_lenth:
            raise RegisterLabelLenthError(
                self.register_label_bit_lenth,
                "another source register"
            )
        else:
            for i in self.asource_register_bits:
                if self.check_flag[self.inst_lenth - 1 - i]:
                    raise RegisterLabelBitsCrowdedError(
                        "another source register",
                        i
                    )
                else:
                    self.check_flag[self.inst_lenth - 1 - i] = True

    def checkAImmediateNumber(self):
        if not self.aimmediate_number_bits:
            return
        else:
            for i in self.aimmediate_number_bits:
                if self.check_flag[self.inst_lenth - 1 - i]:
                    raise ImmediateNumberBitsCrowdedError(i)
                else:
                    self.check_flag[self.inst_lenth - 1 - i] = True

    def checkASoureceRegisterIsAllowed(self, inst: List[int]):
        if not self.asource_register_bits:
            return
        elif [
            inst[self.inst_lenth - i - 1] for i in self.asource_register_bits
        ] not in self.asourece_register_allowed:
            raise RegisterNotBeAllowedError(
                self.i_name,
                "another source register"
            )


class BRANCH(Instruction):
    asource_register_bits = []
    asource_register_allowed = []

    def __init__(
        self,
        instruction_type: str = "",
        instruction_name: str = "",
        op_code: List[int] = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        target_register: List[int] = [21, 20, 19, 18, 17, 16],
        source_register: List[int] = [11, 10, 9, 8, 7, 6],
        another_source_register: List[int] = [],
        immediate_number: List[int] = [],
        target_register_allowed: List[int] = [],
        source_register_allowed: List[int] = [],
        asource_register_allowed: List[int] = []
    ):
        super().__init__(
            instruction_type=instruction_type,
            instruction_name=instruction_name,
            op_code=op_code,
            target_register_bits=target_register,
            source_register_bits=source_register,
            immediate_number=immediate_number,
            target_register_allowed=target_register_allowed,
            source_register_allowed=source_register_allowed,
        )

        self.asource_register_bits = another_source_register
        self.asource_register_allowed = asource_register_allowed

        self.checkInstructionIntegrity()

    def checkInstructionIntegrity(self):
        self.checkOPCode()
        self.checkSourceRegister()
        self.checkTargetRegister()
        self.checkASourceRegister()
        self.checkImmediateNumber()

    def checkASourceRegister(self):
        if not self.asource_register_bits:
            return
        elif len(self.asource_register_bits) \
                != self.register_label_bit_lenth:
            raise RegisterLabelLenthError(
                self.register_label_bit_lenth,
                "another source register"
            )
        else:
            for i in self.asource_register_bits:
                if self.check_flag[self.inst_lenth - 1 - i]:
                    raise RegisterLabelBitsCrowdedError(
                        "another source register",
                        i
                    )
                else:
                    self.check_flag[self.inst_lenth - 1 - i] = True

    def checkASoureceRegisterIsAllowed(self, inst: List[int]):
        if not self.asource_register_bits:
            return
        elif [
            inst[self.inst_lenth - i - 1] for i in self.asource_register_bits
        ] not in self.asourece_register_allowed:
            raise RegisterNotBeAllowedError(
                self.i_name,
                "another source register"
            )


class JUMP(Instruction):
    fsource_register_bits = []
    ssource_register_bits = []
    fsource_register_allowed = []
    ssource_register_allowed = []

    def __init__(
        self,
        instruction_type: str = "",
        instruction_name: str = "",
        op_code: List[int] = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        first_source_register: List[int] = [],
        second_source_register: List[int] = [],
        immediate_number: List[int] = [],
        first_source_register_allowed: List[int] = [],
        second_source_register_allowed: List[int] = []
    ):
        super().__init__(
            instruction_type=instruction_type,
            instruction_name=instruction_name,
            op_code=op_code,
            immediate_number=immediate_number
        )

        self.fsource_register_bits = first_source_register
        self.ssource_register_bits = second_source_register
        self.fsource_register_allowed = first_source_register_allowed
        self.ssource_register_allowed = second_source_register_allowed

        self.checkInstructionIntegrity()

    def checkInstructionIntegrity(self):
        self.checkOPCode()
        self.checkFirstSourceRegister()
        self.checkSecondSourceRegister()

    def checkFirstSourceRegister(self):
        if not self.fsource_register_bits:
            return
        elif len(self.fsource_register_bits) \
                != self.register_label_bit_lenth:
            raise RegisterLabelLenthError(
                self.register_label_bit_lenth,
                "first source registr"
            )
        else:
            for i in self.fsource_register_bits:
                if self.check_flag[self.inst_lenth - 1 - i]:
                    raise RegisterLabelBitsCrowdedError(
                        "first source register",
                        i
                    )
                else:
                    self.check_flag[self.inst_lenth - 1 - i] = True

    def checkSecondSourceRegister(self):
        if not self.ssource_register_bits:
            return
        elif len(self.ssource_register_bits) \
                != self.register_label_bit_lenth:
            raise RegisterLabelLenthError(
                self.register_label_bit_lenth,
                "second source registr"
            )
        else:
            for i in self.ssource_register_bits:
                if self.check_flag[self.inst_lenth - 1 - i]:
                    raise RegisterLabelBitsCrowdedError(
                        "second source register",
                        i
                    )
                else:
                    self.check_flag[self.inst_lenth - 1 - i] = True

    def checkFirstSourceRegisterIsAllowed(self, inst: List[int]):
        if not self.fsource_register_bits:
            return
        elif [
            inst[self.inst_lenth - i - 1] for i in self.fsource_register_bits
        ] not in self.fsource_register_allowed:
            raise RegisterNotBeAllowedError(
                self.i_name,
                "first source register"
            )

    def checkSecondSourceRegisterIsAllowed(self, inst: List[int]):
        if not self.ssource_register_bits:
            return
        elif [
            inst[self.inst_lenth - i - 1] for i in self.ssource_register_bits
        ] not in self.ssource_register_allowed:
            raise RegisterNotBeAllowedError(
                self.i_name,
                "second source register"
            )


class Instrucitons:
    LOAD8_IR = LOAD(
        "memory",
        "LOAD8",
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
        immediate_number=[7, 6, 5, 4, 3, 2, 1, 0]
    )

    LOAD8_RR = LOAD(
        "memory",
        "LOAD8",
        [0, 0, 0, 0, 0, 0, 0, 0, 1, 0],
        first_source_register=[11, 10, 9, 8, 7, 6],
        second_source_register=[5, 4, 3, 2, 1, 0]
    )

    LOAD16_IR = LOAD(
        "memory",
        "LOAD16",
        [0, 0, 0, 0, 0, 0, 0, 0, 1, 1],
        immediate_number=[15, 14, 13, 12, 11, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1, 0]
    )

    LOAD16_RR = LOAD(
        "memory",
        "LOAD16",
        [0, 0, 0, 0, 0, 0, 0, 1, 0, 0],
        first_source_register=[11, 10, 9, 8, 7, 6],
        second_source_register=[5, 4, 3, 2, 1, 0]
    )

    LOAD32 = LOAD(
        "memory",
        "LOAD32",
        [0, 0, 0, 0, 0, 0, 0, 1, 0, 1],
        first_source_register=[11, 10, 9, 8, 7, 6],
        second_source_register=[5, 4, 3, 2, 1, 0]
    )

    STORE8 = STORE(
        "memory",
        "STORE8",
        [0, 0, 0, 0, 0, 0, 0, 1, 0, 1],
        first_target_register=[11, 10, 9, 8, 7, 6],
        second_target_register=[5, 4, 3, 2, 1, 0]
    )

    STORE16 = STORE(
        "memory",
        "STORE16",
        [0, 0, 0, 0, 0, 0, 0, 1, 1, 0],
        first_target_register=[11, 10, 9, 8, 7, 6],
        second_target_register=[5, 4, 3, 2, 1, 0]
    )

    STORE32 = STORE(
        "memory",
        "STORE32",
        [0, 0, 0, 0, 0, 0, 0, 1, 1, 1],
        first_target_register=[11, 10, 9, 8, 7, 6],
        second_target_register=[5, 4, 3, 2, 1, 0]
    )

    MOVE = MOVE(
        "register",
        "MOVE",
        [0, 0, 0, 0, 0, 0, 1, 0, 0, 1]
    )

    ADD_RR = INTEGER(
        "integer",
        "ADD",
        [1, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        another_source_register=[5, 4, 3, 2, 1, 0]
    )

    ADD_IR = INTEGER(
        "integer",
        "ADD",
        [1, 0, 0, 0, 0, 0, 0, 0, 0, 1],
        immediate_number=[15, 14, 13, 12, 5, 4, 3, 2, 1, 0]
    )

    SUB_RR = INTEGER(
        "integer",
        "SUB",
        [1, 0, 0, 0, 0, 0, 0, 0, 1, 0],
        another_source_register=[5, 4, 3, 2, 1, 0]
    )

    SUB_RI = INTEGER(
        "integer",
        "SUB",
        [1, 0, 0, 0, 0, 0, 0, 0, 1, 1],
        immediate_number=[15, 14, 13, 12, 5, 4, 3, 2, 1, 0]
    )

    SUB_IR = INTEGER(
        "integer",
        "SUB",
        [1, 0, 0, 0, 0, 0, 0, 1, 0, 0],
        immediate_number=[15, 14, 13, 12, 5, 4, 3, 2, 1, 0]
    )

    BAND_RR = INTEGER(
        "integer",
        "BAND",
        [1, 0, 0, 0, 0, 0, 0, 1, 0, 1],
        another_source_register=[5, 4, 3, 2, 1, 0]
    )

    BAND_IR = INTEGER(
        "integer",
        "BAND",
        [1, 0, 0, 0, 0, 0, 0, 1, 1, 0],
        immediate_number=[15, 14, 13, 12, 5, 4, 3, 2, 1, 0]
    )

    BOR_RR = INTEGER(
        "integer",
        "BOR",
        [1, 0, 0, 0, 0, 0, 0, 1, 1, 0],
        another_source_register=[5, 4, 3, 2, 1, 0]
    )

    BOR_IR = INTEGER(
        "integer",
        "BOR",
        [1, 0, 0, 0, 0, 0, 0, 1, 1, 1],
        immediate_number=[15, 14, 13, 12, 5, 4, 3, 2, 1, 0]
    )

    BNOT_R = INTEGER(
        "integer",
        "BNOT",
        [1, 0, 0, 0, 0, 0, 1, 0, 0, 0],
        source_register=[],
        another_source_register=[5, 4, 3, 2, 1, 0]
    )

    BNOT_I = INTEGER(
        "integer",
        "BNOT",
        [1, 0, 0, 0, 0, 0, 1, 0, 0, 1],
        immediate_number=[15, 14, 13, 12, 11, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1, 0]
    )

    BXOR_RR = INTEGER(
        "integer",
        "BOR",
        [1, 0, 0, 0, 0, 0, 1, 0, 1, 0],
        another_source_register=[5, 4, 3, 2, 1, 0]
    )

    BXOR_IR = INTEGER(
        "integer",
        "BOR",
        [1, 0, 0, 0, 0, 0, 1, 0, 1, 1],
        immediate_number=[15, 14, 13, 12, 5, 4, 3, 2, 1, 0]
    )

    RAND = INTEGER(
        "integer",
        "RAND",
        [1, 0, 0, 0, 0, 0, 1, 1, 0, 0],
    )

    ROR = INTEGER(
        "integer",
        "ROR",
        [1, 0, 0, 0, 0, 0, 1, 1, 0, 1],
    )

    RXOR = INTEGER(
        "integer",
        "RXOR",
        [1, 0, 0, 0, 0, 0, 1, 1, 1, 0],
    )

    MUL_RR = INTEGER(
        "integer",
        "MUL",
        [1, 0, 0, 0, 0, 0, 1, 1, 1, 1],
        another_source_register=[5, 4, 3, 2, 1, 0]
    )

    MUL_RI = INTEGER(
        "integer",
        "MUL",
        [1, 0, 0, 0, 0, 1, 0, 0, 0, 0],
        immediate_number=[15, 14, 13, 12, 5, 4, 3, 2, 1, 0]
    )

    DIV_RR = INTEGER(
        "integer",
        "DIV",
        [1, 0, 0, 0, 0, 1, 0, 0, 0, 1],
        another_source_register=[5, 4, 3, 2, 1, 0]
    )

    DIV_RI = INTEGER(
        "integer",
        "DIV",
        [1, 0, 0, 0, 0, 1, 0, 0, 1, 0],
        immediate_number=[15, 14, 13, 12, 5, 4, 3, 2, 1, 0]
    )

    DIV_IR = INTEGER(
        "integer",
        "DIV",
        [1, 0, 0, 0, 0, 1, 0, 0, 1, 1],
        immediate_number=[15, 14, 13, 12, 5, 4, 3, 2, 1, 0]
    )

    LS_RR = INTEGER(
        "integer",
        "LS",
        [1, 0, 0, 0, 0, 1, 0, 1, 0, 0],
        source_register=[11, 10, 9, 8, 7, 6],
        another_source_register=[5, 4, 3, 2, 1, 0]
    )

    LS_RI = INTEGER(
        "integer",
        "LS",
        [1, 0, 0, 0, 0, 1, 0, 1, 0, 1],
        source_register=[11, 10, 9, 8, 7, 6],
        immediate_number=[15, 14, 13, 12, 5, 4, 3, 2, 1, 0]
    )

    LS_IR = INTEGER(
        "integer",
        "LS",
        [1, 0, 0, 0, 0, 1, 0, 1, 1, 0],
        source_register=[11, 10, 9, 8, 7, 6],
        immediate_number=[15, 14, 13, 12, 5, 4, 3, 2, 1, 0]
    )

    LS_II = INTEGER(
        "integer",
        "LS",
        [1, 0, 0, 0, 0, 1, 0, 1, 1, 1],
        immediate_number=[15, 14, 13, 12, 11, 10, 9, 8, 7, 6],
        another_immediate_number=[5, 4, 3, 2, 1, 0]
    )

    LRS_RR = INTEGER(
        "integer",
        "LRS",
        [1, 0, 0, 0, 0, 1, 1, 0, 0, 0],
        source_register=[11, 10, 9, 8, 7, 6],
        another_source_register=[5, 4, 3, 2, 1, 0]
    )

    LRS_RI = INTEGER(
        "integer",
        "LRS",
        [1, 0, 0, 0, 0, 1, 1, 0, 0, 1],
        source_register=[11, 10, 9, 8, 7, 6],
        immediate_number=[15, 14, 13, 12, 5, 4, 3, 2, 1, 0]
    )

    LRS_IR = INTEGER(
        "integer",
        "LRS",
        [1, 0, 0, 0, 0, 1, 1, 0, 1, 0],
        source_register=[11, 10, 9, 8, 7, 6],
        immediate_number=[15, 14, 13, 12, 5, 4, 3, 2, 1, 0]
    )

    LRS_II = INTEGER(
        "integer",
        "LRS",
        [1, 0, 0, 0, 0, 1, 1, 0, 1, 1],
        immediate_number=[15, 14, 13, 12, 11, 10, 9, 8, 7, 6],
        another_immediate_number=[5, 4, 3, 2, 1, 0]
    )

    ARS_RR = INTEGER(
        "integer",
        "ARS",
        [1, 0, 0, 0, 0, 1, 1, 1, 0, 0],
        source_register=[11, 10, 9, 8, 7, 6],
        another_source_register=[5, 4, 3, 2, 1, 0]
    )

    ARS_RI = INTEGER(
        "integer",
        "ARS",
        [1, 0, 0, 0, 0, 1, 1, 1, 0, 1],
        source_register=[11, 10, 9, 8, 7, 6],
        immediate_number=[15, 14, 13, 12, 5, 4, 3, 2, 1, 0]
    )

    ARS_IR = INTEGER(
        "integer",
        "ARS",
        [1, 0, 0, 0, 0, 1, 1, 1, 1, 0],
        source_register=[11, 10, 9, 8, 7, 6],
        immediate_number=[15, 14, 13, 12, 5, 4, 3, 2, 1, 0]
    )

    ARS_II = INTEGER(
        "integer",
        "ARS",
        [1, 0, 0, 0, 0, 1, 1, 1, 1, 1],
        immediate_number=[15, 14, 13, 12, 11, 10, 9, 8, 7, 6],
        another_immediate_number=[5, 4, 3, 2, 1, 0]
    )

    LCS_RR = INTEGER(
        "integer",
        "LCS",
        [1, 0, 0, 0, 1, 0, 0, 0, 0, 0],
        source_register=[11, 10, 9, 8, 7, 6],
        another_source_register=[5, 4, 3, 2, 1, 0]
    )

    LCS_RI = INTEGER(
        "integer",
        "LCS",
        [1, 0, 0, 0, 1, 0, 0, 0, 0, 1],
        source_register=[11, 10, 9, 8, 7, 6],
        immediate_number=[15, 14, 13, 12, 5, 4, 3, 2, 1, 0]
    )

    LCS_IR = INTEGER(
        "integer",
        "LCS",
        [1, 0, 0, 0, 1, 0, 0, 0, 1, 0],
        source_register=[11, 10, 9, 8, 7, 6],
        immediate_number=[15, 14, 13, 12, 5, 4, 3, 2, 1, 0]
    )

    LCS_II = INTEGER(
        "integer",
        "LCS",
        [1, 0, 0, 0, 1, 0, 0, 0, 1, 1],
        immediate_number=[15, 14, 13, 12, 11, 10, 9, 8, 7, 6],
        another_immediate_number=[5, 4, 3, 2, 1, 0]
    )

    GT_RR = BRANCH(
        "branch",
        "GT",
        [1, 0, 0, 1, 0, 0, 0, 0, 0, 0],
        source_register=[11, 10, 9, 8, 7, 6],
        another_source_register=[5, 4, 3, 2, 1, 0]
    )

    GT_RI = BRANCH(
        "branch",
        "GT",
        [1, 0, 0, 1, 0, 0, 0, 0, 0, 1],
        source_register=[11, 10, 9, 8, 7, 6],
        immediate_number=[15, 14, 13, 12, 5, 4, 3, 2, 1, 0]
    )

    EQ_RR = BRANCH(
        "branch",
        "EQ",
        [1, 0, 0, 1, 0, 0, 0, 0, 1, 0],
        source_register=[11, 10, 9, 8, 7, 6],
        another_source_register=[5, 4, 3, 2, 1, 0]
    )

    EQ_RI = BRANCH(
        "branch",
        "EQ",
        [1, 0, 0, 1, 0, 0, 0, 0, 1, 1],
        source_register=[11, 10, 9, 8, 7, 6],
        immediate_number=[15, 14, 13, 12, 5, 4, 3, 2, 1, 0]
    )

    LT_RR = BRANCH(
        "branch",
        "LT",
        [1, 0, 0, 1, 0, 0, 0, 1, 0, 0],
        source_register=[11, 10, 9, 8, 7, 6],
        another_source_register=[5, 4, 3, 2, 1, 0]
    )

    LT_RI = BRANCH(
        "branch",
        "LT",
        [1, 0, 0, 1, 0, 0, 0, 1, 0, 1],
        source_register=[11, 10, 9, 8, 7, 6],
        immediate_number=[15, 14, 13, 12, 5, 4, 3, 2, 1, 0]
    )

    GTE_RR = BRANCH(
        "branch",
        "GTE",
        [1, 0, 0, 1, 0, 0, 0, 1, 1, 0],
        source_register=[11, 10, 9, 8, 7, 6],
        another_source_register=[5, 4, 3, 2, 1, 0]
    )

    GTE_RI = BRANCH(
        "branch",
        "GTE",
        [1, 0, 0, 1, 0, 0, 0, 1, 1, 1],
        source_register=[11, 10, 9, 8, 7, 6],
        immediate_number=[15, 14, 13, 12, 5, 4, 3, 2, 1, 0]
    )

    LTE_RR = BRANCH(
        "branch",
        "LTE",
        [1, 0, 0, 1, 0, 0, 1, 0, 0, 0],
        source_register=[11, 10, 9, 8, 7, 6],
        another_source_register=[5, 4, 3, 2, 1, 0]
    )

    LTE_RI = BRANCH(
        "branch",
        "LTE",
        [1, 0, 0, 1, 0, 0, 1, 0, 0, 1],
        source_register=[11, 10, 9, 8, 7, 6],
        immediate_number=[15, 14, 13, 12, 5, 4, 3, 2, 1, 0]
    )

    JMP_I = JUMP(
        "jump",
        "JMP",
        [1, 1, 0, 0, 0, 0, 0, 0, 0, 0],
        immediate_number=[21, 20, 19, 18, 17, 16, 15, 14, 13, 12, 11,
                          10, 9, 8, 7, 6, 5, 4, 3, 2, 1, 0]
    )

    JMP_R = JUMP(
        "jump",
        "JMP",
        [1, 1, 0, 0, 0, 0, 0, 0, 0, 1],
        first_source_register=[11, 10, 9, 8, 7, 6],
        second_source_register=[5, 4, 3, 2, 1, 0]
    )

    OJMP_I = JUMP(
        "jump",
        "OJMP",
        [1, 1, 0, 0, 0, 0, 0, 0, 1, 0],
        immediate_number=[21, 20, 19, 18, 17, 16, 15, 14, 13, 12, 11,
                          10, 9, 8, 7, 6, 5, 4, 3, 2, 1, 0]
    )

    OJMP_R = JUMP(
        "jump",
        "OJMP",
        [1, 1, 0, 0, 0, 0, 0, 0, 1, 1],
        first_source_register=[11, 10, 9, 8, 7, 6],
        second_source_register=[5, 4, 3, 2, 1, 0]
    )

    ZJMP_I = JUMP(
        "jump",
        "ZJMP",
        [1, 1, 0, 0, 0, 0, 0, 1, 0, 0],
        immediate_number=[21, 20, 19, 18, 17, 16, 15, 14, 13, 12, 11,
                          10, 9, 8, 7, 6, 5, 4, 3, 2, 1, 0]
    )

    ZJMP_R = JUMP(
        "jump",
        "ZJMP",
        [1, 1, 0, 0, 0, 0, 0, 1, 0, 1],
        first_source_register=[11, 10, 9, 8, 7, 6],
        second_source_register=[5, 4, 3, 2, 1, 0]
    )

    NOP = Instruction(
        "others",
        "NOP",
        [1, 1, 0, 0, 0, 0, 0, 1, 1, 0]
    )

    def __init__(self):
        pass

    def findInstruction(self, instruction: List[int]):
        for i in dir(self):
            if not i.startswith("__") and not i.endswith("__"):
                try:
                    getattr(self, i).isItThisInstruction(instruction)
                except NotThisInstructionError:
                    pass
                except Exception as e:
                    raise e
                else:
                    print(getattr(self, i).i_type, getattr(self, i).i_name)
