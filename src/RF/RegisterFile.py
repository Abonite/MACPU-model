class Register:
    curr_value = 0
    lable = 0

    def __init__(self, label: int):
        self.lable = label

    def setValue(self, value: int):
        self.curr_value = value


class RegisterFile:
    def __init__(self):
        pass
