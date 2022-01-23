class MemoryCapacityTooSmallError(Exception):
    def __init__(self, ivt_size: int):
        self.ivt_size = ivt_size

    def __str__(self):
        return """MemoryCapacityTooSmallError: The requested memory capacity is \
less than that required by the interrupt vector table. IVT size: {:d}""".\
            format(self.ivt_size)


class UndefinedInstructionError(Exception):
    def __init__(self, instruction: int):
        self.instruction = instruction

    def __str__(self):
        return """UndefinedInstuctionError: The instruction is not defined: \
{:04X}""".format(self.instruction)
