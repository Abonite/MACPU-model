#include "storage.h"

struct Storage new_storage(unsigned int ram_start_addr, struct Ram ram, unsigned int rom_start_addr, struct Rom rom, unsigned char undefine_value) {
    struct Storage storage = {
        (unsigned long long int)ram_start_addr,
        (unsigned long long int)ram_start_addr + (unsigned long long int)ram.size,
        ram,
        (unsigned long long int)rom_start_addr,
        (unsigned long long int)rom_start_addr + (unsigned long long int)rom.size,
        rom,
        undefine_value,

        storage_meth_read_impl,
        storage_meth_write_impl
    };
    return storage;
};

unsigned char* storage_meth_read_impl(struct Storage *self, unsigned int address) {
    unsigned char value[4] = {0, 0, 0, 0};

    unsigned int d = 0;
    for (unsigned long long int i = (unsigned long long int)address; i < (unsigned long long int)address + 4; i++) {
        if ((i >= self->ram_start_addr) && (i <= self->ram_end_addr)) {
            unsigned long long int t = i - self->ram_start_addr;
            value[d] = self->ram.data[t];
        } else if ((i >= self->rom_start_addr) && (i <= self->rom_end_addr)) {
            unsigned long long int t = i - self->rom_start_addr;
            value[d] = self->rom.data[t];
        } else {
            value[d] = self->undefine_value;
        }
        d = d + 1;
    }

    return value;
}

int storage_meth_write_impl(struct Storage *self, unsigned int address, unsigned int size, unsigned char *data) {
    unsigned int d = 0;
    for (unsigned int i = address; i < address + size; i++) {
        if ((i >= self->ram_start_addr) && (i <= self->ram_end_addr)) {
            self->ram.data[i] = data[d];
        } else if ((i >= self->rom_start_addr) && (i <= self->rom_end_addr)) {
            self->rom.data[i] = data[d];
        }
        d = d + 1;
    }
}
