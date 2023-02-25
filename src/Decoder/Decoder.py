from typing import List


class Decoder:
    curr_instruction = [0 for _ in range(32)]

    def __init__(self):
        """left is high bit, right is low"""
        pass

    def decode(self, inst: List[int]):
        self.curr_instruction = inst

    def __D(self):
        op_code = self.curr_instruction[:9]