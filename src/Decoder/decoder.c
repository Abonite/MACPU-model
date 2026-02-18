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

    struct CheckResult meth_check_impl(struct Decoder *self, struct Checker checker) {
        struct CheckResult check_result = {
            0,
            1,
            NULL
        };

        for (int i_a_c = 0; i_a_c < checker.a_invld_num; i_a_c++) {
            if (self->reg_A == checker.a_invld_val[i_a_c]) {
                // Error: invalid reg A
                char error_msg[] = "Invalid reg A.\0";
                check_result.error_msg = &error_msg;
                return check_result;
            }
        }

        for (int i_c_c = 0; i_c_c < checker.c_invld_num; i_c_c++) {
            if (self->reg_C == checker.c_invld_val[i_c_c]) {
                // Error: invalid reg C
                char error_msg[] = "Invalid reg C.\0";
                check_result.error_msg = &error_msg;
                return check_result;
            }
        }

        if (!checker.p_vld && (self->mid_p != 0)) {
            // Error: invalid p
            char error_msg[] = "Invalid P value.\0";
            check_result.error_msg = &error_msg;
            return check_result;
        }

        switch (checker.bc_const) {
            case BC_NO_CONST:
                for (int i_b_c = 0; i_b_c < checker.b_invld_num; i_b_c++) {
                    if (self->reg_B == checker.b_invld_val[i_b_c]) {
                        // Error: invalid reg B
                        char error_msg[] = "Invalid reg B.\0";
                        check_result.error_msg = &error_msg;
                        return check_result;
                    }
                }
                break;
            case BC_CANT_BE_PC_SAME:
                for (int i_b_c = 0; i_b_c < checker.b_invld_num; i_b_c++) {
                    if (self->reg_B == checker.b_invld_val[i_b_c]) {
                        // Error: invalid reg B
                        char error_msg[] = "Invalid reg B.\0";
                        check_result.error_msg = &error_msg;
                        return check_result;
                    }
                }

                if ((self->reg_B == self->reg_C) && (self->reg_B == PC)) {
                    // Error: reg B equ reg C
                    char error_msg[] = "Reg B can't be same as reg C, which is equal to PC.\0";
                    check_result.error_msg = &error_msg;
                    return check_result;
                }
                break;
            case B_ISNT_REG:
                break;
            
            default:
                // Error: invalid check const
                char error_msg[] = "Invalid check const.\0";
                check_result.is_fatal = 0;
                check_result.error_msg = &error_msg;
                return check_result;
                break;
        }

        check_result.check_pass = 1;
        check_result.is_fatal = 0;
        return check_result;
    }
#endif
