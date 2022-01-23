IS = {
    # Sleep - CPU will do nothing
    "SLP": 0x0000,

    # Read in A
    "RDA": 0x0001,
    # Read in B
    "RDB": 0x0002,
    # Read in C
    "RDC": 0x0003,
    # Read in D
    "RDD": 0x0004,
    # Read in E
    "RDE": 0x0005,
    # Read in F
    "RDF": 0x0006,

    # Write A
    # The value in A register will be written in the address
    # which designated by register E
    "EWRA": 0x0007,
    # Write B
    # The value in B register will be written in the address
    # which designated by register E
    "EWRB": 0x0008,
    # Write C
    # The value in C register will be written in the address
    # which designated by register E
    "EWRC": 0x0009,
    # Write D
    # The value in D register will be written in the address
    # which designated by register E
    "EWRD": 0x000A,
    # The value in A register will be written in the address
    # which designated by register F
    "FWRA": 0x000B,
    # Write B
    # The value in B register will be written in the address
    # which designated by register F
    "FWRB": 0x000C,
    # Write C
    # The value in C register will be written in the address
    # which designated by register F
    "FWRC": 0x000D,
    # Write D
    # The value in D register will be written in the address
    # which designated by register F
    "FWRD": 0x000E,

    # Move the value of register A into register F
    "MAF": 0x000F,
    # Move the value of register F into register A
    "MFA": 0x0010,
    # Move the value of register A into register E
    "MAE": 0x0011,
    # Move the value of register E into register A
    "MEA": 0x0012,
    # Move the value of register A into register D
    "MAD": 0x0013,
    # Move the value of register D into register A
    "MDA": 0x0014,
    # Move the value of register A into register C
    "MAC": 0x0015,
    # Move the value of register C into register A
    "MCA": 0x0016,
    # Move the value of register A into register B
    "MAB": 0x0017,
    # Move the value of register B into register A
    "MBA": 0x0018,
    # Move the value of register B into register F
    "MBF": 0x0019,
    # Move the value of register F into register B
    "MFB": 0x001A,
    # Move the value of register B into register E
    "MBE": 0x001B,
    # Move the value of register E into register B
    "MEB": 0x001C,
    # Move the value of register B into register D
    "MBD": 0x001D,
    # Move the value of register D into register B
    "MDB": 0x001E,
    # Move the value of register B into register C
    "MBC": 0x001F,
    # Move the value of register C into register B
    "MCB": 0x0020,
    # Move the value of register C into register F
    "MCF": 0x0021,
    # Move the value of register F into register C
    "MFC": 0x0022,
    # Move the value of register C into register E
    "MCE": 0x0023,
    # Move the value of register E into register C
    "MEC": 0x0024,
    # Move the value of register C into register D
    "MCD": 0x0025,
    # Move the value of register D into register C
    "MDC": 0x0026,
    # Move the value of register D into register F
    "MDF": 0x0027,
    # Move the value of register F into register D
    "MFD": 0x0028,
    # Move the value of register D into register E
    "MDE": 0x0029,
    # Move the value of register E into register D
    "MED": 0x002A,
    # Move the value of register E into register F
    "MEF": 0x002B,
    # Move the value of register F into register E
    "MFE": 0x002C,



    # Add register A and B
    # The result will be storaged in register A
    "ADD": 0x0030,
    # Subtract register A and B
    "SUB": 0x0031,

    # Push register A in to the stack
    "PSHA": 0x0040,
    # Push register B in to the stack
    "PSHB": 0x0041,
    # Push register C in to the stack
    "PSHC": 0x0042,
    # Push register D in to the stack
    "PSHD": 0x0043,
    # Push register E in to the stack
    "PSHE": 0x0044,
    # Push register F in to the stack
    "PSHF": 0x0045,
    # Push register X in to the stack
    "PSHX": 0x0046,
    # Push register Z in to the stack
    "PSHZ": 0x0047,
    # Pop stack in to register A
    "POPA": 0x0048,
    # Pop stack in to register B
    "POPB": 0x0049,
    # Pop stack in to register C
    "POPC": 0x004A,
    # Pop stack in to register D
    "POPD": 0x004B,
    # Pop stack in to register E
    "POPE": 0x004C,
    # Pop stack in to register F
    "POPF": 0x004D,
    # Pop stack in to register X
    "POPX": 0x004E,
    # Pop stack in to register Z
    "POPZ": 0x004F,

    # Jump to the address designated by the value in register E
    "JMP": 0x0050,
    # If the value of register C is zero
    # Then jump to the address designated by register E
    "JCZ": 0x0051,
    # If the value of register C is not zero
    # Then jump to the address designated by register E
    "JCNZ": 0x0052,
    # If the value of register D is zero
    # Then jump to the address designated by register E
    "JDZ": 0x0053,
    # If the value of register D is not zero
    # Then jump to the address designated by register E
    "JDNZ": 0x0054,

    # If the value of register A and B is equal
    # Then set register C to zero
    "AEB": 0x0060,
    # If the value of register A and B is not equal
    # Then set register C to zero
    "ANEB": 0x0061,

    # Register D is decremented by one
    "DDO": 0x0070,
    # Register C is decremented by one
    "CDO": 0x0071,
    # Register B is decremented by one
    "BDO": 0x0072,
    # Register A is decremented by one
    "ADO": 0x0073,
    # Register D is self-incrising by one
    "DSI": 0x0074,
    # Register C is self-incrising by one
    "CSI": 0x0075,
    # Register B is self-incrising by one
    "BSI": 0x0076,
    # Register A is self-incrising by one
    "ASI": 0x0077,

    # Trigger interrupt
    "ITR": 0x0080,

    # Output the data
    # Use value of register B as address
    # Use value of register A as data
    "OUT": 0x0090,

    # Stop cpu
    "STP": 0xFFFF
    }
