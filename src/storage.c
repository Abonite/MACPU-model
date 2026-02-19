#include "storage.h"

struct Storage new_storage(unsigned int ram_start_addr, struct Ram ram, unsigned int rom_start_addr, struct Rom rom, unsigned char undefine_value) {
    struct Storage storage = {
        ram_start_addr,
        ram_start_addr + ram.size,
        ram,
        rom_start_addr,
        rom_start_addr + rom.size,
        rom,
        undefine_value,

        meth_read_impl,
        meth_write_impl
    };
    return storage;
};

unsigned char* meth_read_impl(struct Storage *self, unsigned int address) {
    unsigned char value[4] = {0, 0, 0, 0};

    unsigned int d = 0;
    for (unsigned int i = address; i < address + 4; i++) {
        if ((i >= self->ram_start_addr) && (i <= self->ram_end_addr)) {
            value[d] = self->ram.data[i];
        } else if ((i >= self->rom_start_addr) && (i <= self->rom_end_addr)) {
            value[d] = self->rom.data[i];
        } else {
            value[d] = self->undefine_value;
        }
        d = d + 1;
    }

    return value;
}

int meth_write_impl(struct Storage *self, unsigned int address, unsigned int size, unsigned char *data) {
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
