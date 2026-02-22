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
    unsigned int inner_immediate_number = (((unsigned int)decoder->reg_source_0) << 10) | (((unsigned int)decoder->reg_source_1) << 4) | (unsigned int)decoder->p;
    unsigned int long_inner_immediate_number = (((unsigned int)decoder->reg_target) << 16) | inner_immediate_number;
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
        case JMP_IMME: {
            pc->current_value = long_inner_immediate_number;
            break;
        }
        case JMP_REG: {
            pc->current_value = fetched_immediate;
            break;
        }
        default:
            break;
    }
}