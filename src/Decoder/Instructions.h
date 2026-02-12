typedef enum {
    PC = 0b101001,
    ZERO = 0b000000,
    A1 = 0b000001,
    A2 = 0b000010,
    A3 = 0b000011,
    A4 = 0b000100,
    AR1 = 0b000101,
    AR2 = 0b000110,
    AR3 = 0b000111,
    ASS = 0b001000,
    ASP = 0b001001,
    ADS = 0b001010,
    B1 = 0b001011,
    B2 = 0b001100,
    B3 = 0b001101,
    B4 = 0b001110,
    BR1 = 0b001111,
    BR2 = 0b010000,
    BR3 = 0b010001,
    BSS = 0b010010,
    BSP = 0b010011,
    BDS = 0b010100,
    C1 = 0b010101,
    C2 = 0b010110,
    C3 = 0b010111,
    C4 = 0b011000,
    CR1 = 0b011001,
    CR2 = 0b011010,
    CR3 = 0b011011,
    CSS = 0b011100,
    CSP = 0b011101,
    CDS = 0b011110,
    D1 = 0b011111,
    D2 = 0b100000,
    D3 = 0b100001,
    D4 = 0b100010,
    DR1 = 0b100011,
    DR2 = 0b100100,
    DR3 = 0b100101,
    DSS = 0b100110,
    DSP = 0b100111,
    DDS = 0b101000
} REGISTERS;

typedef struct {
    const unsigned short op_code = 0b0000000001;

    const unsigned char target_register_bit_width = 6;
    const unsigned char target_prohibit_register_number = 2;
    const unsigned char target_prohibit_register[2] = {ZERO, PC};

    const unsigned char source_bit_width = 16;
    const unsigned char source_register_number = 0;
    const unsigned char source_prohibit_register_number = 0;
} LOAD8_I;

typedef struct {
    const unsigned short op_code = 0b0000000010;

    const unsigned char target_register_bit_width = 6;
    const unsigned char target_prohibit_register_number = 2;
    const unsigned char target_prohibit_register[2] = {ZERO, PC};

    const unsigned char zero_bit_width = 4;
    const unsigned char source_register_number = 2;
    const unsigned char source_prohibit_register_number[2] = {0, 0};
    const unsigned char source_register_bit_width[2] = {6, 6};
} LOAD8_R;

typedef struct {
    const unsigned short op_code = 0b0000000011;

    const unsigned char target_register_bit_width = 6;
    const unsigned char target_prohibit_register_number = 2;
    const unsigned char target_prohibit_register[2] = {ZERO, PC};

    const unsigned char source_bit_width = 16;
    const unsigned char source_register_number = 0;
    const unsigned char source_prohibit_register_number = 0;
} LOAD16_I;

typedef struct {
    const unsigned short op_code = 0b0000000100;

    const unsigned char target_register_bit_width = 6;
    const unsigned char target_prohibit_register_number = 2;
    const unsigned char target_prohibit_register[2] = {ZERO, PC};

    const unsigned char zero_bit_width = 4;
    const unsigned char source_register_number = 2;
    const unsigned char source_prohibit_register_number[2] = {0, 0};
    const unsigned char source_register_bit_width[2] = {6, 6};
} LOAD16_R;

typedef struct {
    const unsigned short op_code = 0b0000000101;

    const unsigned char target_register_bit_width = 6;
    const unsigned char target_prohibit_register_number = 2;
    const unsigned char target_prohibit_register[2] = {ZERO, PC};

    const unsigned char zero_bit_width = 4;
    const unsigned char source_register_number = 2;
    const unsigned char source_prohibit_register_number[2] = {0, 0};
    const unsigned char source_register_bit_width[2] = {6, 6};
} LOAD32;

typedef struct {
    const unsigned char op_code = 0b0000000110;

    const unsigned char source_register_bit_width = 6;
    const unsigned char target_prohibit_register_number = 1;
    const unsigned char target_prohibit_register[1] = {ZERO};

    const unsigned char zero_bit_width = 4;

    const unsigned char source_register_number = 2;
    const unsigned char source_prohibit_register_number[2] = {1, 0};
    const unsigned char target_prohibit_register[1] = {ZERO};
    const unsigned char source_register_bit_width[2] = {6, 6};
} STORE8;

typedef struct {
    const unsigned char op_code = 0b0000000111;

    const unsigned char source_register_bit_width = 6;
    const unsigned char target_prohibit_register_number = 1;
    const unsigned char target_prohibit_register[1] = {ZERO};

    const unsigned char zero_bit_width = 4;

    const unsigned char source_register_number = 2;
    const unsigned char source_prohibit_register_number[2] = {1, 0};
    const unsigned char target_prohibit_register[1] = {ZERO};
    const unsigned char source_register_bit_width[2] = {6, 6};
} STORE16;

typedef struct {
    const unsigned char op_code = 0b0000001000;

    const unsigned char source_register_bit_width = 6;
    const unsigned char target_prohibit_register_number = 1;
    const unsigned char target_prohibit_register[1] = {ZERO};

    const unsigned char zero_bit_width = 4;

    const unsigned char source_register_number = 2;
    const unsigned char source_prohibit_register_number[2] = {1, 0};
    const unsigned char target_prohibit_register[1] = {ZERO};
    const unsigned char source_register_bit_width[2] = {6, 6};
} STORE32;