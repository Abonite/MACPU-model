class OperateCodeLenthError(Exception):
    def __init__(self, required_length: int):
        self.r_l = required_length

    def __str__(self) -> str:
        return f"Requires an opcode of length {self.r_l}bit"


class InstructionLenthError(Exception):
    def __init__(self, required_length: int):
        self.r_l = required_length

    def __str__(self) -> str:
        return f"Requires an instrution of length {self.r_l}bit"


class RegisterLabelLenthError(Exception):
    def __init__(self, required_length: int, register_name: str = " "):
        self.r_l = required_length
        self.r_n = register_name

    def __str__(self) -> str:
        return f"Requires a register{self.r_n}label of length {self.r_l}bit"


class NoThisRegisterError(Exception):
    def __init__(self, register_name: str):
        self.r_n = register_name

    def __str__(self) -> str:
        return f"""The number of valid bits in the label of register
{self.r_n} is 0, and there is no such register"""


class RegisterLabelBitsCrowdedError(Exception):
    def __init__(self, register: str, bit: int):
        self.r = register
        self.b = bit

    def __str__(self) -> str:
        return f"Bit {self.b} of register {self.r} label is occupied"


class ImmediateNumberBitsCrowdedError(Exception):
    def __init__(self, bit: int):
        self.b = bit

    def __str__(self) -> str:
        return f"The bit {self.b} of the immediate number is occupied"


class NotThisInstructionError(Exception):
    def __init__(self, inst: str):
        self.i = inst

    def __str__(self) -> str:
        return f"The instruction entered is not {self.i}"


class InvalidBitValueError(Exception):
    def __init__(self, inst: str, bit: int, value: int):
        self.i = inst
        self.b = bit
        self.v = value

    def __str__(self) -> str:
        return f"""The invalid bit of the input instruction is not as expected,
{self.i} should be {self.v} at bit {self.b}"""


class RegisterNotBeAllowedError(Exception):
    def __init__(self, inst: str, register: str):
        self.inst = inst
        self.register = register

    def __str__(self) -> str:
        return f"Register {self.register} of {self.inst} is not allowed"


class NoInstructionError(Exception):
    def __str__(self) -> str:
        return "Decoder did not latch to a valid instruction"


class IllegalInstructionError(Exception):
    def __str__(self) -> str:
        return "Decoder latches to all 0s instruction"
