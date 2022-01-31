from typing import Tuple


class Decoder:
    def __init__(self):
        self.instruction = [0, 0, 0]
        self.counter = 0
        self.instruction_item = 1

    def setValue(self, value: int) -> Tuple[bool, list[int, int, int]]:
        self.instruction[self.counter] = value

        if self.counter == 0:
            match value:
                case 1 | 2 | 3 | 4 | 5 | 6 | 0x51 | 0x52 | 0x53 | \
                        0x54 | 0x100 | 0x101 | 0x102:
                    self.instruction_item = 2
                case _:
                    self.instruction_item = 1

        self.counter += 1

        if self.counter < self.instruction_item:
            return False, [0, 0, 0]
        else:
            self.counter = 0
            inst = self.instruction
            self.instruction = [0 for i in (0, 1, 2)]
            return True, inst
