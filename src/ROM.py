from src.InstructionSet import IS
from os.path import sep
from re import split as resplit


class Rom:
    def __init__(self):
        with open(".{}docs{}ROM.pca".format(sep, sep), "r") as pycpu_assembly:
            assembly = pycpu_assembly.readlines()
            pycpu_assembly.close()

        self.rom = []
        self.tag_stack = []

        for instruction in assembly:
            instruction = instruction.rstrip("\n")
            is_inst = False
            if instruction.startswith("\t") or instruction.startswith(" "):
                instruction = instruction.lstrip("\t").lstrip(" ")
                is_inst = False
            else:
                is_inst = True

            items = resplit("\s|,", instruction)

            if is_inst:
                if items[0] == "JMP" \
                        or items[0] == "JCZ" \
                        or items[0] == "JCNZ" \
                        or items[0] == "JDZ" \
                        or items[0] == "JDNZ":
                    self.rom.append(IS[items[0]])
                    self.tag_stack.append(items[1])
                    self.tag_stack.append(len(self.rom))
                    self.rom.append(0)
                else:
                    for item in items:
                        try:
                            temp = int(item)
                        except ValueError:
                            self.rom.append(IS[item])
                        else:
                            self.rom.append(temp)
            else:
                tag_address = len(self.rom)
                tag = instruction.rstrip(":")
                tag_place = self.tag_stack[self.tag_stack.index(tag) + 1]
                self.rom[tag_place] = tag_address

    def getValue(self, address: int):
        return self.rom[address]

    def getRomSize(self):
        return len(self.rom)
