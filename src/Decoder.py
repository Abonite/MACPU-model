class Decoder:
    def __init__(self):
        self.instruction = [0, 0, 0]
        self.counter = 0
        self.instruction_item = 1

    def setValue(self, value: int):
        self.instruction[self.counter] = value

        if self.counter == 0:
            match value:
                case 1 | 2 | 3 | 4 | 5 | 6 | 0x48 | 0x49 | 0x4A | 0x4B | \
                        0x4C | 0x4D | 0x4E | 0x4F:
                    self.instruction_item = 2
                case _:
                    self.instruction_item = 1

        self.counter += 1

        if self.counter < self.instruction_item:
            return False, [0, 0, 0]
        else:
            self.counter = 0
            return True, self.instruction
