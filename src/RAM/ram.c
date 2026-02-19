#include "ram.h"
#include <stdlib.h>

struct Ram new_ram(unsigned int ram_size, unsigned char init_value) {
    struct Ram ram = {
        ram_size,
        (unsigned char*)(malloc(ram_size * sizeof(unsigned char)))
    };

    for (unsigned int i = 0; i < ram_size; i ++) {
        ram.data[i] = init_value;
    }

    return ram;
};
