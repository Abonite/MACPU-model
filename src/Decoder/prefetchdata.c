#define __32bit__

#include "prefetchdata.h"
#include "../ALU/registerfile.h"
#include "decoder.h"
#include "opcode.h"

struct DataFetcher new_datafetcher(struct Decoder *decoder, struct RegisterFile *rf) {
    struct DataFetcher result = {
        0,
        0
    };

    unsigned char *data;

    data = rf->read(rf, decoder->reg_source_0, decoder->reg_source_1);
    result.address = data[0] + data[1];

    switch (decoder->op_code) {
        case LOAD8_REG: {
            result.data_need_fetch = 1;
            break;
        }
        case LOAD16_REG: {
            result.data_need_fetch = 1;
            break;
        }
        case LOAD32: {
            result.data_need_fetch = 1;
            break;
        }
        case JMP_REG: {
            result.data_need_fetch = 1;
            break;
        }
        default:
            break;
    }

    return result;
}