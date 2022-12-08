class RegisterOverFlowError(Exception):
    def __init__(self, reg_width, num_width):
        self.reg_width = reg_width
        self.num_width = num_width

    def __str__(self, number_width):
        return f"""RegisterOverFlowError:
The value assigned to the register exceeds the bit width of the register.
The input digit bit width is: {self.num_width},
the register bit width is: {self.reg_width}"""
