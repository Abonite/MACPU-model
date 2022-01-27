from src.CpuException import UndefinedInstructionError, \
    StackOverflowError, ExitError


class Executer:
    def __init__(self, stack_start: int, stack_size: int):
        self.reg_a = 0
        self.reg_b = 0
        self.reg_c = 0
        self.reg_d = 0
        self.reg_e = 0
        self.reg_f = 0

        self.reg_stack_start = stack_start
        self.reg_stack_pointer = 0
        self.reg_stack_size = stack_size

        self.reg_x = 0
        self.reg_z = 0

    def execute(self, instruction: list[int, int, int]):
        inst = instruction[0]
        arg1 = instruction[1]

        match inst:
            # Sleep - CPU will do nothing
            case 0x0000:
                return "NAN", 0, 0
            # Read in A
            case 0x0001:
                self.reg_a = arg1
                return "NAN", 0, 0
            # Read in B
            case 0x0002:
                self.reg_b = arg1
                return "NAN", 0, 0
            # Read in C
            case 0x0003:
                self.reg_c = arg1
                return "NAN", 0, 0
            # Read in D
            case 0x0004:
                self.reg_d = arg1
                return "NAN", 0, 0
            # Read in E
            case 0x0005:
                self.reg_e = arg1
                return "NAN", 0, 0
            # Read in F
            case 0x0006:
                self.reg_f = arg1
                return "NAN", 0, 0

            # Write A
            # The value in A register will be written in the address
            # which designated by register E
            case 0x0007:
                return "DMEM", self.reg_a, self.reg_e
            # Write B
            # The value in B register will be written in the address
            # which designated by register E
            case 0x0008:
                return "DMEM", self.reg_b, self.reg_e
            # Write C
            # The value in C register will be written in the address
            # which designated by register E
            case 0x0009:
                return "DMEM", self.reg_c, self.reg_e
            # Write D
            # The value in D register will be written in the address
            # which designated by register E
            case 0x000A:
                return "DMEM", self.reg_d, self.reg_e
            # The value in A register will be written in the address
            # which designated by register F
            case 0x000B:
                return "DMEM", self.reg_a, self.reg_f
            # Write B
            # The value in B register will be written in the address
            # which designated by register F
            case 0x000C:
                return "DMEM", self.reg_b, self.reg_f
            # Write C
            # The value in C register will be written in the address
            # which designated by register F
            case 0x000D:
                return "DMEM", self.reg_c, self.reg_f
            # Write D
            # The value in D register will be written in the address
            # which designated by register F
            case 0x000E:
                return "DMEM", self.reg_d, self.reg_f

            # Move the value of register A into register F
            case 0x000F:
                self.reg_f = self.reg_a
                return "NAN", 0, 0
            # Move the value of register F into register A
            case 0x0010:
                self.reg_a = self.reg_f
                return "NAN", 0, 0
            # Move the value of register A into register E
            case 0x0011:
                self.reg_e = self.reg_a
                return "NAN", 0, 0
            # Move the value of register E into register A
            case 0x0012:
                self.reg_a = self.reg_e
                return "NAN", 0, 0
            # Move the value of register A into register D
            case 0x0013:
                self.reg_d = self.reg_a
                return "NAN", 0, 0
            # Move the value of register D into register A
            case 0x0014:
                self.reg_a = self.reg_d
                return "NAN", 0, 0
            # Move the value of register A into register C
            case 0x0015:
                self.reg_c = self.reg_a
                return "NAN", 0, 0
            # Move the value of register C into register A
            case 0x0016:
                self.reg_a = self.reg_c
                return "NAN", 0, 0
            # Move the value of register A into register B
            case 0x0017:
                self.reg_b = self.reg_a
                return "NAN", 0, 0
            # Move the value of register B into register A
            case 0x0018:
                self.reg_a = self.reg_b
                return "NAN", 0, 0
            # Move the value of register B into register F
            case 0x0019:
                self.reg_f = self.reg_b
                return "NAN", 0, 0
            # Move the value of register F into register B
            case 0x001A:
                self.reg_b = self.reg_f
                return "NAN", 0, 0
            # Move the value of register B into register E
            case 0x001B:
                self.reg_e = self.reg_b
                return "NAN", 0, 0
            # Move the value of register E into register B
            case 0x001C:
                self.reg_b = self.reg_e
                return "NAN", 0, 0
            # Move the value of register B into register D
            case 0x001D:
                self.reg_d = self.reg_b
                return "NAN", 0, 0
            # Move the value of register D into register B
            case 0x001E:
                self.reg_b = self.reg_d
                return "NAN", 0, 0
            # Move the value of register B into register C
            case 0x001F:
                self.reg_c = self.reg_b
                return "NAN", 0, 0
            # Move the value of register C into register B
            case 0x0020:
                self.reg_b = self.reg_c
                return "NAN", 0, 0
            # Move the value of register C into register F
            case 0x0021:
                self.reg_f = self.reg_c
                return "NAN", 0, 0
            # Move the value of register F into register C
            case 0x0022:
                self.reg_c = self.reg_f
                return "NAN", 0, 0
            # Move the value of register C into register E
            case 0x0023:
                self.reg_e = self.reg_c
                return "NAN", 0, 0
            # Move the value of register E into register C
            case 0x0024:
                self.reg_c = self.reg_e
                return "NAN", 0, 0
            # Move the value of register C into register D
            case 0x0025:
                self.reg_d = self.reg_c
                return "NAN", 0, 0
            # Move the value of register D into register C
            case 0x0026:
                self.reg_c = self.reg_d
                return "NAN", 0, 0
            # Move the value of register D into register F
            case 0x0027:
                self.reg_f = self.reg_d
                return "NAN", 0, 0
            # Move the value of register F into register D
            case 0x0028:
                self.reg_d = self.reg_f
                return "NAN", 0, 0
            # Move the value of register D into register E
            case 0x0029:
                self.reg_e = self.reg_d
                return "NAN", 0, 0
            # Move the value of register E into register D
            case 0x002A:
                self.reg_d = self.reg_e
                return "NAN", 0, 0
            # Move the value of register E into register F
            case 0x002B:
                self.reg_f = self.reg_e
                return "NAN", 0, 0
            # Move the value of register F into register E
            case 0x002C:
                self.reg_e = self.reg_f
                return "NAN", 0, 0

            # Add register A and B
            # The result will be storaged in register A
            case 0x0030:
                self.reg_a = self.reg_a + self.reg_b
                return "NAN", 0, 0
            # Subtract register A and B
            case 0x0031:
                self.reg_a = self.reg_a - self.reg_b
                return "NAN", 0, 0

            # Push register A in to the stack
            case 0x0040:
                stack_address = self.reg_stack_pointer + self.reg_stack_start
                self.reg_stack_pointer += 1
                if self.reg_stack_pointer > self.reg_stack_size:
                    raise StackOverflowError()
                else:
                    return "DMEM", self.reg_a, stack_address
            # Push register B in to the stack
            case 0x0041:
                stack_address = self.reg_stack_pointer + self.reg_stack_start
                self.reg_stack_pointer += 1
                if self.reg_stack_pointer > self.reg_stack_size:
                    raise StackOverflowError()
                else:
                    return "DMEM", self.reg_b, stack_address
            # Push register C in to the stack
            case 0x0042:
                stack_address = self.reg_stack_pointer + self.reg_stack_start
                self.reg_stack_pointer += 1
                if self.reg_stack_pointer > self.reg_stack_size:
                    raise StackOverflowError()
                else:
                    return "DMEM", self.reg_c, stack_address
            # Push register D in to the stack
            case 0x0043:
                stack_address = self.reg_stack_pointer + self.reg_stack_start
                self.reg_stack_pointer += 1
                if self.reg_stack_pointer > self.reg_stack_size:
                    raise StackOverflowError()
                else:
                    return "DMEM", self.reg_d, stack_address
            # Push register E in to the stack
            case 0x0044:
                stack_address = self.reg_stack_pointer + self.reg_stack_start
                self.reg_stack_pointer += 1
                if self.reg_stack_pointer > self.reg_stack_size:
                    raise StackOverflowError()
                else:
                    return "DMEM", self.reg_e, stack_address
            # Push register F in to the stack
            case 0x0045:
                stack_address = self.reg_stack_pointer + self.reg_stack_start
                self.reg_stack_pointer += 1
                if self.reg_stack_pointer > self.reg_stack_size:
                    raise StackOverflowError()
                else:
                    return "DMEM", self.reg_f, stack_address
            # Push register X in to the stack
            case 0x0046:
                stack_address = self.reg_stack_pointer + self.reg_stack_start
                self.reg_stack_pointer += 1
                if self.reg_stack_pointer > self.reg_stack_size:
                    raise StackOverflowError()
                else:
                    return "DMEM", self.reg_x, stack_address
            # Push register Z in to the stack
            case 0x0047:
                stack_address = self.reg_stack_pointer + self.reg_stack_start
                self.reg_stack_pointer += 1
                if self.reg_stack_pointer > self.reg_stack_size:
                    raise StackOverflowError()
                else:
                    return "DMEM", self.reg_z, stack_address
            # Pop stack in to register A
            case 0x0048:
                stack_address = self.reg_stack_pointer + self.reg_stack_start
                self.reg_stack_pointer -= 1
                if self.reg_stack_pointer < 0:
                    raise StackOverflowError()
                return "IDREG", stack_address, "RegA"
            # Pop stack in to register B
            case 0x0049:
                stack_address = self.reg_stack_pointer + self.reg_stack_start
                self.reg_stack_pointer -= 1
                if self.reg_stack_pointer < 0:
                    raise StackOverflowError()
                return "IDREG", stack_address, "RegB"
            # Pop stack in to register C
            case 0x004A:
                stack_address = self.reg_stack_pointer + self.reg_stack_start
                self.reg_stack_pointer -= 1
                if self.reg_stack_pointer < 0:
                    raise StackOverflowError()
                return "IDREG", stack_address, "RegC"
            # Pop stack in to register D
            case 0x004B:
                stack_address = self.reg_stack_pointer + self.reg_stack_start
                self.reg_stack_pointer -= 1
                if self.reg_stack_pointer < 0:
                    raise StackOverflowError()
                return "IDREG", stack_address, "RegD"
            # Pop stack in to register E
            case 0x004C:
                stack_address = self.reg_stack_pointer + self.reg_stack_start
                self.reg_stack_pointer -= 1
                if self.reg_stack_pointer < 0:
                    raise StackOverflowError()
                return "IDREG", stack_address, "RegE"
            # Pop stack in to register F
            case 0x004D:
                stack_address = self.reg_stack_pointer + self.reg_stack_start
                self.reg_stack_pointer -= 1
                if self.reg_stack_pointer < 0:
                    raise StackOverflowError()
                return "IDREG", stack_address, "RegF"
            # Pop stack in to register X
            case 0x004E:
                stack_address = self.reg_stack_pointer + self.reg_stack_start
                self.reg_stack_pointer -= 1
                if self.reg_stack_pointer < 0:
                    raise StackOverflowError()
                return "IDREG", stack_address, "RegX"
            # Pop stack in to register Z
            case 0x004F:
                stack_address = self.reg_stack_pointer + self.reg_stack_start
                self.reg_stack_pointer -= 1
                if self.reg_stack_pointer < 0:
                    raise StackOverflowError()
                return "IDREG", stack_address, "RegZ"

            # Jump to the address designated by the value in register E
            case 0x0050:
                return "DREG", self.reg_e, "PC"
            # If the value of register C is zero
            # Then jump to the address designated by register E
            case 0x0051:
                if self.reg_c == 0:
                    return "DREG", self.reg_e, "PC"
                else:
                    return "NAN", 0, 0
            # If the value of register C is not zero
            # Then jump to the address designated by register E
            case 0x0052:
                if self.reg_c != 0:
                    return "DREG", self.reg_e, "PC"
                else:
                    return "NAN", 0, 0
            # If the value of register D is zero
            # Then jump to the address designated by register E
            case 0x0053:
                if self.reg_d == 0:
                    return "DREG", self.reg_e, "PC"
                else:
                    return "NAN", 0, 0
            # If the value of register D is not zero
            # Then jump to the address designated by register E
            case 0x0054:
                if self.reg_d != 0:
                    return "DREG", self.reg_e, "PC"
                else:
                    return "NAN", 0, 0

            # If the value of register A and B is equal
            # Then set register C to zero
            case 0x0060:
                if self.reg_a == self.reg_b:
                    self.reg_c = 0
                else:
                    pass

                return "NAN", 0, 0
            # If the value of register A and B is not equal
            # Then set register C to zero
            case 0x0061:
                if self.reg_a != self.reg_b:
                    self.reg_c = 0
                else:
                    pass

                return "NAN", 0, 0

            # Register D is decremented by one
            case 0x0070:
                self.reg_d -= 1
                return "NAN", 0, 0
            # Register C is decremented by one
            case 0x0071:
                self.reg_c -= 1
                return "NAN", 0, 0
            # Register B is decremented by one
            case 0x0072:
                self.reg_b -= 1
                return "NAN", 0, 0
            # Register A is decremented by one
            case 0x0073:
                self.reg_a -= 1
                return "NAN", 0, 0
            # Register D is self-incrising by one
            case 0x0074:
                self.reg_d += 1
                return "NAN", 0, 0
            # Register C is self-incrising by one
            case 0x0075:
                self.reg_c += 1
                return "NAN", 0, 0
            # Register B is self-incrising by one
            case 0x0076:
                self.reg_b += 1
                return "NAN", 0, 0
            # Register A is self-incrising by one
            case 0x0077:
                self.reg_a += 1
                return "NAN", 0, 0

            # Trigger interrupt
            case 0x0080:
                return "NAN", 0, 0

            # Output the data
            # Use value of register B as address
            # Use value of register A as data
            case 0x0090:
                return "NAN", 0, 0

            # Stop cpu
            case 0xFFFF:
                input("Finish.Press Enter to exit...")
                raise ExitError()

            case _:
                raise UndefinedInstructionError(self.inst)
