#ifdef __32bit__
    #define PC      0b101001
    #define ZERO    0b000000

    #define A0  1
    #define A1  2
    #define A2  3
    #define A3  4
    #define AR0 5
    #define AR1 6
    #define AR2 7
    #define ASS 8
    #define ASP 9
    #define ADS 10

    #define B0  11
    #define B1  12
    #define B2  13
    #define B3  14
    #define BR0 15
    #define BR1 16
    #define BR2 17
    #define BSS 18
    #define BSP 19
    #define BDS 20

    #define C0  21
    #define C1  22
    #define C2  23
    #define C3  24
    #define CR0 25
    #define CR1 26
    #define CR2 27
    #define CSS 28
    #define CSP 29
    #define CDS 30

    #define D0  31
    #define D1  32
    #define D2  33
    #define D3  34
    #define DR0 35
    #define DR1 36
    #define DR2 37
    #define DSS 38
    #define DSP 39
    #define DDS 40

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
        char *error_msg;
    };

    #define OP_TI  0
    #define OP_I   20
    #define OP_TS  40
    #define OP_TSI 60
    #define OP_TSS 80
    #define OP_TII 100

    struct Decoder {
        unsigned char reg_target;

        unsigned char code_type;
        unsigned char reg_source_0;
        unsigned char reg_source_1;
        unsigned char p;

        struct CheckResult (*decode)(struct Decoder *self, unsigned char *source_code);
        struct CheckResult (*check)(struct Decoder *self, struct Checker checker);
    };

    struct Decoder new_decoder();

    struct CheckResult meth_decode_impl(struct Decoder *self, unsigned char *source_code);
    struct CheckResult meth_check_impl(struct Decoder *self, struct Checker checker);
#endif