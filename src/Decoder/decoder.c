#include <stdlib.h>

#define __32bit__

#include "decoder.h"

struct Decoder new_decoder() {
    struct Decoder result = {
        0,
        0,
        0,
        0,
        0,
        meth_decode_impl,
        meth_check_impl
    };

    return result;
}

#ifdef __32bit__
    #define OP_CODE_LBIT 22 // low bit at 22
    #define OP_CODE_BITM 0b1111111111

    #define REGA_CODE_LBIT  16 // low bit at 16
    #define P_CODE_LBIT     12
    #define REGB_CODE_LBIT  6
    #define REG_CODE_BITM   0b111111
    #define P_CODE_BITM     0b1111

    struct CheckResult meth_decode_impl(struct Decoder *self, int source_code) {
        unsigned short op_code = 0;
        op_code = (source_code & (OP_CODE_BITM << OP_CODE_LBIT)) >> OP_CODE_LBIT;
        self->reg_A = (source_code & (REG_CODE_BITM << REGA_CODE_LBIT)) >> REGA_CODE_LBIT;
        self->mid_p = (source_code & (P_CODE_BITM << P_CODE_LBIT)) >> P_CODE_LBIT;
        self->reg_B = (source_code & (REG_CODE_BITM << REGB_CODE_LBIT)) >> REGB_CODE_LBIT;
        self->reg_C = source_code & REG_CODE_BITM;

        switch (op_code) {
        // LOAD8 immediate
        case 0b0000000001:
            self->imme_type = BIT16_IMME;

            unsigned char invld_a_val[] = {PC, ZERO};
            struct Checker checker = {
                2,
                &invld_a_val,
                0,
                0,
                NULL,
                0,
                NULL,
                BC_NO_CONST
            };

            struct CheckResult check_result = self->check(self, checker);
            if (!check_result.check_pass) {
                return check_result;
            }
            break;
        // LOAD8 register address
        case 0b0000000010:
            self->imme_type = NONE_IMME;

            unsigned char invld_a_val[] = {PC, ZERO};
            struct Checker checker = {
                2,
                &invld_a_val,
                0,
                0,
                NULL,
                0,
                NULL,
                BC_CANT_BE_PC_SAME
            };

            struct CheckResult check_result = self->check(self, checker);
            if (!check_result.check_pass) {
                return check_result;
            }
            break;
        // LOAD16 immediate
        case 0b0000000011:
            self->imme_type = BIT16_IMME;

            unsigned char invld_a_val[] = {PC, ZERO};
            struct Checker checker = {
                2,
                &invld_a_val,
                0,
                0,
                NULL,
                0,
                NULL,
                BC_NO_CONST
            };

            struct CheckResult check_result = self->check(self, checker);
            if (!check_result.check_pass) {
                return check_result;
            }
            break;
        // LOAD16 register address
        case 0b0000000100:
            self->imme_type = NONE_IMME;

            unsigned char invld_a_val[] = {PC, ZERO};
            struct Checker checker = {
                2,
                &invld_a_val,
                0,
                0,
                NULL,
                0,
                NULL,
                BC_CANT_BE_PC_SAME
            };

            struct CheckResult check_result = self->check(self, checker);
            if (!check_result.check_pass) {
                return check_result;
            }
            break;
        // LOAD32 register address
        case 0b0000000101:
            self->imme_type = NONE_IMME;

            unsigned char invld_a_val[] = {PC, ZERO};
            struct Checker checker = {
                2,
                &invld_a_val,
                0,
                0,
                NULL,
                0,
                NULL,
                BC_NO_CONST
            };

            struct CheckResult check_result = self->check(self, checker);
            if (!check_result.check_pass) {
                return check_result;
            }
            break;

        // STORE8
        case 0b0000000110:
            self->imme_type = NONE_IMME;

            unsigned char invld_a_val[] = {PC, ZERO};
            unsigned char invld_b_val[] = {ZERO};
            unsigned char invld_c_val[] = {PC};
            struct Checker checker = {
                2,
                &invld_a_val,
                0,
                1,
                &invld_b_val,
                1,
                &invld_c_val,
                BC_NO_CONST
            };

            struct CheckResult check_result = self->check(self, checker);
            if (!check_result.check_pass) {
                return check_result;
            }
            break;
        // STORE16
        case 0b0000000111:
            self->imme_type = NONE_IMME;

            unsigned char invld_a_val[] = {PC, ZERO};
            unsigned char invld_b_val[] = {ZERO};
            unsigned char invld_c_val[] = {PC};
            struct Checker checker = {
                2,
                &invld_a_val,
                0,
                1,
                &invld_b_val,
                1,
                &invld_c_val,
                BC_NO_CONST
            };

            struct CheckResult check_result = self->check(self, checker);
            if (!check_result.check_pass) {
                return check_result;
            }
            break;
        // STORE32
        case 0b0000001000:
            self->imme_type = NONE_IMME;

            unsigned char invld_a_val[] = {PC, ZERO};
            unsigned char invld_b_val[] = {ZERO};
            unsigned char invld_c_val[] = {PC};
            struct Checker checker = {
                2,
                &invld_a_val,
                0,
                1,
                &invld_b_val,
                1,
                &invld_c_val,
                BC_NO_CONST
            };

            struct CheckResult check_result = self->check(self, checker);
            if (!check_result.check_pass) {
                return check_result;
            }
            break;


        // MOVE
        case 0b0000001001:
            self->imme_type = NONE_IMME;

            unsigned char invld_a_val[] = {PC, ZERO};
            struct Checker checker = {
                2,
                &invld_a_val,
                0,
                0,
                NULL,
                0,
                NULL,
                BC_NO_CONST
            };

            struct CheckResult check_result = self->check(self, checker);
            if (!check_result.check_pass) {
                return check_result;
            }
            break;


        // ADD immediate
        case 0b1000000000:
            self->imme_type = BIT10_IMME;

            unsigned char invld_a_val[] = {PC, ZERO};
            struct Checker checker = {
                2,
                &invld_a_val,
                1,
                0,
                NULL,
                0,
                NULL,
                B_ISNT_REG
            };

            struct CheckResult check_result = self->check(self, checker);
            if (!check_result.check_pass) {
                return check_result;
            }
            break;
        // ADD register
        case 0b1000000001:
            self->imme_type = NONE_IMME;

            unsigned char invld_a_val[] = {PC, ZERO};
            struct Checker checker = {
                2,
                &invld_a_val,
                0,
                0,
                NULL,
                0,
                NULL,
                BC_NO_CONST
            };

            struct CheckResult check_result = self->check(self, checker);
            if (!check_result.check_pass) {
                return check_result;
            }
            break;
        // SUB immediate (imme - reg)
        case 0b1000000010:
            self->imme_type = BIT10_IMME;

            unsigned char invld_a_val[] = {PC, ZERO};
            struct Checker checker = {
                2,
                &invld_a_val,
                1,
                0,
                NULL,
                0,
                NULL,
                B_ISNT_REG
            };

            struct CheckResult check_result = self->check(self, checker);
            if (!check_result.check_pass) {
                return check_result;
            }
            break;
        // SUB immediate (reg - imme)
        case 0b1000000011:
            self->imme_type = BIT10_IMME;

            unsigned char invld_a_val[] = {PC, ZERO};
            struct Checker checker = {
                2,
                &invld_a_val,
                1,
                0,
                NULL,
                0,
                NULL,
                B_ISNT_REG
            };

            struct CheckResult check_result = self->check(self, checker);
            if (!check_result.check_pass) {
                return check_result;
            }
            break;
        // SUB register
        case 0b1000000100:
            self->imme_type = NONE_IMME;

            unsigned char invld_a_val[] = {PC, ZERO};
            struct Checker checker = {
                2,
                &invld_a_val,
                0,
                0,
                NULL,
                0,
                NULL,
                BC_NO_CONST
            };

            struct CheckResult check_result = self->check(self, checker);
            if (!check_result.check_pass) {
                return check_result;
            }
            break;
        default:
            break;
        }
    }

    int meth_check_impl(struct Decoder *self, struct Checker checker) {
        for (int i_a_c = 0; i_a_c < checker.a_invld_num; i_a_c++) {
            if (self->reg_A == checker.a_invld_val[i_a_c]) {
            }
        }
    }
#endif
