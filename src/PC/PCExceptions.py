class PCAddressOverFlowError(Exception):
    def __init__(self, addr: int):
        self.addr = addr

    def __str__(self):
        return f"Address {self.addr} exceeds valid value"
