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


class UndefinedRegisterError(Exception):
    def __init__(self, register: str):
        self.register = register

    def __str__(self):
        return """UndefinedRegisterError: The register is not defined: \
{}""".format(self.register)


class UndefinedOperaterError(Exception):
    def __init__(self, operater: str):
        self.operater = operater

    def __str__(self):
        return """UndefinedOperaterError: The operater is not defined: \
{}""".format(self.operater)


class StackOverflowError(Exception):
    def __init__(self):
        pass

    def __str__(self):
        return "StackOverflowError: The operater caused stack over flow"


class ExitError(Exception):
    def __init__(self):
        pass
