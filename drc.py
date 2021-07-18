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
    # Read in F
    "RDF": 0x06,
    # Write A
    # The value in A register will be written in the address
    # which designated by register E
    "EWRA": 0x07,
    # Write B
    # The value in B register will be written in the address
    # which designated by register E
    "EWRB": 0x08,
    # Write C
    # The value in A register will be written in the address
    # which designated by register E
    "EWRC": 0x09,
    # Write D
    # The value in B register will be written in the address
    # which designated by register E
    "EWRD": 0x0A,
    # The value in A register will be written in the address
    # which designated by register F
    "FWRA": 0x0B,
    # Write B
    # The value in B register will be written in the address
    # which designated by register F
    "FWRB": 0x0C,
    # Write C
    # The value in A register will be written in the address
    # which designated by register F
    "FWRC": 0x0D,
    # Write D
    # The value in B register will be written in the address
    # which designated by register F
    "FWRD": 0x0E,
    # Move the value of register A into register E
    "MAE": 0X0F,
    # Move the value of register E into register A
    "MEA": 0X10,
    # Move the value of register B into register E
    "MBE": 0X11,
    # Move the value of register E into register B
    "MEB": 0X12,
    # Move the value of register A into register F
    "MAF": 0X13,
    # Move the value of register F into register A
    "MFA": 0X14,
    # Move the value of register B into register F
    "MBF": 0X15,
    # Move the value of register F into register B
    "MFB": 0X16,


    # Add register A and B
    # The result will be storaged in register A
    "ADD": 0x20,
    # Subtract register A and B
    "SUB": 0x21,

    # Push register A in to the stack
    "PSHA": 0x30,
    # Push register B in to the stack
    "PSHB": 0x31,
    # Push register C in to the stack
    "PSHC": 0x32,
    # Push register D in to the stack
    "PSHD": 0x33,
    # Push register E in to the stack
    "PSHE": 0x34,
    # Push register F in to the stack
    "PSHF": 0x35,
    # Push register X in to the stack
    "PSHX": 0x36,
    # Push register Z in to the stack
    "PSHZ": 0x37,
    # Pop stack in to register A
    "POPA": 0x38,
    # Pop stack in to register B
    "POPB": 0x39,
    # Pop stack in to register C
    "POPC": 0x3A,
    # Pop stack in to register D
    "POPD": 0x3B,
    # Pop stack in to register E
    "POPE": 0x3C,
    # Pop stack in to register F
    "POPF": 0x3D,
    # Pop stack in to register X
    "POPX": 0x3E,
    # Pop stack in to register Z
    "POPZ": 0x3F,

    # Jump to the address designated by the value in register E
    "JMP": 0x40,
    # If the value of register C is zero
    # Then jump to the address designated by register E
    "JCZ": 0x41,
    # If the value of register C is not zero
    # Then jump to the address designated by register E
    "JCNZ": 0x42,
    # If the value of register D is zero
    # Then jump to the address designated by register E
    "JDZ": 0x43,
    # If the value of register D is not zero
    # Then jump to the address designated by register E
    "JDNZ": 0x44,

    # If the value of register A and B is equal
    # Then set register C to zero
    "AEB": 0x50,
    # If the value of register A and B is not equal
    # Then set register C to zero
    "ANEB": 0x51,

    # Register D is decremented by one
    "DDO": 0x60,
    # Register C is decremented by one
    "CDO": 0x61,
    # Register B is decremented by one
    "BDO": 0x62,
    # Register A is decremented by one
    "ADO": 0x63,
    # Register D is self-incrising by one
    "DSI": 0x64,
    # Register C is self-incrising by one
    "CSI": 0x65,
    # Register B is self-incrising by one
    "BSI": 0x66,
    # Register A is self-incrising by one
    "ASI": 0x67,

    # Trigger interrupt
    # Jump to the interrupt vector table looking for the jump address
    # The interrupt code is the value of the next address
    # ----interrupt vector table----
    # 1024 + interrupt code
    # CPU will read the value at the corresponding address to register E
    # Then need to manually trigger the jump,like use JMP
    "ITR": 0x70,

    # Output the data
    # Use value of register B as address
    # Use value of register A as data
    "OUT": 0x80,

    # Stop cpu
    "STP": 0xFF
    }
