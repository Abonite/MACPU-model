#include "registerfile.h"
#include "../Decoder/opcode.h"
#include "register.h"

struct RegisterFile new_registerfile() {
    struct RegisterFile result = {
        0,

        0,
        0,
        0,
        0,
        0,
        0,
        0,
        0,
        0,
        0,

        0,
        0,
        0,
        0,
        0,
        0,
        0,
        0,
        0,
        0,

        0,
        0,
        0,
        0,
        0,
        0,
        0,
        0,
        0,
        0,

        0,
        0,
        0,
        0,
        0,
        0,
        0,
        0,
        0,
        0,

        registerfile_meth_write_impl,
        registerfile_meth_read_impl,
        registerfile_meth_print_impl
    };

    return result;
}

int registerfile_meth_write_impl(struct RegisterFile *self, unsigned char register_label, unsigned int data) {
    switch (register_label) {
        case A0:
            self->REG_A0 = data;
            break;
        case A1:
            self->REG_A1 = data;
            break;
        case A2:
            self->REG_A2 = data;
            break;
        case A3:
            self->REG_A3 = data;
            break;
        case AR0:
            self->REG_AR0 = data;
            break;
        case AR1:
            self->REG_AR1 = data;
            break;
        case AR2:
            self->REG_AR2 = data;
            break;
        case ASS:
            self->REG_ASS = data;
            break;
        case ASP:
            self->REG_ASP = data;
            break;
        case ADS:
            self->REG_ADS = data;
            break;

        case B0:
            self->REG_B0 = data;
            break;
        case B1:
            self->REG_B1 = data;
            break;
        case B2:
            self->REG_B2 = data;
            break;
        case B3:
            self->REG_B3 = data;
            break;
        case BR0:
            self->REG_BR0 = data;
            break;
        case BR1:
            self->REG_BR1 = data;
            break;
        case BR2:
            self->REG_BR2 = data;
            break;
        case BSS:
            self->REG_BSS = data;
            break;
        case BSP:
            self->REG_BSP = data;
            break;
        case BDS:
            self->REG_BDS = data;
            break;

        case C0:
            self->REG_C0 = data;
            break;
        case C1:
            self->REG_C1 = data;
            break;
        case C2:
            self->REG_C2 = data;
            break;
        case C3:
            self->REG_C3 = data;
            break;
        case CR0:
            self->REG_CR0 = data;
            break;
        case CR1:
            self->REG_CR1 = data;
            break;
        case CR2:
            self->REG_CR2 = data;
            break;
        case CSS:
            self->REG_CSS = data;
            break;
        case CSP:
            self->REG_CSP = data;
            break;
        case CDS:
            self->REG_CDS = data;
            break;

        case D0:
            self->REG_D0 = data;
            break;
        case D1:
            self->REG_D1 = data;
            break;
        case D2:
            self->REG_D2 = data;
            break;
        case D3:
            self->REG_D3 = data;
            break;
        case DR0:
            self->REG_DR0 = data;
            break;
        case DR1:
            self->REG_DR1 = data;
            break;
        case DR2:
            self->REG_DR2 = data;
            break;
        case DSS:
            self->REG_DSS = data;
            break;
        case DSP:
            self->REG_DSP = data;
            break;
        case DDS:
            self->REG_DDS = data;
            break;

        default:
            break;
    }
}

