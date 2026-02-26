#ifndef __INTERRUPT__
    #define __INTERRUPT__

    // FATAL
    #define UNKNOW_CODE         0
    #define INVALID_OPREG_A     1
    #define INVALID_OPREG_B     2
    #define INVALID_OPREG_C     3

    #define BC_SAME             10

    int interrupt(struct CheckResult decoder_result, struct Decoder *decoder, struct RegisterFile *register_file);
#endif