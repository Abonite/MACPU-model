from typing import List


class ArithmeticLogicUnit:
    unit_width = 0

    ADD_R = []
    SUB_R = []
    MUL_R = []
    DIV_Q = []
    DIV_R = []

    NOT_R = []
    AND_R = []
    OR_R = []
    XOR_R = []

    ASL_R = []
    ASR_R = []
    LSL_R = []
    LSR_R = []
    LCS_R = []

    GTJ_R = []
    STJ_R = []
    EJ_R = []

    def __init__(
            self,
            unit_width: int = 16
    ):
        self.unit_width = unit_width

    def caculate(self, input_a: List[int], input_b: List[int], option: List[int], output: List[int]):

