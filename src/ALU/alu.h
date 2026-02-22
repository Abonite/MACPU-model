#ifndef __ALU__
    #define __ALU__

    int integer_caculate_unit (
        struct Decoder *decoder,
        unsigned char *immediate,
        struct ProgramCounter *pc,
        struct RegisterFile *rf
    );
#endif