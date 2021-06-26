DRC = {
    # Sleep - CPU will do nothing
    "SLP": 0x00,

    # Read in A
    # The next 8bit will be moved in to register A
    "RDA": 0x01,
    # Read in B
    "RDB": 0x02,
    # Read in C
    "RDC": 0x03,
    # Read in D
    "RDD": 0x04,
    # Read in E
    "RDE": 0x05,
    # Write A
    # The value in A register will be written in the address
    # which designated by register E
    "WRA": 0x06,
    # Write B
    # The value in B register will be written in the address
    # which designated by register E
    "WRB": 0x07,
    # Write C
    # The value in A register will be written in the address
    # which designated by register E
    "WRC": 0x08,
    # Write D
    # The value in B register will be written in the address
    # which designated by register E
    "WRD": 0x09,
    # Move the value of register A into register E
    "MAE": 0X0A,
    # Move the value of register E into register A
    "MEA": 0X0B,
    # Move the value of register B into register E
    "MBE": 0X0C,
    # Move the value of register E into register B
    "MEB": 0X0D,
    # Move the value of register A into register B
    "MAB": 0X0E,

    # Add register A and B
    # The result will be storaged in register A
    "ADD": 0x10,
    # Subtract register A and B
    "SUB": 0x11,

    # Push register A,B,C,D,E,I,and IP in to the stack
    "PSH": 0x20,
    # Pop them out
    "POP": 0x21,

    # Jump to the address designated by the value in register E
    "JMP": 0x30,
    # If the value of register C is zero
    # Then jump to the address designated by register E
    "JCZ": 0x31,
    # If the value of register C is not zero
    # Then jump to the address designated by register E
    "JCNZ": 0x32,
    # If the value of register D is zero
    # Then jump to the address designated by register E
    "JDZ": 0x33,
    # If the value of register D is not zero
    # Then jump to the address designated by register E
    "JDNZ": 0x34,

    # If the value of register A and B is equal
    # Then set register C to zero
    "AEB": 0x40,
    # If the value of register A and B is not equal
    # Then set register C to zero
    "ANEB": 0x41,

    # Register D is decremented by one
    "DDO": 0x50,
    # Register C is decremented by one
    "CDO": 0x51,

    # Trigger interrupt
    # Jump to the interrupt vector table looking for the jump address
    # The interrupt code is the value of the next address
    # ----interrupt vector table----
    # 1024 + interrupt code
    # CPU will read the value at the corresponding address to register E
    # Then need to manually trigger the jump,like use JMP
    "ITR": 0x60,

    # Output the data
    # Use value of register B as address
    # Use value of register A as data
    "OUT": 0x70,

    # Stop cpu
    "STP": 0xFF
    }
