#include "RAM/ram.h"
#include "ROM/rom.h"

struct Storage {
    unsigned int ram_start_addr;
    unsigned int ram_end_addr;
    struct Ram ram;
    unsigned int rom_start_addr;
    unsigned int rom_end_addr;
    struct Rom rom;

    unsigned char undefine_value;

    unsigned char* (*read)(struct Storage *self, unsigned int address);
    int (*write)(struct Storage *self, unsigned int address, unsigned int size, unsigned char *data);
};

struct Storage new_storage(unsigned int ram_start_addr, struct Ram ram, unsigned int rom_start_addr, struct Rom rom, unsigned char undefine_value);
unsigned char* meth_read_impl(struct Storage *self, unsigned int address);
int meth_write_impl(struct Storage *self, unsigned int address, unsigned int size, unsigned char *data);