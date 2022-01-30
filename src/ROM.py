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
        self.tag_place = []

        for instruction in assembly:
            instruction = instruction.rstrip("\n")
            instruction = instruction.split(";")[0]
            instruction = instruction.rstrip("\t").rstrip(" ")

            if instruction == "":
                continue

            is_inst = False
            if instruction.startswith("\t") or instruction.startswith(" "):
                instruction = instruction.lstrip("\t").lstrip(" ")
                is_inst = True
            else:
                is_inst = False

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
                            if item.startswith("0x"):
                                self.rom.append(int(item, 16))
                            else:
                                self.rom.append(IS[item])
                        else:
                            self.rom.append(temp)
            else:
                tag_address = len(self.rom)
                tag = instruction.rstrip(":")
                self.tag_place.append(tag)
                self.tag_place.append(tag_address)

        for i in range(0, len(self.tag_place), 2):
            tag = self.tag_place[i]
            tag_address = self.tag_place[i + 1]
            tag_place = self.tag_stack[self.tag_stack.index(tag) + 1]
            self.rom[tag_place] = tag_address

    def getValue(self, address: int):
        return self.rom[address]

    def getRomSize(self):
        return len(self.rom)
