#define __32bit__

#include "../FetchInst/programcounter.h"
#include "decoder.h"
#include "../ALU/registerfile.h"
#include "../ALU/register.h"

int interrupt(struct CheckResult decoder_result, struct Decoder *decoder, struct RegisterFile *register_file, unsigned int current_address) {
    if (!decoder_result.check_pass && decoder_result.is_fatal) {
        printf("[FATAL]: At: %x, %d, %b; code: %d;\n", current_address, current_address, current_address, decoder_result.err_type);
        register_file->print(register_file);
        register_file->write(register_file, A3, decoder_result.err_type);
        decoder->code_type = OP_I;
        decoder->reg_target = 0b111111;
        decoder->reg_source_0 = 0b111111;
        decoder->reg_source_1 = 0b111111;
        decoder->p = 0b1000;
        decoder->op_code = 0b1100000000; // JMP [0xFFFFFFF8]
        return 1;
    } else if (!decoder_result.check_pass && !decoder_result.is_fatal) {
        printf("[ERROR]: code: %d;\n", decoder_result.err_type);
        return -1;
    }

    return 0;
}
