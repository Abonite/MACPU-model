#ifndef __REGISTER_FILE__
    #define __REGISTER_FILE__

    struct RegisterFile {
        unsigned int REG_ZERO;

        unsigned int REG_A0;
        unsigned int REG_A1;
        unsigned int REG_A2;
        unsigned int REG_A3;
        unsigned int REG_AR0;
        unsigned int REG_AR1;
        unsigned int REG_AR2;
        unsigned int REG_ASS;
        unsigned int REG_ASP;
        unsigned int REG_ADS;

        unsigned int REG_B0;
        unsigned int REG_B1;
        unsigned int REG_B2;
        unsigned int REG_B3;
        unsigned int REG_BR0;
        unsigned int REG_BR1;
        unsigned int REG_BR2;
        unsigned int REG_BSS;
        unsigned int REG_BSP;
        unsigned int REG_BDS;

        unsigned int REG_C0;
        unsigned int REG_C1;
        unsigned int REG_C2;
        unsigned int REG_C3;
        unsigned int REG_CR0;
        unsigned int REG_CR1;
        unsigned int REG_CR2;
        unsigned int REG_CSS;
        unsigned int REG_CSP;
        unsigned int REG_CDS;

        unsigned int REG_D0;
        unsigned int REG_D1;
        unsigned int REG_D2;
        unsigned int REG_D3;
        unsigned int REG_DR0;
        unsigned int REG_DR1;
        unsigned int REG_DR2;
        unsigned int REG_DSS;
        unsigned int REG_DSP;
        unsigned int REG_DDS;

        int (*write)(struct RegisterFile *self, unsigned char register, unsigned int data);
        unsigned int* (*read)(struct RegisterFile *self, unsigned char register_0, unsigned char register_1);
        int (*print)(struct Registerfile *self);
    };

    struct RegisterFile new_registerfile();

    int registerfile_meth_write_impl(struct RegisterFile *self, unsigned char register, unsigned int data);
    unsigned int* registerfile_meth_read_impl(struct RegisterFile *self, unsigned char register_0, unsigned char register_1);
    int registerfile_meth_print_impl();
#endif