unsigned int* registerfile_meth_read_impl(struct RegisterFile *self, unsigned char register_0, unsigned char register_1) {
    unsigned int data[2] = {0, 0};

    switch (register_0) {
        case A0:
            data[0] = self->REG_A0;
            break;
        case A1:
            data[0] = self->REG_A1;
            break;
        case A2:
            data[0] = self->REG_A2;
            break;
        case A3:
            data[0] = self->REG_A3;
            break;
        case AR0:
            data[0] = self->REG_AR0;
            break;
        case AR1:
            data[0] = self->REG_AR1;
            break;
        case AR2:
            data[0] = self->REG_AR2;
            break;
        case ASS:
            data[0] = self->REG_ASS;
            break;
        case ASP:
            data[0] = self->REG_ASP;
            break;
        case ADS:
            data[0] = self->REG_ADS;
            break;

        case B0:
            data[0] = self->REG_B0;
            break;
        case B1:
            data[0] = self->REG_B1;
            break;
        case B2:
            data[0] = self->REG_B2;
            break;
        case B3:
            data[0] = self->REG_B3;
            break;
        case BR0:
            data[0] = self->REG_BR0;
            break;
        case BR1:
            data[0] = self->REG_BR1;
            break;
        case BR2:
            data[0] = self->REG_BR2;
            break;
        case BSS:
            data[0] = self->REG_BSS;
            break;
        case BSP:
            data[0] = self->REG_BSP;
            break;
        case BDS:
            data[0] = self->REG_BDS;
            break;

        case C0:
            data[0] = self->REG_C0;
            break;
        case C1:
            data[0] = self->REG_C1;
            break;
        case C2:
            data[0] = self->REG_C2;
            break;
        case C3:
            data[0] = self->REG_C3;
            break;
        case CR0:
            data[0] = self->REG_CR0;
            break;
        case CR1:
            data[0] = self->REG_CR1;
            break;
        case CR2:
            data[0] = self->REG_CR2;
            break;
        case CSS:
            data[0] = self->REG_CSS;
            break;
        case CSP:
            data[0] = self->REG_CSP;
            break;
        case CDS:
            data[0] = self->REG_CDS;
            break;

        case D0:
            data[0] = self->REG_D0;
            break;
        case D1:
            data[0] = self->REG_D1;
            break;
        case D2:
            data[0] = self->REG_D2;
            break;
        case D3:
            data[0] = self->REG_D3;
            break;
        case DR0:
            data[0] = self->REG_DR0;
            break;
        case DR1:
            data[0] = self->REG_DR1;
            break;
        case DR2:
            data[0] = self->REG_DR2;
            break;
        case DSS:
            data[0] = self->REG_DSS;
            break;
        case DSP:
            data[0] = self->REG_DSP;
            break;
        case DDS:
            data[0] = self->REG_DDS;
            break;

        default:
            break;
    }

    switch (register_1) {
        case A0:
            data[1] = self->REG_A0;
            break;
        case A1:
            data[1] = self->REG_A1;
            break;
        case A2:
            data[1] = self->REG_A2;
            break;
        case A3:
            data[1] = self->REG_A3;
            break;
        case AR0:
            data[1] = self->REG_AR0;
            break;
        case AR1:
            data[1] = self->REG_AR1;
            break;
        case AR2:
            data[1] = self->REG_AR2;
            break;
        case ASS:
            data[1] = self->REG_ASS;
            break;
        case ASP:
            data[1] = self->REG_ASP;
            break;
        case ADS:
            data[1] = self->REG_ADS;
            break;

        case B0:
            data[1] = self->REG_B0;
            break;
        case B1:
            data[1] = self->REG_B1;
            break;
        case B2:
            data[1] = self->REG_B2;
            break;
        case B3:
            data[1] = self->REG_B3;
            break;
        case BR0:
            data[1] = self->REG_BR0;
            break;
        case BR1:
            data[1] = self->REG_BR1;
            break;
        case BR2:
            data[1] = self->REG_BR2;
            break;
        case BSS:
            data[1] = self->REG_BSS;
            break;
        case BSP:
            data[1] = self->REG_BSP;
            break;
        case BDS:
            data[1] = self->REG_BDS;
            break;

        case C0:
            data[1] = self->REG_C0;
            break;
        case C1:
            data[1] = self->REG_C1;
            break;
        case C2:
            data[1] = self->REG_C2;
            break;
        case C3:
            data[1] = self->REG_C3;
            break;
        case CR0:
            data[1] = self->REG_CR0;
            break;
        case CR1:
            data[1] = self->REG_CR1;
            break;
        case CR2:
            data[1] = self->REG_CR2;
            break;
        case CSS:
            data[1] = self->REG_CSS;
            break;
        case CSP:
            data[1] = self->REG_CSP;
            break;
        case CDS:
            data[1] = self->REG_CDS;
            break;

        case D0:
            data[1] = self->REG_D0;
            break;
        case D1:
            data[1] = self->REG_D1;
            break;
        case D2:
            data[1] = self->REG_D2;
            break;
        case D3:
            data[1] = self->REG_D3;
            break;
        case DR0:
            data[1] = self->REG_DR0;
            break;
        case DR1:
            data[1] = self->REG_DR1;
            break;
        case DR2:
            data[1] = self->REG_DR2;
            break;
        case DSS:
            data[1] = self->REG_DSS;
            break;
        case DSP:
            data[1] = self->REG_DSP;
            break;
        case DDS:
            data[1] = self->REG_DDS;
            break;

        default:
            break;
    }

    return data;
}

