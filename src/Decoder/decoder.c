#define __32bit__

#include "decoder.h"

struct Decoder new_decoder() {
    struct Decoder result = {
        0,
        0,
        0,
        0,
        0,
        0,
        meth_decode_impl
    };

    return result;
}

#ifdef __32bit__
    #define OP_CODE_LBIT 22 // low bit at 22
    #define OP_CODE_BITM 0b1111111111

    int meth_decode_impl(struct Decoder *self, int source_code) {
        unsigned char op_code;
        op_code = (source_code & (OP_CODE_BITM << OP_CODE_LBIT)) >> OP_CODE_LBIT;

        switch (op_code) {
        // LOAD8 immediate
        case 0b0000000001:
            self->reg_A = (source_code & (0b111111 << 16)) >> 16;
            self->bit16_imme = 1;
            self->mid_p = (source_code & (0b1111 << 12)) >> 12;
            self->reg_B = (source_code & (0b111111 << 6)) >> 6;
            self->C_is_imme = 0;
            self->reg_C = (source_code & 0b111111);
            break;
        // LOAD8 register address
        case 0b0000000010:
            self->reg_A = (source_code & (0b111111 << 16)) >> 16;
            self->bit16_imme = 0;
            self->mid_p = (source_code & (0b1111 << 12)) >> 12;
            self->reg_B = (source_code & (0b111111 << 6)) >> 6;
            self->C_is_imme = 0;
            self->reg_C = (source_code & 0b111111);
            break;
        // LOAD16 immediate
        case 0b0000000011:
            self->reg_A = (source_code & (0b111111 << 16)) >> 16;
            self->bit16_imme = 1;
            self->mid_p = (source_code & (0b1111 << 12)) >> 12;
            self->reg_B = (source_code & (0b111111 << 6)) >> 6;
            self->C_is_imme = 0;
            self->reg_C = (source_code & 0b111111);
            break;
        // LOAD16 register address
        case 0b0000000100:
            self->reg_A = (source_code & (0b111111 << 16)) >> 16;
            self->bit16_imme = 0;
            self->mid_p = (source_code & (0b1111 << 12)) >> 12;
            self->reg_B = (source_code & (0b111111 << 6)) >> 6;
            self->C_is_imme = 0;
            self->reg_C = (source_code & 0b111111);
            break;
        // LOAD32 register address
        case 0b0000000101:
            self->reg_A = (source_code & (0b111111 << 16)) >> 16;
            self->bit16_imme = 0;
            self->mid_p = (source_code & (0b1111 << 12)) >> 12;
            self->reg_B = (source_code & (0b111111 << 6)) >> 6;
            self->C_is_imme = 0;
            self->reg_C = (source_code & 0b111111);
            break;

        // STORE8
        case 0b0000000110:
            self->reg_A = (source_code & (0b111111 << 16)) >> 16;
            self->bit16_imme = 1;
            self->mid_p = (source_code & (0b1111 << 12)) >> 12;
            self->reg_B = (source_code & (0b111111 << 6)) >> 6;
            self->C_is_imme = 0;
            self->reg_C = (source_code & 0b111111);
            break;
        // STORE16
        case 0b0000000111:
            self->reg_A = (source_code & (0b111111 << 16)) >> 16;
            self->bit16_imme = 1;
            self->mid_p = (source_code & (0b1111 << 12)) >> 12;
            self->reg_B = (source_code & (0b111111 << 6)) >> 6;
            self->C_is_imme = 0;
            self->reg_C = (source_code & 0b111111);
            break;
        // STORE32
        case 0b0000001000:
            self->reg_A = (source_code & (0b111111 << 16)) >> 16;
            self->bit16_imme = 1;
            self->mid_p = (source_code & (0b1111 << 12)) >> 12;
            self->reg_B = (source_code & (0b111111 << 6)) >> 6;
            self->C_is_imme = 0;
            self->reg_C = (source_code & 0b111111);
            break;


        // MOVE
        case 0b0000001001:
            self->reg_A = (source_code & (0b111111 << 16)) >> 16;
            self->bit16_imme = 0;
            self->mid_p = (source_code & (0b1111 << 12)) >> 12;
            self->reg_B = (source_code & (0b111111 << 6)) >> 6;
            self->C_is_imme = 0;
            self->reg_C = (source_code & 0b111111);
            break;


        // ADD
        case 0b1000000000:
            self->reg_A = (source_code & (0b111111 << 16)) >> 16;
            self->bit16_imme = 0;
            self->mid_p = (source_code & (0b1111 << 12)) >> 12;
            self->reg_B = (source_code & (0b111111 << 6)) >> 6;
            self->C_is_imme = 0;
            self->reg_C = (source_code & 0b111111);
            break;
        default:
            break;
        }
    }
#endif
