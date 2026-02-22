#define __32bit__

#include "../FetchInst/programcounter.h"
#include "register.h"
#include "../Decoder/opcode.h"
#include "../FetchInst/programcounter.h"
#include "../Decoder/decoder.h"

int integer_caculate_unit (
    struct Decoder *decoder,
    unsigned char *immediate,
    struct ProgramCounter *pc,
    struct RegisterFile *rf
) {
    switch (decoder->op_code) {
        case JMP_IMME: {
            unsigned int immediate_number = (((unsigned int)decoder->reg_source_0) << 16) | (((unsigned int)decoder->reg_source_1) << 10) | (unsigned int)decoder->p;
            for (int i = 1; i <= 10; i ++) {
                immediate_number = (immediate_number & 0b00000000001000000000000000000000) << i;
            }

            pc->current_value = immediate_number;
            break;
        }
        case JMP_REG: {
            for (int i = 3; i >= 0; i--) {
                pc->current_value = pc->current_value | (immediate[i] << (i * 8));
            }
            break;
        }
        default:
            break;
    }
}