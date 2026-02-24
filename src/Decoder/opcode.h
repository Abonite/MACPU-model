#ifndef __DEFINE_OPCODE__
    #define __DEFINE_OPCODE__

    #ifdef __32bit__

        #define LOAD8_IMME  0b0000000001
        #define LOAD8_REG   0b0000000010
        #define LOAD16_IMME 0b0000000011
        #define LOAD16_REG  0b0000000100
        #define LOAD32      0b0000000101
        #define STORE8      0b0000000110
        #define STORE16     0b0000000111
        #define STORE32     0b0000001000

        #define MOVE        0b0000001001

        #define ADD_IMME    0b1000000000
        #define ADD_REG     0b1000000001
        #define SUB_IMME_RI 0b1000000010
        #define SUB_REG     0b1000000011

        #define EQ_IMME     0b1001000010
        #define EQ_REG      0b1001000011

        #define JMP_IMME    0b1100000000
        #define JMP_REG     0b1100000001
        #define OJMP_IMME   0b1100000010
        #define OJMP_REG    0b1100000011
        #define ZJMP_IMME   0b1100000100
        #define ZJMP_REG    0b1100000101
    #endif
#endif