#ifndef __DECODER__
    #define __DECODER__

    #ifdef __32bit__

        #define S0S1_NO_CONST   0

        struct Checker {
            int target_invld_num;
            unsigned char *target_invld_val;
            int source_0_invld_num;
            unsigned char *source_0_invld_val;
            int source_1_invld_num;
            unsigned char *source_1_invld_val;

            unsigned char bc_const;
        };

        struct CheckResult {
            int check_pass;
            int is_fatal;
            int err_type;
        };

        #define OP_TI  0
        #define OP_I   20
        #define OP_TS  40
        #define OP_TSI 60
        #define OP_TSS 80
        #define OP_TII 100
        #define OP_SS  120

        struct Decoder {
            unsigned short op_code;
            unsigned char reg_target;

            unsigned char code_type;
            unsigned char reg_source_0;
            unsigned char reg_source_1;
            unsigned char p;

            struct CheckResult (*decode)(struct Decoder *self, unsigned char *source_code);
            struct CheckResult (*check)(struct Decoder *self, struct Checker checker);
        };

        struct Decoder new_decoder();

        struct CheckResult decoder_meth_decode_impl(struct Decoder *self, unsigned char *source_code);
        struct CheckResult decoder_meth_check_impl(struct Decoder *self, struct Checker checker);
    #endif
#endif