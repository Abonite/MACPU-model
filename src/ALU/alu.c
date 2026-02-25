#define __32bit__

#include "registerfile.h"
#include "register.h"
#include "../Decoder/opcode.h"
#include "../FetchInst/programcounter.h"
#include "../Decoder/decoder.h"

int integer_caculate_unit (
    struct Decoder *decoder,
    unsigned int fetched_immediate,
    struct ProgramCounter *pc,
    struct RegisterFile *rf
) {
    unsigned int short_inner_immediate_number = (((unsigned int)decoder->reg_source_1) << 4) | (unsigned int)decoder->p;
    unsigned int inner_immediate_number = (((unsigned int)decoder->reg_source_0) << 10) | short_inner_immediate_number;
    unsigned int long_inner_immediate_number = (((unsigned int)decoder->reg_target) << 16) | inner_immediate_number;
    for (int i = 1; i <= 16; i ++) {
        short_inner_immediate_number = short_inner_immediate_number | (short_inner_immediate_number & 0b1000000000) << i;
    }

    for (int i = 1; i <= 16; i ++) {
        inner_immediate_number = inner_immediate_number | (inner_immediate_number & 0b1000000000000000) << i;
    }

    for (int i = 1; i <= 10; i ++) {
        long_inner_immediate_number = long_inner_immediate_number | (long_inner_immediate_number & 0b1000000000000000000000) << i;
    }

    switch (decoder->op_code) {
        case LOAD8_IMME: {
            rf->write(rf, decoder->reg_target, inner_immediate_number);
            break;
        }
        case LOAD8_REG: {
            rf->write(rf, decoder->reg_target, fetched_immediate);
            break;
        }
        case LOAD16_IMME: {
            rf->write(rf, decoder->reg_target, inner_immediate_number);
            break;
        }
        case LOAD16_REG: {
            rf->write(rf, decoder->reg_target, fetched_immediate);
            break;
        }
        case LOAD32: {
            rf->write(rf, decoder->reg_target, fetched_immediate);
            break;
        }
        case MOVE: {
            if (decoder->reg_source_0 == 0b101001) {
                unsigned int t = pc->current_value;
                rf->write(rf, decoder->reg_target, t);
            } else {
                unsigned int *t = rf->read(rf, decoder->reg_source_0, 0);
                rf->write(rf, decoder->reg_target, t[0]);
            }
            break;
        }
        case ADD_IMME: {
            unsigned int *t = rf->read(rf, decoder->reg_source_0, 0);
            rf->write(rf, decoder->reg_target, t[0] + short_inner_immediate_number);
            break;
        }
        case ADD_REG: {
            unsigned int *t = rf->read(rf, decoder->reg_source_0, decoder->reg_source_1);
            rf->write(rf, decoder->reg_target, t[0] + t[1]);
            break;
        }
        case SUB_IMME_RI: {
            unsigned int *t = rf->read(rf, decoder->reg_source_0, 0);
            rf->write(rf, decoder->reg_target, t[0] - short_inner_immediate_number);
            break;
        }
        case SUB_REG: {
            unsigned int *t = rf->read(rf, decoder->reg_source_0, decoder->reg_source_1);
            rf->write(rf, decoder->reg_target, t[0] - t[1]);
            break;
        }
        case EQ_IMME: {
            unsigned int *t = rf->read(rf, decoder->reg_source_0, 0);
            if (t[0] == short_inner_immediate_number) {
                rf->write(rf, decoder->reg_target, 1);
            } else {
                rf->write(rf, decoder->reg_target, 0);
            }
            break;
        }
        case EQ_REG: {
            unsigned int *t = rf->read(rf, decoder->reg_source_0, decoder->reg_source_1);
            if (t[0] == t[1]) {
                rf->write(rf, decoder->reg_target, 1);
            } else {
                rf->write(rf, decoder->reg_target, 0);
            }
            break;
        }
        case JMP_IMME: {
            pc->current_value = long_inner_immediate_number;
            break;
        }
        case JMP_REG: {
            unsigned int *t = rf->read(rf, decoder->reg_target, 0);
            pc->current_value = t[0];
            break;
        }
        case OJMP_IMME: {
            unsigned int *t = rf->read(rf, decoder->reg_target, 0);
            if (t[0]) {
                pc->current_value = inner_immediate_number;
            }
            break;
        }
        case OJMP_REG: {
            unsigned int *t = rf->read(rf, decoder->reg_target, decoder->reg_source_0);
            if (t[0]) {
                pc->current_value = t[1];
            }
            break;
        }
        case ZJMP_IMME: {
            unsigned int *t = rf->read(rf, decoder->reg_target, 0);
            if (!t[0]) {
                pc->current_value = inner_immediate_number;
            }
            break;
        }
        case ZJMP_REG: {
            unsigned int *t = rf->read(rf, decoder->reg_target, decoder->reg_source_0);
            if (!t[0]) {
                pc->current_value = t[1];
            }
            break;
        }
        default:
            break;
    }
}