int registerfile_meth_print_impl(struct RegisterFile *self) {
    printf("[DEBUG]: Registers value is:\n");
    printf("%%A0: %x, %d, %b\n", self->REG_A0, self->REG_A0, self->REG_A0);
    printf("%%A1: %x, %d, %b\n", self->REG_A1, self->REG_A1, self->REG_A1);
    printf("%%A2: %x, %d, %b\n", self->REG_A2, self->REG_A2, self->REG_A2);
    printf("%%A3: %x, %d, %b\n", self->REG_A3, self->REG_A3, self->REG_A3);
    printf("%%AR0: %x, %d, %b\n", self->REG_AR0, self->REG_AR0, self->REG_AR0);
    printf("%%AR1: %x, %d, %b\n", self->REG_AR1, self->REG_AR1, self->REG_AR1);
    printf("%%AR2: %x, %d, %b\n", self->REG_AR2, self->REG_AR2, self->REG_AR2);
    printf("%%ASS: %x, %d, %b\n", self->REG_ASS, self->REG_ASS, self->REG_ASS);
    printf("%%ASP: %x, %d, %b\n", self->REG_ASP, self->REG_ASP, self->REG_ASP);
    printf("%%ADS: %x, %d, %b\n", self->REG_ADS, self->REG_ADS, self->REG_ADS);

    printf("%%B0: %x, %d, %b\n", self->REG_B0, self->REG_B0, self->REG_B0);
    printf("%%B1: %x, %d, %b\n", self->REG_B1, self->REG_B1, self->REG_B1);
    printf("%%B2: %x, %d, %b\n", self->REG_B2, self->REG_B2, self->REG_B2);
    printf("%%B3: %x, %d, %b\n", self->REG_B3, self->REG_B3, self->REG_B3);
    printf("%%BR0: %x, %d, %b\n", self->REG_BR0, self->REG_BR0, self->REG_BR0);
    printf("%%BR1: %x, %d, %b\n", self->REG_BR1, self->REG_BR1, self->REG_BR1);
    printf("%%BR2: %x, %d, %b\n", self->REG_BR2, self->REG_BR2, self->REG_BR2);
    printf("%%BSS: %x, %d, %b\n", self->REG_BSS, self->REG_BSS, self->REG_BSS);
    printf("%%BSP: %x, %d, %b\n", self->REG_BSP, self->REG_BSP, self->REG_BSP);
    printf("%%BDS: %x, %d, %b\n", self->REG_BDS, self->REG_BDS, self->REG_BDS);

    printf("%%C0: %x, %d, %b\n", self->REG_C0, self->REG_C0, self->REG_C0);
    printf("%%C1: %x, %d, %b\n", self->REG_C1, self->REG_C1, self->REG_C1);
    printf("%%C2: %x, %d, %b\n", self->REG_C2, self->REG_C2, self->REG_C2);
    printf("%%C3: %x, %d, %b\n", self->REG_C3, self->REG_C3, self->REG_C3);
    printf("%%CR0: %x, %d, %b\n", self->REG_CR0, self->REG_CR0, self->REG_CR0);
    printf("%%CR1: %x, %d, %b\n", self->REG_CR1, self->REG_CR1, self->REG_CR1);
    printf("%%CR2: %x, %d, %b\n", self->REG_CR2, self->REG_CR2, self->REG_CR2);
    printf("%%CSS: %x, %d, %b\n", self->REG_CSS, self->REG_CSS, self->REG_CSS);
    printf("%%CSP: %x, %d, %b\n", self->REG_CSP, self->REG_CSP, self->REG_CSP);
    printf("%%CDS: %x, %d, %b\n", self->REG_CDS, self->REG_CDS, self->REG_CDS);

    printf("%%D0: %x, %d, %b\n", self->REG_D0, self->REG_D0, self->REG_D0);
    printf("%%D1: %x, %d, %b\n", self->REG_D1, self->REG_D1, self->REG_D1);
    printf("%%D2: %x, %d, %b\n", self->REG_D2, self->REG_D2, self->REG_D2);
    printf("%%D3: %x, %d, %b\n", self->REG_D3, self->REG_D3, self->REG_D3);
    printf("%%DR0: %x, %d, %b\n", self->REG_DR0, self->REG_DR0, self->REG_DR0);
    printf("%%DR1: %x, %d, %b\n", self->REG_DR1, self->REG_DR1, self->REG_DR1);
    printf("%%DR2: %x, %d, %b\n", self->REG_DR2, self->REG_DR2, self->REG_DR2);
    printf("%%DSS: %x, %d, %b\n", self->REG_DSS, self->REG_DSS, self->REG_DSS);
    printf("%%DSP: %x, %d, %b\n", self->REG_DSP, self->REG_DSP, self->REG_DSP);
    printf("%%DDS: %x, %d, %b\n", self->REG_DDS, self->REG_DDS, self->REG_DDS);
    printf("\n");
}