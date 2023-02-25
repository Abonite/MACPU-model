class OperateCodeLenthError(Exception):
    def __init__(self, required_length: int):
        self.r_l = required_length

    def __str__(self) -> str:
        return f"Requires an opcode of length {self.r_l}bit"


class RegisterLabelBitsCrowdedError(Exception):
    def __init__(self, register: str):
        self.r = register

    def __str__(self) -> str:
        return f"The tag bit of register {self.r} is crowded"
