#include <stdlib.h>

#define __32bit__

#include "decoder.h"
#include "opcode.h"
#include "../ALU/register.h"

struct Decoder new_decoder() {
    struct Decoder result = {
        0,
        0,
        0,
        0,
        0,
        0,
        decoder_meth_decode_impl,
        decoder_meth_check_impl
    };

    return result;
}

#ifdef __32bit__
    #define OP_CODE_LBIT 22 // low bit at 22
    #define OP_CODE_BITM 0b1111111111

    #define REGT_CODE_LBIT  16 // low bit at 16
    #define REGS0_CODE_LBIT 10
    #define REGS1_CODE_LBIT 4
    #define REG_CODE_BITM   0b111111
    #define P_CODE_BITM     0b1111

    struct CheckResult decoder_meth_decode_impl(struct Decoder *self, unsigned char *source_code) {
        unsigned int code = 0;
        for (int i = 0; i < 4; i++) {
            code = code | (source_code[i] << (i * 8));
        }

        self->op_code = 0;
        self->op_code = (code & (OP_CODE_BITM << OP_CODE_LBIT)) >> OP_CODE_LBIT;
        self->reg_target = (code & (REG_CODE_BITM << REGT_CODE_LBIT)) >> REGT_CODE_LBIT;
        self->reg_source_0 = (code & (REG_CODE_BITM << REGS0_CODE_LBIT)) >> REGS0_CODE_LBIT;
        self->reg_source_1 = (code & (REG_CODE_BITM << REGS1_CODE_LBIT)) >> REGS1_CODE_LBIT;
        self->p = code & P_CODE_BITM;

        switch (self->op_code) {
            // LOAD8 immediate
            case LOAD8_IMME: {
                self->code_type = OP_TI;

                unsigned char invld_a_val[] = {PC, ZERO};
                struct Checker checker = {
                    2,
                    &invld_a_val,
                    0,
                    NULL,
                    0,
                    NULL,
                    S0S1_NO_CONST
                };

                struct CheckResult check_result = self->check(self, checker);
                return check_result;
            }
            // LOAD8 register address
            case LOAD8_REG: {
                self->code_type = OP_TSS;

                unsigned char invld_a_val[] = {PC, ZERO};
                struct Checker checker = {
                    2,
                    &invld_a_val,
                    0,
                    NULL,
                    0,
                    NULL,
                    S0S1_NO_CONST
                };

                struct CheckResult check_result = self->check(self, checker);
                return check_result;
            }
            // LOAD16 immediate
            case LOAD16_IMME: {
                self->code_type = OP_TI;

                unsigned char invld_a_val[] = {PC, ZERO};
                struct Checker checker = {
                    2,
                    &invld_a_val,
                    0,
                    NULL,
                    0,
                    NULL,
                    S0S1_NO_CONST
                };

                struct CheckResult check_result = self->check(self, checker);
                return check_result;
            }
            // LOAD16 register address
            case LOAD16_REG: {
                self->code_type = OP_TSS;

                unsigned char invld_a_val[] = {PC, ZERO};
                struct Checker checker = {
                    2,
                    &invld_a_val,
                    0,
                    NULL,
                    0,
                    NULL,
                    S0S1_NO_CONST
                };

                struct CheckResult check_result = self->check(self, checker);
                return check_result;
            }
            // LOAD32 register address
            case LOAD32:
                self->code_type = OP_TSS;

                unsigned char invld_a_val[] = {PC, ZERO};
                struct Checker checker = {
                    2,
                    &invld_a_val,
                    0,
                    NULL,
                    0,
                    NULL,
                    S0S1_NO_CONST
                };

                struct CheckResult check_result = self->check(self, checker);
                return check_result;
                break;

            // STORE8
            case STORE8: {
                self->code_type = OP_TSI;

                unsigned char invld_a_val[] = {PC, ZERO};
                unsigned char invld_b_val[] = {ZERO};
                unsigned char invld_c_val[] = {PC};
                struct Checker checker = {
                    2,
                    &invld_a_val,
                    1,
                    &invld_b_val,
                    1,
                    &invld_c_val,
                    S0S1_NO_CONST
                };

                struct CheckResult check_result = self->check(self, checker);
                return check_result;
            }
            // STORE16
            case STORE16: {
                self->code_type = OP_TSI;

                unsigned char invld_a_val[] = {PC, ZERO};
                unsigned char invld_b_val[] = {ZERO};
                unsigned char invld_c_val[] = {PC};
                struct Checker checker = {
                    2,
                    &invld_a_val,
                    1,
                    &invld_b_val,
                    1,
                    &invld_c_val,
                    S0S1_NO_CONST
                };

                struct CheckResult check_result = self->check(self, checker);
                return check_result;
            }
            // STORE32
            case STORE32: {
                self->code_type = OP_TSI;

                unsigned char invld_a_val[] = {PC, ZERO};
                unsigned char invld_b_val[] = {ZERO};
                unsigned char invld_c_val[] = {PC};
                struct Checker checker = {
                    2,
                    &invld_a_val,
                    1,
                    &invld_b_val,
                    1,
                    &invld_c_val,
                    S0S1_NO_CONST
                };

                struct CheckResult check_result = self->check(self, checker);
                return check_result;
            }


            // MOVE
            case MOVE: {
                self->code_type = OP_TS;

                unsigned char invld_a_val[] = {PC, ZERO};
                struct Checker checker = {
                    2,
                    &invld_a_val,
                    0,
                    NULL,
                    0,
                    NULL,
                    S0S1_NO_CONST
                };

                struct CheckResult check_result = self->check(self, checker);
                return check_result;
            }


            // ADD immediate
            case ADD_IMME: {
                self->code_type = OP_TSI;

                unsigned char invld_a_val[] = {PC, ZERO};
                struct Checker checker = {
                    2,
                    &invld_a_val,
                    0,
                    NULL,
                    0,
                    NULL,
                    S0S1_NO_CONST
                };

                struct CheckResult check_result = self->check(self, checker);
                return check_result;
            }
            // ADD register
            case ADD_REG: {
                self->code_type = OP_TSS;

                unsigned char invld_a_val[] = {PC, ZERO};
                struct Checker checker = {
                    2,
                    &invld_a_val,
                    0,
                    NULL,
                    0,
                    NULL,
                    S0S1_NO_CONST
                };

                struct CheckResult check_result = self->check(self, checker);
                return check_result;
            }
            // SUB immediate (reg - imme)
            case SUB_IMME_RI: {
                self->code_type = OP_TSI;

                unsigned char invld_a_val[] = {PC, ZERO};
                struct Checker checker = {
                    2,
                    &invld_a_val,
                    0,
                    NULL,
                    0,
                    NULL,
                    S0S1_NO_CONST
                };

                struct CheckResult check_result = self->check(self, checker);
                return check_result;
            }
            // SUB register
            case SUB_REG: {
                self->code_type = OP_TSS;

                unsigned char invld_a_val[] = {PC, ZERO};
                struct Checker checker = {
                    2,
                    &invld_a_val,
                    0,
                    NULL,
                    0,
                    NULL,
                    S0S1_NO_CONST
                };

                struct CheckResult check_result = self->check(self, checker);
                return check_result;
            }
            // JMP Immediate
            case JMP_IMME: {
                self->code_type = OP_I;

                struct Checker checker = {
                    0,
                    NULL,
                    0,
                    NULL,
                    0,
                    NULL,
                    S0S1_NO_CONST
                };

                struct CheckResult check_result = self->check(self, checker);
                return check_result;
            }
            // JMP register
            case JMP_REG: {
                self->code_type = OP_SS;

                struct Checker checker = {
                    0,
                    NULL,
                    0,
                    NULL,
                    0,
                    NULL,
                    S0S1_NO_CONST
                };

                struct CheckResult check_result = self->check(self, checker);
                return check_result;
            }
            default: {
                char error_msg[] = "Unknown instruction.\0";
                struct CheckResult check_result = {
                    0,
                    1,
                    &error_msg
                };
                return check_result;
            }
        }
    }

    struct CheckResult decoder_meth_check_impl(struct Decoder *self, struct Checker checker) {
        struct CheckResult check_result = {
            0,
            1,
            NULL
        };

        switch (self->code_type) {
            case OP_TI: {
                for (int i_a_c = 0; i_a_c < checker.target_invld_num; i_a_c++) {
                    if (self->reg_target == checker.target_invld_val[i_a_c]) {
                        // Error: invalid reg A
                        char error_msg[] = "Invalid reg A.\0";
                        check_result.error_msg = &error_msg;
                        return check_result;
                    }
                }
            }
            case OP_I: {
                check_result.check_pass = 1;
                check_result.is_fatal = 0;
                return check_result;
            }
            case OP_TS: {
                for (int i_t_c = 0; i_t_c < checker.target_invld_num; i_t_c++) {
                    if (self->reg_target == checker.target_invld_val[i_t_c]) {
                        char error_msg[] = "Invalid target register.\0";
                        check_result.error_msg = &error_msg;
                        return check_result;
                    }
                }

                for (int i_s0_c = 0; i_s0_c < checker.source_0_invld_num; i_s0_c++) {
                    if (self->reg_source_0 == checker.source_0_invld_val[i_s0_c]) {
                        char error_msg[] = "Invalid source 0 register.\0";
                        check_result.error_msg = &error_msg;
                        return check_result;
                    }
                }
            }
            case OP_TSI: {
                for (int i_t_c = 0; i_t_c < checker.target_invld_num; i_t_c++) {
                    if (self->reg_target == checker.target_invld_val[i_t_c]) {
                        char error_msg[] = "Invalid target register.\0";
                        check_result.error_msg = &error_msg;
                        return check_result;
                    }
                }

                for (int i_s0_c = 0; i_s0_c < checker.source_0_invld_num; i_s0_c++) {
                    if (self->reg_source_0 == checker.source_0_invld_val[i_s0_c]) {
                        char error_msg[] = "Invalid source 0 register.\0";
                        check_result.error_msg = &error_msg;
                        return check_result;
                    }
                }
            }
            case OP_TSS: {
                for (int i_t_c = 0; i_t_c < checker.target_invld_num; i_t_c++) {
                    if (self->reg_target == checker.target_invld_val[i_t_c]) {
                        char error_msg[] = "Invalid target register.\0";
                        check_result.error_msg = &error_msg;
                        return check_result;
                    }
                }

                for (int i_s0_c = 0; i_s0_c < checker.source_0_invld_num; i_s0_c++) {
                    if (self->reg_source_0 == checker.source_0_invld_val[i_s0_c]) {
                        char error_msg[] = "Invalid source 0 register.\0";
                        check_result.error_msg = &error_msg;
                        return check_result;
                    }
                }

                for (int i_s1_c = 0; i_s1_c < checker.source_1_invld_num; i_s1_c++) {
                    if (self->reg_source_1 == checker.source_1_invld_val[i_s1_c]) {
                        char error_msg[] = "Invalid source 1 register.\0";
                        check_result.error_msg = &error_msg;
                        return check_result;
                    }
                }

                switch (checker.bc_const) {
                    case S0S1_NO_CONST:
                        break;            
                    default:
                        // Error: invalid check const
                        char error_msg[] = "Invalid check const.\0";
                        check_result.is_fatal = 0;
                        check_result.error_msg = &error_msg;
                        return check_result;
                        break;
                }
            }
        }

        check_result.check_pass = 1;
        check_result.is_fatal = 0;
        return check_result;
    }
#endif
